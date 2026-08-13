# 🤖 RCPS 420: Robotics & Embedded Systems Exam Portal

An interactive web application and revision tool built with **Streamlit** for practicing solved exam questions, taking mock exams, and downloading offline revision PDFs.

## 🚀 Live Streamlit Cloud Deployment Guide

Follow these simple steps to host this app on **Streamlit Community Cloud** (100% Free):

### Step 1: Create a GitHub Repository
1. Go to [GitHub.com](https://github.com) and create a **New Public Repository** named `robotics-embedded-exam-prep`.
2. Do NOT initialize with a README (we already created one).

### Step 2: Push Your Local Code to GitHub
Run the following commands in your terminal inside this folder:

```bash
git init
git add .
git commit -m "Initial commit for Streamlit Cloud deployment"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/robotics-embedded-exam-prep.git
git push -u origin main
```

*(Replace `YOUR_GITHUB_USERNAME` with your actual GitHub account name).*

---

### Step 3: Deploy on Streamlit Community Cloud
1. Sign in to [share.streamlit.io](https://share.streamlit.io/) with your GitHub account.
2. Click **"New App"** in the top right.
3. Fill in the details:
   - **Repository:** `YOUR_GITHUB_USERNAME/robotics-embedded-exam-prep`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **"Deploy!"** 🚀

Within 1-2 minutes, your live link (e.g. `https://robotics-embedded-exam-prep.streamlit.app`) will be ready to share with all your classmates!

---

## 🛠️ Local Setup
To run the app locally on your machine:

```bash
pip install -r requirements.txt
streamlit run app.py
```
