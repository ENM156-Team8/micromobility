import traceback
from flask import Flask, render_template, request, url_for, redirect, session
import os, sys, secrets

import openapi_client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from globals import waypoint, trip
from findTrip import getTripSuggestions
from main import *
from apiHandler import getMapsToken
from colorama import Fore
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim


# get maps api key from file
mapsAPIKey = getMapsToken()

# global var for list of trips
trips = []


# tripObj is the searchedTrip from input fields
class tripObj:
    def __init__(self, startLocation: str, startLocationCoords: str, destinationLocation: str, destinationLocationCoords: str, opt1: bool, opt2: bool):
        self.startLocation: str = startLocation
        self.startLocationCoords: str = startLocationCoords
        self.destinationLocation: str = destinationLocation
        self.destinationLocationCoords: str = destinationLocationCoords
        self.opt1: bool = opt1
        self.opt2: bool = opt2

    # return dict of the object to be stored in serialized and session
    def to_dict(self):
        return {
            'startLocation': self.startLocation,
            'startLocationCoords': self.startLocationCoords,
            'destinationLocation': self.destinationLocation,
            'destinationLocationCoords': self.destinationLocationCoords,
            'opt1': self.opt1,
            'opt2': self.opt2
        }
    

def formatTime(timeDate: str) -> str:
    time = timeDate.split("T")[1]
    timeArr = time.split(":")
    return timeArr[0] + ":" + timeArr[1]



def formatCoords(coords: str) -> str:
    print("original: " + coords)
    if (coords.__contains__("'")):
        temp = coords.split("'")
        coords = temp[1] + ", " + temp[3]
        print("remove ':" + coords)
    if (coords.__contains__("(")):
        coords = coords[1:-1]
    print("remove ():" + coords)
    return coords


"""
The function `get_location_by_coordinates` takes latitude and longitude coordinates as input and
returns the corresponding address using the Nominatim geocoding service.

:param lat: The latitude of the location you want to get the address for
:param lon: The "lon" parameter represents the longitude coordinate of a location
:return: the address of the location corresponding to the given latitude and longitude coordinates.
"""
geolocator = Nominatim(user_agent="VastTrafikMicrobilitet")
def get_location_by_coordinates(coords):
    """ coords = tuple(float(i) for i in coords.split(', '))
    location = geolocator.reverse(coords, exactly_one=True) """
    print("Coords: ", coords)
    location = geolocator.reverse(coords, exactly_one=True)
    print("Location: ", location)
    print("Adress:", location.address)
    return location.address


app = Flask(__name__)  
# set the secret key to a random string
app.secret_key = secrets.token_hex(16)
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='None',
)


