# 🎯 The Pitch Visualizer – From Words to Storyboard

The Pitch Visualizer is a web-based AI tool that converts narrative text into a multi-panel visual storyboard.  

It automatically:
- Breaks a story into key scenes
- Enhances each scene into a visual prompt
- Generates AI images for every scene
- Displays them as a coherent storyboard

This helps sales teams, marketers, and presenters quickly turn customer stories into engaging visual pitch content.

---

## 🚀 Features

✅ Accepts narrative text input  
✅ Automatically segments story into scenes  
✅ Intelligent prompt engineering for better visuals  
✅ AI-based image generation (API)  
✅ Displays storyboard in sequence  
✅ Simple and interactive web interface  

---

## 🧠 How It Works

1. User enters a short story (3–5 sentences)
2. Text is split into logical scenes
3. Each scene is enhanced into a visual description
4. AI generates an image for every scene
5. Images are shown as a storyboard

---

## 🛠️ Tech Stack

- Python  
- Flask (web framework)  
- AI Image Generation API  
- HTML + Jinja Templates  

---

## 📂 Project Structure

pitch-visualizer/
│
├── app.py
├── requirements.txt
│
├── services/
│ ├── text_segmentation.py
│ ├── prompt_engineering.py
│ └── image_generator.py
│
└── templates/
├── index.html
└── storyboard.html


---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download Project

Place project folder on your computer.

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
