# modules/itinerary.py

def generate_itinerary(destination, days, data):
    """
    Generate a day-wise itinerary based on destination and number of days
    """

    places = data[destination]["places"]
    activities = data[destination]["activities"]

    itinerary = []

    for i in range(days):
        day_plan = {
            "day": i + 1,
            "place": places[i % len(places)],
            "activity": activities[i % len(activities)]
        }
        itinerary.append(day_plan)

    return itinerary


def generate_detailed_itinerary(destination, days, data):
    places = data[destination]["places"]
    activities = data[destination]["activities"]

    itinerary = []

    for i in range(days):
        place = places[i % len(places)]  # ✅ get dict

        day_plan = {
            "day": i + 1,
            "place_name": place["name"],     # ✅ extract name
            "image": place["image"],         # ✅ store image
            "afternoon": f"Enjoy {activities[i % len(activities)]}",
            "evening": "Explore local markets & relax"
        }

        itinerary.append(day_plan)

    return itinerary


def format_itinerary(itinerary):
    """
    Convert itinerary into readable text format (useful for export/PDF)
    """

    formatted = ""

    for day in itinerary:
        formatted += f"Day {day['day']}:\n"
        
        if "morning" in day:
            formatted += f"  🌅 Morning: {day['morning']}\n"
            formatted += f"  🌞 Afternoon: {day['afternoon']}\n"
            formatted += f"  🌙 Evening: {day['evening']}\n"
        else:
            formatted += f"  📍 Place: {day['place']}\n"
            formatted += f"  🎯 Activity: {day['activity']}\n"
        
        formatted += "\n"

    return formatted