import streamlit as st
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

from utils.helpers import load_data, format_currency, validate_inputs
from utils.constants import BUDGET_TYPES, INTERESTS, DATA_PATH, APP_TITLE, APP_SUBTITLE
from modules.itinerary import generate_detailed_itinerary
from modules.budget import calculate_budget, get_budget_breakdown
from modules.recomendations import get_recommendations
from data.fetch_data import generate_data

# 🌍 Page Config
st.set_page_config(page_title="Travel Planner", page_icon="🌍", layout="wide")

# 🎨 Global Styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.card {
    border-radius: 15px;
    padding: 12px;
    background: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# 🎨 Header
st.title(APP_TITLE)
st.markdown(APP_SUBTITLE)
st.write("---")

# ➕ Add City Section
st.markdown("## ➕ Add New City")

cities_input = st.text_input("Enter cities (comma separated)")

if not os.path.exists(DATA_PATH):
    with open(DATA_PATH, "w") as f:
        json.dump({}, f)

data = load_data(DATA_PATH)

col_add, col_reset = st.columns(2)

with col_add:
    if st.button("Add City Data"):
        if cities_input:
            cities = cities_input.split(",")
            generate_data(cities)
            data = load_data(DATA_PATH)
            st.success("✅ New city data added!")

with col_reset:
    if st.button("🔄 Reset Database"):
        if os.path.exists(DATA_PATH):
            os.remove(DATA_PATH)
            st.warning("Database cleared!")

st.write("---")

# 🧾 Input Section
st.markdown("## ✈️ Plan Your Trip")

if not data:
    st.warning("⚠️ No cities available. Add a city first.")
    st.stop()

col1, col2, col3 = st.columns(3)

with col1:
    destination = st.selectbox("📍 Destination", list(data.keys()))

with col2:
    days = st.slider("📅 Days", 1, 10)

with col3:
    budget = st.selectbox("💰 Budget", BUDGET_TYPES)

interests = st.multiselect("🎯 Interests", INTERESTS)

st.write("---")

# 📍 Show Places
st.markdown("## 📍 Top Places")

places = data[destination]["places"]
cols = st.columns(2)

for i, place in enumerate(places):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="card">
            <img src="{place['image']}" style="width:100%; border-radius:10px;">
            <h4>{place['name']}</h4>
        </div>
        """, unsafe_allow_html=True)

# 🚀 Generate Plan
if st.button("🚀 Generate Travel Plan"):
    with st.spinner("Generating your travel plan..."):
        try:
            validate_inputs(destination, days, budget, data)

            # 📅 Itinerary
            itinerary = generate_detailed_itinerary(destination, days, data)

            st.markdown("## 📅 Your Itinerary")

            for day in itinerary:
                st.markdown(f"""
                <div class="card">
                    <h4>Day {day['day']}</h4>
                    <p><b>🌅 Morning:</b> Visit {day['place_name']}</p>
                    <p><b>🌞 Afternoon:</b> {day['afternoon']}</p>
                    <p><b>🌙 Evening:</b> {day['evening']}</p>
                </div>
                """, unsafe_allow_html=True)

                if day.get("image"):
                    st.image(day["image"], use_container_width=True)

            # 💰 Budget
            total_cost = calculate_budget(destination, days, budget, data)
            breakdown = get_budget_breakdown(destination, days, budget, data)

            st.markdown("## 💰 Budget Summary")

            col1, col2 = st.columns(2)

            with col1:
                st.success(f"Total Cost: {format_currency(total_cost)}")

            with col2:
                for key, value in breakdown.items():
                    st.write(f"{key}: {format_currency(value)}")

            # 📊 Chart
            df = pd.DataFrame(list(breakdown.items()), columns=["Category", "Cost"])

            fig, ax = plt.subplots()
            ax.pie(df["Cost"], labels=df["Category"], autopct='%1.1f%%')

            st.pyplot(fig)

            # 🎯 Recommendations
            recs = get_recommendations(destination, interests, budget, data)

            st.markdown("## 🎯 Recommendations")

            for r in recs:
                st.markdown(f"<div class='card'>👉 {r}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(str(e))
