# 🌍 AI Travel Planner Web App

## 🚀 Overview

The **AI Travel Planner** is a smart web application that helps users plan trips by generating **personalized itineraries, budget estimates, and recommendations** based on their preferences.

The app integrates **real-world travel APIs, image services, and intelligent recommendation logic** to deliver a rich travel planning experience.

---

## ✨ Features

* 📍 **Dynamic Destination Search**

  * Add any city dynamically
  * Fetch real tourist attractions using API

* 🖼️ **Image-Rich UI**

  * Each destination includes high-quality images
  * Clean card-based layout

* 📅 **Smart Itinerary Generator**

  * Day-wise planning
  * Real places instead of dummy data

* 💰 **Budget Estimation**

  * Cost breakdown (Low / Medium / Luxury)
  * Visualized using charts

* 🎯 **Personalized Recommendations**

  * Based on interests (Adventure, Food, Nature, History)
  * Budget-aware suggestions

* ⚡ **API Optimization**

  * Local JSON caching system
  * Avoids repeated API calls (rate-limit safe)

---

## 🧠 Tech Stack

* **Frontend:** Streamlit

* **Backend:** Python

* **APIs Used:**

  * Travel Advisor API (RapidAPI)
  * Unsplash API (Images)

* **Libraries:**

  * pandas
  * matplotlib
  * requests
  * scikit-learn (for ML extension)

---

## 🏗️ Project Structure

```
TravelPlannerApp/
│
├── app.py                  # Main Streamlit app
├── requirements.txt
│
├── data/
│   ├── fetch_data.py       # API + data generation
│   └── destinations.json   # Cached data
│
├── modules/
│   ├── itinerary.py
│   ├── budget.py
│   └── recomendations.py
│
├── utils/
│   ├── helpers.py
│   └── constants.py
│
└── pages/                  # Multi-page UI
```

---

## ⚙️ How It Works

```
User Input → Fetch API → Cache JSON → Generate Itinerary → Show UI
```

* Cities are fetched only once
* Stored in `destinations.json`
* Reused to reduce API calls

---

## 🧪 Machine Learning Extension

This project includes the foundation for:

* ✅ Interest-based city recommendation
* ✅ Content-based similarity model (Cosine Similarity)
* ✅ Future upgrade to full recommendation engine

---

## 📦 Installation (Local Setup)

```bash
git clone https://github.com/YOUR_USERNAME/travelandtourismwebapp.git
cd travelandtourismwebapp

pip install -r requirements.txt
streamlit run app.py
```

---

## 🔑 API Setup

Create a `.env` or use Streamlit secrets:

```
RAPIDAPI_KEY=your_key
UNSPLASH_KEY=your_key
```

---

## 🌐 Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Select repo
4. Add secrets
5. Deploy 🚀

---


---

## 🧠 SOP (Statement of Purpose)

This project was built to demonstrate the integration of:

* Real-world APIs
* Data processing pipelines
* UI/UX design using Streamlit
* Recommendation systems

The main goal was to create a **scalable and intelligent travel planning system** that mimics real-world platforms like MakeMyTrip or TripAdvisor.

Key learning outcomes:

* API handling and optimization
* Data caching strategies
* Modular code architecture
* Building user-centric UI
* Applying ML concepts in real applications

This project reflects my ability to combine **software engineering + data science + user experience design** into a practical solution.

---

## 🚀 Future Improvements

* 🤖 AI chatbot for travel planning
* 🗺️ Map integration (Google Maps API)
* 📅 Smart itinerary optimization (distance-based)
* 👤 User login & saved trips
* 📊 Advanced ML recommendation system

---

## 👨‍💻 Author

**Mahesh Kolekar**

---

## ⭐ Show Your Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it

---
﻿# travelandtourismwebapp
