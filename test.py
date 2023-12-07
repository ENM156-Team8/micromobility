
from apiHandler import *
from globals import coordinatePair, vtApiType, googleTripMode, googleApiMode
import pprint


class vt_station:
    def __init__(self, name="", gid="", latitude=0, longitude=0, distance=0):
        self.name = name
        self.gid = gid
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
    
    def show(self):
        return f'{self.name, self.gid, self.latitude, self.longitude, self.distance}'

#Uesd in conjunction with locations_by_coordiantes_get to create a list of nearby stations
#On index = 0 is the closest station
def create_stations(res):
    #print(res)
    stations = []
    for st in res.results:
        
        station = vt_station(
        name = st.name,
        gid = st.gid,
        latitude = float(st.latitude),
        longitude = float(st.longitude),
        distance = st.straight_line_distance_in_meters)

        stations.append(station)
    
    # for station in stations:
    #     print(station.show())
    return stations

radius = 1000
response = location_api.locations_by_coordinates_get(57.690012, 11.972992, radius_in_meters=radius)

s = create_stations(response)

response = journey_api.journeys_get(origin_latitude=float(s[0].latitude), origin_longitude=float(s[0].latitude), destination_latitude=float(s[3].latitude), destination_longitude=float(s[3].longitude))
print(response)
