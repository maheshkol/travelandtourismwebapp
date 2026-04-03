# pages/1_Home.py

import streamlit as st

st.set_page_config(page_title="Travel Planner", page_icon="🌍")

# 🌍 Title
st.title("🌍 AI Travel Planner App")

# Subtitle
st.markdown("""
Plan your trips smarter with personalized itineraries, budget estimates, and recommendations.
""")

st.write("---")

# ✨ Features Section
st.header("✨ Features")

st.markdown("""
- 📅 Customized Day-wise Itinerary  
- 💰 Budget Estimation (Low / Medium / Luxury)  
- 🎯 Interest-based Recommendations  
- 🌍 Multiple Destinations  
- ⚡ Fast & Simple Planning  
""")

st.write("---")

# 🧭 How it works
st.header("🧭 How It Works")

st.markdown("""
1. Select your destination  
2. Choose number of days  
3. Pick your budget  
4. Add your interests  
5. Get your personalized travel plan instantly  
""")

st.write("---")

# 🚀 Call to Action
st.header("🚀 Get Started")

st.info("👉 Go to **Plan Trip** page from the sidebar to create your itinerary.")

st.write("---")

# 👨‍💻 Footer
st.markdown("""
---
Made with ❤️ using Streamlit  
""")