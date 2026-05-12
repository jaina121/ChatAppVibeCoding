# 💬 ChatApp - Real-time Chat Website

A modern, real-time chat application built with Python FastAPI and vanilla JavaScript. Features real-time messaging, user management, and a beautiful responsive UI.

> **⏱️ Quick Submission?** See [QUICKSTART.md](QUICKSTART.md) for a 30-minute path to deployment!

## 🎯 Features

### ✅ Core Features
- **User Management**
  - Register new users
  - Search users by username
  - Display list of all users
  - Unique username validation

- **Messaging**
  - Send and receive real-time messages
  - View complete chat history
  - Search messages by content
  - Direct user-to-user messaging
  - Timestamp for each message

- **Frontend**
  - Clean, modern web interface
  - Real-time message display
  - User list with search functionality
  - Responsive design (desktop & mobile)
  - Beautiful gradient UI with dark/light message bubbles
  - Online/offline status indicator

### 🔐 Session & Authentication Improvements (NEW)

- **Login for existing users:** Single auth form now supports logging in existing accounts via `POST /api/users/login`.
- **Smart register/login flow:** The auth form tries to `login` first and falls back to `register` automatically if the user does not exist.
- **Logout:** Clear session with a visible logout button; closes the WebSocket and clears `localStorage`.
- **Session persistence:** Browser `localStorage` preserves the logged-in user; the app auto-restores the session on page reload.
- **Account switching:** Logout and login as a different user without losing other users' chat history (history is stored in the DB).
- **Client-side filtering:** Incoming WebSocket messages are shown only when they belong to the currently open conversation (prevents message interleaving in the UI).

- **Backend**
  - FastAPI Python backend
  - RESTful API endpoints
  - WebSocket support for real-time communication
  - SQLite database for persistent storage
  - CORS enabled for cross-origin requests

### 🚀 Additional Features
- ✨ Modern gradient UI design
- 🔄 Real-time WebSocket communication
- 📱 Fully responsive mobile UI
- 🔍 Search functionality for users and messages
- 💾 Persistent database storage
- 🐳 Docker support for easy deployment

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** SQLite
- **Real-time:** WebSockets
- **Deployment:** Docker, Cloud platforms (Render )

## 📦 Project Structure

```
chatapp/
├── main.py              # FastAPI application
├── static/
│   └── index.html       # Frontend
├── chat.db              # SQLite database (auto-created)
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md            # This file
```

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jaina121/ChattVibeCoding.git
   cd chatapp
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Open in browser**
   ```
   http://localhost:8000
   ```

### Authentication Notes

- The login form accepts a single `username`. If the username exists, the server returns the user and the client logs in. If the username does not exist, the client automatically registers the username and logs in.
- Sessions are stored locally in `localStorage` under the key `chatappUser`. To fully logout, click the **Logout** button in the sidebar — this closes the WebSocket connection and clears the local session.

### Using Docker

1. **Build the image**
   ```bash
   docker build -t chatapp .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 chatapp
   ```

## 🌐 API Endpoints

### User Management
- `POST /api/users/register` - Register a new user
- `GET /api/users` - Get all users (supports ?search=query)
- `POST /api/users/login` - Login existing user (returns 401 if not found)

### Messaging
- `POST /api/messages` - Send a message
- `GET /api/messages` - Get all messages (supports ?search=query)
- `WebSocket /ws/{user_id}` - Real-time message streaming

### Frontend
- `GET /` - Serve main HTML page

## 🌍 Live Demo

**Live Website:** [UPDATE_THIS_WITH_YOUR_RENDER_URL](https://render.com)

> Get your Render URL from the [QUICKSTART.md](QUICKSTART.md) - Step 4

## 📹 Demo Video

Watch the full demo: [YouTube Demo Video](https://youtu.be/-YMsUIBJCzU?si=FInptYDWa7PwcPs_)

Features shown:
- User registration and login
- Searching and selecting users
- Real-time message sending/receiving
- Message history
- API endpoints in action
- Deployed live application

## 📸 Screenshots

### Chat Interface
![Chat Window](screenshot1.png)

### User List
![User List](screenshot2.png)

## 🔧 Configuration

No configuration needed! The app works out of the box. The SQLite database is created automatically on first run.

## 🐛 Troubleshooting

**Port already in use:**
```bash
python main.py --port 8001
```

**Database issues:**
Simply delete `chat.db` and restart - it will be recreated

## 📝 API Examples

### Register User
```bash
curl -X POST http://localhost:8000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"username": "alice"}'
```

### Get All Users
```bash
curl http://localhost:8000/api/users
```

### Send Message
```bash
curl -X POST "http://localhost:8000/api/messages?sender_id=1" \
  -H "Content-Type: application/json" \
  -d '{"content": "Hello!", "receiver_id": 2}'
```

### Search Messages
```bash
curl "http://localhost:8000/api/messages?search=hello"
```

## 📋 Requirements

See `requirements.txt`:
- fastapi==0.104.1
- uvicorn==0.24.0
- python-multipart==0.0.6
- pydantic==2.5.0
- aiosqlite==0.19.0

## 🚢 Deployment

### Deploy to Render

1. Push to GitHub
2. Go to [render.com]( https://render.com/docs/web-services#port-binding)
3. Create new Web Service
4. Connect your GitHub repository
5. Set Build command: `pip install -r requirements.txt`
6. Set Start command: `uvicorn main:app --host 0.0.0.0 --port 8000`
7. Deploy!


## 👨‍💻 Author

Built for Vibe Coding Final Project Joodonbek kyzy Jainagyl

---

**Made with ❤️ using FastAPI and vanilla JavaScript**
