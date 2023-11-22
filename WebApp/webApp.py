from flask import Flask, render_template, request, url_for, send_from_directory, redirect, session
import os, sys, secrets
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import *



class tripObj:
    def __init__(self, startLocation, destinationLocation, opt1, opt2):
        self.startLocation = startLocation
        self.destinationLocation = destinationLocation
        self.opt1 = opt1
        self.opt2 = opt2

    # return dict of the object to be stored in serialized and session
    def to_dict(self):
        return {
            'startLocation': self.startLocation,
            'destinationLocation': self.destinationLocation,
            'opt1': self.opt1,
            'opt2': self.opt2
        }



app = Flask(__name__)  
# set the secret key to a random string
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=['POST', 'GET'])
def index():
    # init the trip object and trips list
    searchedTrip = None
    trips = []
    noTripSearchedError: str = 'Sök en resa för att börja'

    # check if the trip object and trips list are stored in session
    if 'searchedTrip' in session:
        searchedTrip = session['searchedTrip']
        trips = session['trips']
        noTripSearchedError: str = None

    # if the request is POST
    if request.method == 'POST':
        # get the form data as dict
        formData = request.form.to_dict()

        # create a trip object
        searchedTrip = tripObj(
            # TODO get coordinates from start and destination addresses
            startLocation = formData.get('startLocation'),
            destinationLocation = formData.get('destinationLocation'), 
            opt1 = False if formData.get('opt1') is None else True, 
            opt2 = False if formData.get('opt2') is None else True
        )

        # TODO get trips from main.py
        tripStr="your trip between: " + searchedTrip.startLocation + " and " + searchedTrip.destinationLocation + " with options: " + str(searchedTrip.opt1) + " and " + str(searchedTrip.opt2) + " has been submitted"
        trips = [tripStr, "test2", "test3"]

        # store the trip object in session
        session['trips'] = trips
        session['searchedTrip'] = searchedTrip.to_dict()
        
        return redirect(url_for('index'))
    
    # if the request is GET
    else:
        session.pop('trips', None)
        session.pop('searchedTrip', None)
        return render_template('index.html', searchedTrip = searchedTrip, trips = trips, noTripSearchedError = noTripSearchedError)




if __name__ == "__main__":
    app.run(debug=True)