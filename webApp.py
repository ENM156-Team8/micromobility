from flask import Flask, request, jsonify
from flask_cors import CORS
from main import *
#from pyscript import document

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


""" def generate_image(event):
    input_text = document.querySelector("#error_code")
    error_code = input_text.value
    error_img = "https://http.cat/" + error_code
    output_div = document.querySelector("#output")
    output_div.innerHTML = "<img src='" + error_img + "'/>" """

@app.route('/submitTrip', methods=['POST'])
def submit_trip():
    data = request.get_json()
    start_location: str = data.get('startLocation')
    destination_location: str = data.get('destinationLocation')
    start: coordinatePair = parsLocation(start_location)
    destination: coordinatePair  = parsLocation(destination_location)

    vtResponse: str = apiCallerVt(start, destination, vtApiType.POSITIONS)
    sosResponse: dict = apiCallerSos(start)

    return jsonify(message=f"<p>Your trip from ({start_location}) to ({destination_location}) has been submitted!</p>")

def parsLocation(location: str) -> coordinatePair:
    lat_long: list[str] = location.split(",")
    latitude: float = float(lat_long[0].strip())
    longitude: float = float(lat_long[1].strip())
    coords = coordinatePair(latitude, longitude)
    return coords

if __name__ == "__main__":
    app.run(debug=True)