import os
import requests
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

MAPBOX_URL = "https://api.mapbox.com/search/geocode/v6/forward"
MBTA_STOPS_URL = "https://api-v3.mbta.com/stops"


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
    """
    Takes latitude/longitude and returns nearest MBTA stop info.
    """
    headers = {}
    if MBTA_API_KEY:
        headers["x-api-key"] = MBTA_API_KEY

    params = {
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "filter[radius]": 0.01,
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

    name = attributes["name"]
    wheelchair_boarding = attributes.get("wheelchair_boarding")

    wheelchair_accessible = wheelchair_boarding == 1

    return name, wheelchair_accessible


def find_stop_near(place_name):
    """
    Full pipeline:
    place name -> Mapbox lat/lng -> nearest MBTA stop
    """
    latitude, longitude = geocode_place(place_name)
    stop_name, wheelchair_accessible = find_nearest_stop(latitude, longitude)

    return stop_name, wheelchair_accessible


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