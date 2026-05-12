# ⚡ QUICKSTART - Get to Submission in 30 Minutes!

**Deadline: 5:00 PM** ⏰

Follow these steps in order. Each section takes ~5-10 minutes.

---

## 🚀 STEP 1: Test Locally (5 min)

Your server is already running! Just verify it's working:

### Run the test script:
```bash
python test_api.py
```

You should see all tests passing with ✅.

**If the server crashed**, restart it:
```bash
python main.py
```

---

## 📤 STEP 2: Create GitHub Repository (5 min)

1. Go to [github.com](https://github.com)
2. Click the **"+"** icon → **"New repository"**
3. Name: `chatapp`
4. Description: `Real-time chat app with FastAPI and WebSockets`
5. Set to **Public** ✓
6. Click **"Create repository"**

---

## 📬 STEP 3: Push Code to GitHub (3 min)

After creating your GitHub repository, you'll see a page with commands.

Run these commands in your chatapp folder:

```bash
git remote add origin https://github.com/YOUR_USERNAME/chatapp.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME`** with your actual GitHub username.

---

## 🌐 STEP 4: Deploy to Render (5 min)

### Simple 3-step deployment:

1. Go to [render.com](https://render.com) and create free account
2. Click **"New +"** → **"Web Service"**
3. Select **"GitHub"** and connect your `chatapp` repository
4. Fill in settings:
   - **Name:** `chatapp`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 8080`
   - **Plan:** Free
5. Click **"Deploy Web Service"**

**Wait 2-3 minutes** for it to deploy. You'll get a URL like:
```
https://chatapp-abc123.onrender.com
```

**Save this URL!** It's your live website.

---

## 🎬 STEP 5: Record Demo Video (5 min)

### Super quick 2-minute video:

1. **Test the live site** at your Render URL (or localhost if using local)
2. **Record your screen** using:
   - OBS (free)
   - Windows 11 built-in recorder
   - Phone screen recording
3. **Show this:**
   - Register 2 users
            - Demonstrate login + logout (show session persistence):
               - Log in as user A, send a message
               - Refresh the page to show session restore
               - Logout and log in as user B to show account switching
   - Send a message from one to another
   - Show message appearing on both screens
   - Say what the app does
4. **Upload to YouTube** (unlisted or public)
5. **Get the YouTube link**

See [DEMO_VIDEO_GUIDE.md](DEMO_VIDEO_GUIDE.md) for detailed instructions.

---

## 📝 STEP 6: Final README Check (2 min)

Your README.md already has everything, just update these lines:

1. Find this line in README.md:
   ```
   **Live Website:** [https://chatapp-demo.onrender.com](https://chatapp-demo.onrender.com)
   ```
   Replace with your actual Render URL.

2. Find this line:
   ```
   Watch the full demo: [YouTube Demo Video](https://youtu.be/your-demo-video-link)
   ```
   Replace with your actual YouTube link.

3. Commit these changes:
   ```bash
   git add README.md
   git commit -m "Update live URL and demo video link"
   git push origin main
   ```

---

## 📧 STEP 7: FINAL SUBMISSION (1 min)

Send email to: **kyrgyzstanait@gmail.com**

**Subject:** `Vibe Coding Final Project – YOUR FULL NAME`

**Body:**
```
Hi,

Here's my ChatApp project:

🔗 GitHub: https://github.com/YOUR_USERNAME/chatapp
🌐 Live Website: https://chatapp-abc123.onrender.com
📹 Demo Video: https://youtu.be/XXXXXXXXXX

Features:
✅ User registration and search
✅ Real-time messaging
✅ Message history
✅ Beautiful responsive UI
✅ FastAPI backend with WebSockets
✅ Deployed on Render

Thank you!
```

---

## ✅ Checklist Before Submission

- [ ] Server tested locally with `test_api.py`
- [ ] Code pushed to GitHub repository
- [ ] Website deployed on Render (or another platform)
- [ ] Demo video recorded and uploaded to YouTube
- [ ] README.md has correct URLs
- [ ] Email sent to kyrgyzstanait@gmail.com before 5:00 PM

---

## 🆘 Troubleshooting

**"Server won't start"**
```bash
python main.py
```
If error, make sure all packages are installed:
```bash
pip install -r requirements.txt
```

**"Can't connect to GitHub"**
- Use HTTPS URL, not SSH
- Make sure your git is configured: 
  ```bash
  git config user.name "Your Name"
  git config user.email "your@email.com"
  ```

**"Render deployment failed"**
- Check the build logs on Render dashboard
- Make sure you selected Python 3 environment
- Verify `requirements.txt` has `websockets==12.0`

**"WebSocket not working"**
- Make sure you're using your deployed URL (https://...)
- Local testing might need manual WebSocket port
- Render auto-enables WebSocket support

**"Demo video upload taking forever"**
- Make sure your internet is stable
- Try uploading unlisted first to save time

---

## 🎉 You're Done!

After these 7 steps, you're ready to submit!

**Total time:** ~30-40 minutes ⏰

**Key files created:**
- `main.py` - Full FastAPI backend
- `static/index.html` - Beautiful frontend
- `README.md` - Project documentation
- `DEPLOYMENT.md` - Detailed deployment guide
- `DEMO_VIDEO_GUIDE.md` - Video recording tips
- `test_api.py` - API test script

---

**Questions?** Check the other guide files:
- 📘 [README.md](README.md) - Full project info
- 🚀 [DEPLOYMENT.md](DEPLOYMENT.md) - Detailed deployment steps
- 🎬 [DEMO_VIDEO_GUIDE.md](DEMO_VIDEO_GUIDE.md) - Video recording tips

Good luck! 🚀✨
