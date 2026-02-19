# 🛡️ SafeHer – Women Safety Platform

A complete, production-level civic-tech web application for women's safety.

---

## ✅ STEPS TO RUN (Easy — 3 Steps Only!)

### Step 1 – Install Python
Make sure Python is installed. Check by running:
```
python --version
```
If not installed → Download from https://python.org (version 3.8+)

---

### Step 2 – Install Flask (one command)
Open your terminal / command prompt in this folder and run:
```
pip install flask
```

---

### Step 3 – Run the App
```
python app.py
```

Then open your browser and go to:
```
http://localhost:5000
```

That's it! 🎉

---

## 📁 File Structure

```
women-safety-platform/
│
├── app.py                  ← Main Flask backend (all API routes)
├── requirements.txt        ← Python dependencies (just flask)
│
├── templates/
│   ├── base.html           ← Navbar, SOS button, footer (shared layout)
│   ├── home.html           ← Home page with hero, stats, features
│   ├── dashboard.html      ← User dashboard with contacts, location sharing
│   ├── map.html            ← Interactive safety map (Leaflet.js)
│   ├── report.html         ← Incident reporting form
│   ├── chatbot.html        ← AI safety assistant chatbot
│   └── education.html      ← Safety education: self defense, legal rights
│
└── static/
    ├── css/style.css       ← All styling (dark theme, responsive)
    └── js/main.js          ← SOS system, geolocation, shake detection, login
```

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🚨 SOS Alert | 5-second countdown SOS with GPS location capture |
| 📞 Fake Call | Trigger fake incoming call to escape situations |
| 🗺️ Safety Map | Interactive Leaflet map with police, hospital markers |
| 🤖 AI Chatbot | Rule-based safety assistant (no API key needed!) |
| 📊 Incident Report | Community safety reporting with categories |
| 👨‍👩‍👧 Guardian Mode | Generate shareable location links |
| 📚 Education | Self defense, legal rights, cyber safety tabs |
| 📱 Shake Detection | Shake phone to trigger SOS (mobile) |

---

## 🔧 No Extra Configuration Needed!

- ✅ No database setup — uses in-memory storage
- ✅ No API keys — AI chatbot is rule-based
- ✅ No login required — enter any name to start
- ✅ Map uses free OpenStreetMap — no Google API key

---

## 📞 Emergency Numbers Integrated

| Number | Service |
|---|---|
| 100 | Police |
| 112 | National Emergency |
| 1091 | Women's Helpline |
| 108 | Ambulance |
| 1930 | Cyber Crime |
| 1098 | Childline |

---

## 💼 Resume Description

**AI-Enabled Women Safety Civic Platform**  
• Built full-stack mobile-responsive safety web platform using Flask, JavaScript, and Bootstrap 5  
• Integrated real-time GPS tracking, SOS alert system, shake detection, and fake call feature  
• Developed AI safety chatbot with self-defense guidance, legal rights info, and emergency helplines  
• Designed community incident reporting with interactive safety map using Leaflet.js + OpenStreetMap  
• Implemented guardian tracking mode with shareable live location links