@app.route('/', methods=['POST', 'GET'])
def index():
    # init the trip object and trips list
    global trips
    searchedTrip: tripObj = None
    trips = []
            
    

    # check if the trip object and trips list are stored in session
    if 'searchedTrip' in session:
        searchedTrip: tripObj = session['searchedTrip']
        trips = session['trips']
        noTripSearchedError: str = session['searchedTrip']

    # if the request is POST
    if request.method == 'POST':
        # get the form data as dict
        formData: dict[str, str] = request.form.to_dict()

        # get the coordinates from the form data
        startCoordsList: list[str] = formData.get('startLocationCoords').split(',')
        destinationCoordsList: list[str] = formData.get('destinationLocationCoords').split(',')
        print(startCoordsList)
        if len(startCoordsList) != 2 or len(destinationCoordsList) != 2:
            print("Error: invalid coordinates")
            session['searchedTrip'] = tripObj(
                "", 
                "", 
                "", 
                "", 
                False if formData.get('opt1') is None else True, 
                False if formData.get('opt2') is None else True
            ).to_dict()
            session['trips'] = []
            session['noTripSearchedError'] = "Error: Ogiltig address"
            return redirect(url_for('index'))
        else:
            startCoordsPair: coordinatePair = coordinatePair(startCoordsList[0], startCoordsList[1])
            destinationCoordsPair: coordinatePair = coordinatePair(destinationCoordsList[0], destinationCoordsList[1])

        # create a trip object
        searchedTrip = tripObj(
            startLocation = formData.get('startLocation'),
            startLocationCoords = formData.get('startLocationCoords'),
            destinationLocation = formData.get('destinationLocation'), 
            destinationLocationCoords = formData.get('destinationLocationCoords'),
            opt1 = False if formData.get('opt1') is None else True, 
            opt2 = False if formData.get('opt2') is None else True
        )

        # get trips from backend
        try:
            result = getTripSuggestions(startCoordsPair, destinationCoordsPair)
            for trip in result:
                travleModeList = []
                if result[trip] is not None:
                    newTrip = result[trip].to_dict()
                    newTrip['departure'] = datetime.now().strftime("%H:%M")
                    newTrip["arrival"] = (datetime.now() + timedelta(minutes = newTrip["duration"])).strftime("%H:%M")

                    if len(newTrip['waypoints']) == 1:
                        if (newTrip['waypoints'][0]['mode'] == "WALKING"):
                            newTrip['travelMode'] = "walk"
                    else:  
                        for waypoint in newTrip['waypoints']:
                            if waypoint['mode'] == "BICYCLING":
                                newTrip['travelMode'] = "bike"
                                break
                            elif waypoint['mode'] == "VOI":
                                newTrip['travelMode'] = "voi"
                                break
                    if "travelMode" not in newTrip:
                        newTrip['travelMode'] = "tram"
                    
                    for waypoint in newTrip['waypoints']:
                        if waypoint['mode'] == "BICYCLING" and "bike" not in travleModeList:
                            travleModeList.append("bike")
                        elif waypoint['mode'] == "VOI" and "voi" not in travleModeList:
                            travleModeList.append("voi")
                        elif waypoint['mode'] == "TRANSIT" and "tram" not in travleModeList:
                            travleModeList.append("tram")
                    
                    #print("travleModeList: " + str(travleModeList))
                    newTrip['travleModeList'] = travleModeList
                    #print(newTrip)

                    trips.append(newTrip)
            trips = sorted(trips, key=lambda trip: trip['duration'])
        except Exception as error:
            print(Fore.RED + "\n----------ERROR-----------\n")
            print(traceback.format_exc())
            print(type(error))
            if isinstance(error, openapi_client.exceptions.BadRequestException) or isinstance(error, openapi_client.exceptions.UnauthorizedException):
                httpStatus = error.status
                httpReason = error.reason
                errorText = f"Error: {httpStatus} {httpReason}"
            elif isinstance(error, IndexError):
                errorText = "Error: Hittade ingen resa"
            else:
                errorText = "Error: 500 Internal Server Error"
                print("Error: " + str(error))
            print("\n----------ERROR-----------\n" + Fore.RESET)
            trips = []
            session['noTripSearchedError'] = errorText
            return redirect(url_for('index'))


        # store the trip object in session
        session['trips'] = trips
        session['searchedTrip'] = searchedTrip.to_dict()
        session['noTripSearchedError'] = None
        
        return redirect(url_for('index'))
    
    # if the request is GET
    else:
        #trips = session.pop('trips', []) 
        searchedTrip = session.pop('searchedTrip', searchedTrip)
        if "trips" in session and searchedTrip is not None:
            trips = session['trips']
        else:
            trips = []
        if searchedTrip is None:
            searchedTrip = tripObj("", "", "", "", True, True).to_dict()
        noTripSearchedError = session.pop('noTripSearchedError', "Sök en resa för att börja")
        return render_template('index.html', searchedTrip = searchedTrip, trips = trips, noTripSearchedError = noTripSearchedError, mapsAPIKey = mapsAPIKey)


@app.route('/detailedTrip/tripIndex=<int:tripIndex>', methods=['POST', 'GET'])
def detailedTrip(tripIndex):
    print("index = " + str(tripIndex))
    return render_template('detailedTrip.html', mapsAPIKey = mapsAPIKey, trip = trips[tripIndex])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
