import os
import requests
from dotenv import load_dotenv
from math import radians, sin, cos, sqrt, atan2

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

MAPBOX_URL = "https://api.mapbox.com/search/geocode/v6/forward"
MBTA_STOPS_URL = "https://api-v3.mbta.com/stops"

def calculate_distance_miles(lat1, lon1, lat2, lon2):
    earth_radius_miles = 3958.8

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius_miles * c

def geocode_place(place_name):
    """
    Takes a place name/address and returns (latitude, longitude).
    Example: geocode_place("Boston Common") -> (42.355, -71.065)
    """
    if not MAPBOX_TOKEN:
        raise ValueError("Missing MAPBOX_TOKEN in .env file")

    params = {
        "q": place_name,
        "access_token": MAPBOX_TOKEN,
        "limit": 1,
        "country": "us",
        "proximity": "-71.0589,42.3601",  # bias toward Boston
    }

    response = requests.get(MAPBOX_URL, params=params)
    response.raise_for_status()

    data = response.json()
    features = data.get("features", [])

    if not features:
        raise ValueError(f"No location found for: {place_name}")

    coordinates = features[0]["geometry"]["coordinates"]
    longitude = coordinates[0]
    latitude = coordinates[1]

    return latitude, longitude


def find_nearest_stop(latitude, longitude):
    headers = {}

    if MBTA_API_KEY:
        headers["x-api-key"] = MBTA_API_KEY

    params = {
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "filter[radius]": 0.03,
        "sort": "distance",
        "page[limit]": 1,
    }

    response = requests.get(MBTA_STOPS_URL, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    stops = data.get("data", [])

    if not stops:
        raise ValueError("No MBTA stops found nearby")

    stop = stops[0]
    attributes = stop["attributes"]

    return {
        "name": attributes["name"],
        "wheelchair_accessible": attributes.get("wheelchair_boarding") == 1,
        "latitude": attributes["latitude"],
        "longitude": attributes["longitude"],
    }


def find_stop_near(place_name):
    place_latitude, place_longitude = geocode_place(place_name)
    stop = find_nearest_stop(place_latitude, place_longitude)

    distance_miles = calculate_distance_miles(
        place_latitude,
        place_longitude,
        stop["latitude"],
        stop["longitude"]
    )

    walking_minutes = round(distance_miles / 3 * 60)

    return {
        "place_name": place_name,
        "place_latitude": place_latitude,
        "place_longitude": place_longitude,
        "stop_name": stop["name"],
        "wheelchair_accessible": stop["wheelchair_accessible"],
        "stop_latitude": stop["latitude"],
        "stop_longitude": stop["longitude"],
        "distance_miles": round(distance_miles, 2),
        "walking_minutes": walking_minutes,
    }

def main():
    test_places = [
        "Boston Common",
        "Fenway Park",
        "Copley Square Boston",
    ]

    for place in test_places:
        try:
            stop_name, accessible = find_stop_near(place)
            accessible_text = "Yes" if accessible else "No"

            print(f"\nPlace: {place}")
            print(f"Nearest stop: {stop_name}")
            print(f"Wheelchair accessible: {accessible_text}")

        except Exception as error:
            print(f"\nCould not process {place}: {error}")


if __name__ == "__main__":
    main()