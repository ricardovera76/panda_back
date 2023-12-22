import requests
url = "https://maps.googleapis.com/maps/api/directions/json?destination=Perth%2C%20AU&origin=Sydney%2C%20AU&waypoints=via%3Aenc%3AlexeF%7B~wsZejrPjtye%40%3A&key=AIzaSyCnvG6URTsIU2pRFEqOfW_JEffkWz4cp5o"

def calculate_route():
    data = requests.get(url)
    print(data)