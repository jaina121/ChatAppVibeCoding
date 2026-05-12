# 🚀 Deployment Guide for ChatApp

## Step 1: Create GitHub Account & Repository

1. Go to [github.com](https://github.com) and create an account if you don't have one
2. Click "+" → "New repository"
3. Name it: `chatapp`
4. Set to **Public**
5. Click "Create repository"

## Step 2: Push Code to GitHub

In your project folder, run these commands:

```bash
git remote add origin https://github.com/jaina121/ChattVibeCoding.git
git branch -M main
git push -u origin main
```


## Step 3: Deploy to Render (Free!)

### Option A: Deploy from GitHub (Recommended)

1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Select "Connect a repository" → select your `chatapp` repository
4. Set these settings:
   - **Name:** chatapp
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 8080`
   - **Plan:** Free
5. Click "Deploy Web Service"
6. Wait 2-3 minutes for deployment

### Option B: Docker Deployment (Even Faster!)

```bash
cd chatapp
docker build -t chatapp .
docker run -p 8000:8000 chatapp
```

## Step 4: Get Your Live URL

After deployment, Render will give you a URL like:
```
https://chatapp-xxxxx.onrender.com
```


