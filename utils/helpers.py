# utils/helpers.py

import json
import os


def load_data(filepath):
    """
    Load JSON data from a file
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception(f"❌ File not found: {filepath}")
    except json.JSONDecodeError:
        raise Exception("❌ Error decoding JSON file")


def save_json(filepath, data):
    """
    Save data to a JSON file
    """
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        raise Exception(f"❌ Error saving JSON: {e}")


def format_currency(amount):
    """
    Format number into Indian currency format
    Example: 12500 -> ₹ 12,500
    """
    return f"₹ {amount:,.0f}"


def validate_inputs(destination, days, budget, data):
    """
    Validate user inputs before processing
    """
    if destination not in data:
        raise ValueError("Invalid destination selected")

    if days <= 0:
        raise ValueError("Days must be greater than 0")

    if budget not in ["Low", "Medium", "Luxury"]:
        raise ValueError("Invalid budget type")

    return True


def safe_get(data, key, default=None):
    """
    Safely get value from dictionary
    """
    return data[key] if key in data else default


def format_itinerary_text(itinerary):
    """
    Convert itinerary into readable text format
    (Useful for downloads / PDF later)
    """
    output = ""

    for day in itinerary:
        output += f"Day {day['day']}:\n"

        if "morning" in day:
            output += f"  🌅 Morning: {day['morning']}\n"
            output += f"  🌞 Afternoon: {day['afternoon']}\n"
            output += f"  🌙 Evening: {day['evening']}\n"
        else:
            output += f"  📍 Place: {day['place']}\n"
            output += f"  🎯 Activity: {day['activity']}\n"

        output += "\n"

    return output