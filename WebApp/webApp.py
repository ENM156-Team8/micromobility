from flask import Flask, render_template, request, url_for, send_from_directory, redirect, session
import os, sys, secrets
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import *


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
    noTripSearchedError: str = 'Sök en resa för att börja'

    # check if the trip object and trips list are stored in session
    if 'searchedTrip' in session:
        searchedTrip: tripObj = session['searchedTrip']
        trips: list = session['trips']
        noTripSearchedError: str = None

    # if the request is POST
    if request.method == 'POST':
        # get the form data as dict
        formData: dict[str, str] = request.form.to_dict()

        # get the coordinates from the form data
        startCoordsList: list[str] = formData.get('startLocationCoords').split(',')
        destinationCoordsList: list[str] = formData.get('destinationLocationCoords').split(',')
        # create coordinatePair objects from the coordinates TODO send to main.py
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

        print(searchedTrip.to_dict())

        # TODO get trips from main.py
        tripStr="Your trip between: " + searchedTrip.startLocation + " and " + searchedTrip.destinationLocation + ", with options: " + str(searchedTrip.opt1) + " and " + str(searchedTrip.opt2) + ", with coords: (" + searchedTrip.startLocationCoords + ") and (" + searchedTrip.destinationLocationCoords + ") has been submitted."
        trips = [tripStr, "test2", "test3"]

        # store the trip object in session
        session['trips'] = trips
        session['searchedTrip'] = searchedTrip.to_dict()
        
        return redirect(url_for('index'))
    
    # if the request is GET
    else:
        session.pop('trips', None)
        session.pop('searchedTrip', None)
        return render_template('index.html', searchedTrip = searchedTrip, trips = trips, noTripSearchedError = noTripSearchedError, mapsAPIKey = mapsAPIKey)




if __name__ == "__main__":
    app.run(debug=True)
