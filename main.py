from fastapi import FastAPI, WebSocket, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import json
import os
from datetime import datetime
import sqlite3
from pydantic import BaseModel
from typing import List, Optional

# Database initialization
DATABASE = "chat.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (sender_id) REFERENCES users(id),
            FOREIGN KEY (receiver_id) REFERENCES users(id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Models
class User(BaseModel):
    username: str

class UserResponse(BaseModel):
    id: int
    username: str

class Message(BaseModel):
    content: str
    receiver_id: Optional[int] = None

class MessageResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: Optional[int]
    content: str
    created_at: str
    sender_username: str

# WebSocket manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: dict = {}

    async def connect(self, websocket: WebSocket, user_id: int):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: int):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def broadcast(self, data: dict):
        for connection in self.active_connections.values():
            try:
                await connection.send_json(data)
            except:
                pass

    async def send_personal(self, user_id: int, data: dict):
        if user_id in self.active_connections:
            try:
                await self.active_connections[user_id].send_json(data)
            except:
                pass

manager = ConnectionManager()

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

# FastAPI app
app = FastAPI(lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes

@app.post("/api/users/register", response_model=UserResponse)
async def register_user(user: User):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (user.username,))
        conn.commit()
        user_id = cursor.lastrowid
        return {"id": user_id, "username": user.username}
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        conn.close()

@app.post("/api/users/login", response_model=UserResponse)
async def login_user(user: User):
    """Login endpoint - finds existing user by username"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, username FROM users WHERE username = ?", (user.username,))
        result = cursor.fetchone()
        
        if result:
            return {"id": result[0], "username": result[1]}
        else:
            raise HTTPException(status_code=401, detail="User not found")
    finally:
        conn.close()

@app.get("/api/users", response_model=List[UserResponse])
async def get_users(search: Optional[str] = Query(None)):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    if search:
        cursor.execute("SELECT id, username FROM users WHERE username LIKE ?", (f"%{search}%",))
    else:
        cursor.execute("SELECT id, username FROM users")
    
    users = cursor.fetchall()
    conn.close()
    
    return [{"id": u[0], "username": u[1]} for u in users]

@app.post("/api/messages")
async def send_message(sender_id: int, message: Message):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO messages (sender_id, receiver_id, content) VALUES (?, ?, ?)",
        (sender_id, message.receiver_id, message.content)
    )
    conn.commit()
    msg_id = cursor.lastrowid
    conn.close()
    
    # Broadcast to connected users
    cursor = sqlite3.connect(DATABASE).cursor()
    cursor.execute("SELECT username FROM users WHERE id = ?", (sender_id,))
    sender = cursor.fetchone()[0]
    
    await manager.broadcast({
        "type": "message",
        "id": msg_id,
        "sender_id": sender_id,
        "sender_username": sender,
        "receiver_id": message.receiver_id,
        "content": message.content,
        "timestamp": datetime.now().isoformat()
    })
    
    return {"status": "ok", "message_id": msg_id}

@app.get("/api/messages", response_model=List[MessageResponse])
async def get_messages(user_id: Optional[int] = None, search: Optional[str] = None):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    if search:
        cursor.execute(
            """SELECT m.id, m.sender_id, m.receiver_id, m.content, m.created_at, u.username 
               FROM messages m JOIN users u ON m.sender_id = u.id 
               WHERE m.content LIKE ? ORDER BY m.created_at DESC""",
            (f"%{search}%",)
        )
    else:
        cursor.execute(
            """SELECT m.id, m.sender_id, m.receiver_id, m.content, m.created_at, u.username 
               FROM messages m JOIN users u ON m.sender_id = u.id 
               ORDER BY m.created_at DESC LIMIT 100"""
        )
    
    messages = cursor.fetchall()
    conn.close()
    
    return [
        {
            "id": m[0],
            "sender_id": m[1],
            "receiver_id": m[2],
            "content": m[3],
            "created_at": m[4],
            "sender_username": m[5]
        }
        for m in messages
    ]

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            msg_data = json.loads(data)
            
            # Save message to database
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO messages (sender_id, receiver_id, content) VALUES (?, ?, ?)",
                (user_id, msg_data.get("receiver_id"), msg_data.get("content"))
            )
            conn.commit()
            conn.close()
            
            # Broadcast
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM users WHERE id = ?", (user_id,))
            username = cursor.fetchone()[0]
            conn.close()
            
            await manager.broadcast({
                "type": "message",
                "sender_id": user_id,
                "sender_username": username,
                "receiver_id": msg_data.get("receiver_id"),
                "content": msg_data.get("content"),
                "timestamp": datetime.now().isoformat()
            })
    except:
        manager.disconnect(user_id)

# Serve frontend
@app.get("/")
async def root():
    return FileResponse("static/index.html")

# Mount static files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
