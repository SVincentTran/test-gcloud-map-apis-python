# Google cloud functions imports
from flask import escape
import functions_framework
import googlemaps
import json

gmaps = googlemaps.Client(key="AIzaSyB9JWWSImc9xmKCdIuYILsujwoNOa4HAhY")

@functions_framework.http
def search_directions(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'origin' in request_json:
        origin = request_json['origin']
    elif request_args and 'origin' in request_args:
        origin = request_args['origin']
    else:
        return False
    print(origin)

    if request_json and 'destination' in request_json:
        destination = request_json['destination']
    elif request_args and 'destination' in request_args:
        destination = request_args['destination']
    else:
        return False
    print(destination)

    directions = gmaps.directions(origin, destination)

    print(directions)

    return directions
    # return f"Hello {origin} to {destination}"