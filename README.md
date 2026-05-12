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
- **Deployment:** Docker, Cloud platforms (Render, Railway, etc.)

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
   git clone https://github.com/yourusername/chatapp.git
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

Watch the full demo: [YouTube Demo Video](https://UPDATE_WITH_YOUR_YOUTUBE_LINK)

> For recording instructions, see [DEMO_VIDEO_GUIDE.md](DEMO_VIDEO_GUIDE.md)

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
2. Go to [render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Set Build command: `pip install -r requirements.txt`
6. Set Start command: `uvicorn main:app --host 0.0.0.0 --port 8000`
7. Deploy!

### Deploy to Railway

1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. Create new Project
4. Connect GitHub repository
5. Railway auto-detects and deploys
6. Get live URL

### Deploy to PythonAnywhere

1. Upload files
2. Create new web app
3. Configure WSGI settings
4. Run `pip install -r requirements.txt`
5. Set startup commands

## 🤝 Contributing

Feel free to fork, modify, and improve!

## 📄 License

MIT License - feel free to use this project

## 👨‍💻 Author

Built for Vibe Coding Final Project

---

**Made with ❤️ using FastAPI and vanilla JavaScript**
