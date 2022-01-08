# Google map imports
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyB9JWWSImc9xmKCdIuYILsujwoNOa4HAhY")

# Test get origin places
origin = gmaps.find_place("Big C Ha Noi", "textquery")
origin_id = origin["candidates"][0]["place_id"]

# Test get destination places
destination = gmaps.find_place("Vincom Nguyen Chi Thanh", "textquery")
destination_id = destination["candidates"][0]["place_id"]

# Test get directions
directions = gmaps.directions("Big C Ha Noi", "Vincom Nguyen Chi Thanh")

print(origin)
print(destination)
print(directions)