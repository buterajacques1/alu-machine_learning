#!/usr/bin/env python3
"""
Script to display the upcoming SpaceX launch information
"""
import requests

def fetch_upcoming_launch():
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    launches = response.json()
    # Sort launches by unix date, and take the soonest
    next_launch = sorted(launches, key=lambda x: x['date_unix'])[0]

    # Fetch rocket name
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{next_launch['rocket']}"
    rocket_name = requests.get(rocket_url).json()['name']

    # Fetch launchpad details
    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{next_launch['launchpad']}"
    launchpad = requests.get(launchpad_url).json()
    launchpad_name = f"{launchpad['name']} ({launchpad['locality']})"

    # Prepare and print the formatted launch information
    launch_info = f"{next_launch['name']} ({next_launch['date_local']}) {rocket_name} - {launchpad_name}"
    print(launch_info)

if __name__ == '__main__':
    fetch_upcoming_launch()
