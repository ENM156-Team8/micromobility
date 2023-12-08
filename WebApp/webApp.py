import traceback
from flask import Flask, render_template, request, url_for, redirect, session
import os, sys, secrets
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import *
from apiHandler import getMapsToken
from colorama import Fore
from datetime import datetime, timedelta


# TODO get maps api key from file
mapsAPIKey = getMapsToken()



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

def searchSosTrip(startCoordsPair, destinationCoordsPair):
    sosTrip = getSosTrip(startCoordsPair, destinationCoordsPair)
    #print(sosTrip)
    for segment in sosTrip["segments"]:
        # print("from " + str(segment["from"]))
        segment["from"] = segment["from"].to_dict()
        # print("to " + str(segment["to"]))
        segment["to"] = segment["to"].to_dict()
        sosTrip["departure"] = datetime.now().strftime("%H:%M")
        sosTrip["arrival"] = (datetime.now() + timedelta(minutes = sosTrip["duration"])).strftime("%H:%M")
    return sosTrip

def searchTramTrip(startCoordsPair, destinationCoordsPair):
    tramTrip = getTripByTram(startCoordsPair, destinationCoordsPair)[0]
    print(tramTrip)
    tramTrip["from"] = tramTrip["from"].to_dict()
    tramTrip["to"] = tramTrip["to"].to_dict()
    tramTrip["departure"] = formatTime(tramTrip["departure"])
    tramTrip["arrival"] = formatTime(tramTrip["arrival"])
    return tramTrip



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
    searchedTrip: tripObj = None
    trips = []

    # check if the trip object and trips list are stored in session
    if 'searchedTrip' in session:
        searchedTrip: tripObj = session['searchedTrip']
        trips: list = session['trips']
        noTripSearchedError: str = session['searchedTrip']

    # if the request is POST
    if request.method == 'POST':
        # get the form data as dict
        formData: dict[str, str] = request.form.to_dict()

        # get the coordinates from the form data
        startCoordsList: list[str] = formData.get('startLocationCoords').split(',')
        destinationCoordsList: list[str] = formData.get('destinationLocationCoords').split(',')
        print(startCoordsList)
        # create coordinatePair objects from the coordinates TODO send to main.py
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
            # TODO get coordinates from start and destination addresses
            startLocation = formData.get('startLocation'),
            startLocationCoords = formData.get('startLocationCoords'),
            destinationLocation = formData.get('destinationLocation'), 
            destinationLocationCoords = formData.get('destinationLocationCoords'),
            opt1 = False if formData.get('opt1') is None else True, 
            opt2 = False if formData.get('opt2') is None else True
        )

        # TODO get trips from main.py
        try:
            trips.append(searchSosTrip(startCoordsPair, destinationCoordsPair))
            #trips.append(searchTramTrip(startCoordsPair, destinationCoordsPair))
        except Exception as error:
            print(Fore.RED + "\n----------ERROR-----------\n")
            print(traceback.format_exc())
            errorData = error.args[0]
            if isinstance(errorData, dict):
                statusCode = errorData.get('statusCode')
                errorText = "Error: " + str(statusCode) + " " + str(errorData.get('message'))
                print(errorText + ", url: " + str(errorData.get('url')))
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
        trips = session.pop('trips', []) 
        searchedTrip = session.pop('searchedTrip', None)
        noTripSearchedError = session.pop('noTripSearchedError', "Sök en resa för att börja")
        print(trips)
        return render_template('index.html', searchedTrip = searchedTrip, trips = trips, noTripSearchedError = noTripSearchedError, mapsAPIKey = mapsAPIKey)


@app.route('/detailedTrip/tripIndex=<int:tripIndex>', methods=['POST', 'GET'])
def detailedTrip(tripIndex):
    print("index = " + str(tripIndex))
    return render_template('detailedTrip.html', mapsAPIKey = mapsAPIKey)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
