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

    if request_json and "origin" in request_json:
        origin = request_json["origin"]
    elif request_args and "origin" in request_args:
        origin = request_args["origin"]
    else:
        return False
    print(origin)

    if request_json and "destination" in request_json:
        destination = request_json["destination"]
    elif request_args and "destination" in request_args:
        destination = request_args["destination"]
    else:
        return False
    print(destination)

    directions = gmaps.directions(origin, destination)

    str_direction = json.dumps(directions)

    return str_direction
    # return f"Hello {origin} to {destination}"

@functions_framework.http
def geocoding(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "name" in request_json:
        name = request_json["name"]
    elif request_args and "name" in request_args:
        name = request_args["name"]
    else:
        return False
    
    print(name)

    geocode = gmaps.geocode(name)

    str_geocode = json.dumps(json)

    return str_geocode