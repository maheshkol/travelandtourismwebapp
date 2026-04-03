# data/fetch_data.py
import requests
import json
import os
import time


API_KEY = "3b629954c1mshfced3d70f4496a4p16ba2ejsn4981d071983a"   # 🔴 paste your key here
API_HOST = "travel-advisor.p.rapidapi.com"

# ✅ STEP 1: Get location_id from city
def get_location_id(city):
    url = "https://travel-advisor.p.rapidapi.com/locations/search"

    querystring = {
        "query": city,
        "limit": "1",
        "lang": "en_US"
    }

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        print(f"❌ Failed to get location_id for {city}")
        return None

    data = response.json()

    try:
        return data["data"][0]["result_object"]["location_id"]
    except:
        print(f"⚠️ No location_id found for {city}")
        return None


# ✅ STEP 2: Fetch real tourist attractions
def fetch_places(city):
    location_id = get_location_id(city)

    if not location_id:
        return []
    
    url = "https://travel-advisor.p.rapidapi.com/attractions/list"

    querystring = {
        "location_id": location_id,
        "lang": "en_US",
        "currency": "USD"
    }

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(f"\n📍 {city}")
    print("STATUS:", response.status_code)

    if response.status_code != 200:
        print("❌ Error:", response.text)
        return []

    data = response.json()

    places = []

    for item in data.get("data", []):
        name = item.get("name")
        rating = item.get("rating")

        # ✅ Filter good quality attractions only
        if name and rating:
            image_url = fetch_image(f"{name} {city} landmark")

            places.append({
                "name": name,
                "image": image_url
            })

    return places[:5] if places else []

def fetch_image(query):
    url = "https://api.unsplash.com/search/photos"

    headers = {
        "Authorization": "Client-ID HnCZMt8AVPhc6GEPrZ3zIuGsVUUrKEi3Xp5VaSzLUoo"
    }

    params = {
        "query": query,
        "per_page": 1,
        "orientation": "landscape"
    }

    response = requests.get(url, headers=headers, params=params)

    print(f"🖼️ Image search for: {query}")
    print("Image API STATUS:", response.status_code)

    if response.status_code != 200:
        return "https://via.placeholder.com/400x300?text=No+Image"

    try:
        data = response.json()

        results = data.get("results")

        if not results:
            return "https://via.placeholder.com/400x300?text=No+Image"

        return results[0]["urls"]["regular"]

    except:
        return "https://via.placeholder.com/400x300?text=No+Image"

# ✅ MAIN FUNCTION (UNCHANGED LOGIC - GOOD)
def generate_data(cities):
    file_path = "data/destinations.json"

    # ✅ LOAD existing data
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
    else:
        final_data = {}

    for city in cities:
        city = city.strip().title()

        if not city:
            continue

    # ✅ Only skip if images already exist
        if city in final_data and all(
        isinstance(p, dict) and p.get("image") for p in final_data[city]["places"]
    ):
            print(f"⏩ Skipping {city} (already has images)")
            continue

        print(f"🌐 Fetching / Updating {city}...")

        places = fetch_places(city)

        if not places:
            print(f"⚠️ No data for {city}")
            continue

        final_data[city] = {
            "places": places,
            "activities": ["Exploring", "Photography", "Local Experience"],
            "hotel_cost": {
                "Low": 1200,
                "Medium": 3000,
                "Luxury": 7000
            }
        }
        time.sleep(1)

    # ✅ SAVE updated data
    os.makedirs("data", exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=4)

    print("✅ JSON updated!")


if __name__ == "__main__":
    user_input = input("Enter cities (comma separated): ")
    cities = user_input.split(",")

    generate_data(cities)