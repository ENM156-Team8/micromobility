
from apiHandler import *
from globals import coordinatePair, vtApiType, googleTripMode, googleApiMode
from pprint import pprint
import json
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_transport_mode import VTApiPlaneraResaWebV4ModelsJourneyTransportMode

class vtStation:

    def __init__(self, name, gid, latitude, longitude, distance):
        self.name = name
        self.gid = gid
        # self.latitude = latitude
        # self.longitude = longitude
        self.coord = coordinatePair(latitude, longitude)
        self.distance = distance
    
    def show(self):
        return f'{self.name, self.gid, self.latitude, self.longitude, self.distance}'
    
class vtJourney:
    def __init__(self, time, nr_connections, start: coordinatePair, end: coordinatePair):
        self.time = time
        self.nr_connections = nr_connections
        self.start = start
        self.end = end
        
    def show(self):
        return f'{self.time, self.nr_connections, self.start, self.end}'
    


#Uesd in conjunction with locations_by_coordiantes_get to create a list of nearby stations
#On index = 0 is the closest station
def createStations(response):
    #print(res)
    stations = []
    for st in response.results:
        
        station = vtStation(
        name = st.name,
        gid = st.gid,
        latitude = st.latitude,
        longitude = st.longitude,
        distance = st.straight_line_distance_in_meters)

        stations.append(station)
    
    # for station in stations:
    #     print(station.show())
    return stations


#Used in conjunction with the VT API journey response
def getNumberOfConnections(response):
    return(len(response.results[0].trip_legs)-1)

def estimatedTime(response):
    time = 0

    for trip in response.results[0].trip_legs:
        #print(trip.estimated_duration_in_minutes)
        time += (trip.estimated_duration_in_minutes or 0) + (trip.estimated_connecting_time_in_minutes or 0)

    # for connect in response.results[0].connection_links:
    #     time += connect.estimated_duration_in_minutes

    return time

def getVtJourneyStats(response) -> vtJourney:
    #print(response)
    tripLegs = response.results[0].trip_legs
    lenTripLegs = len(tripLegs)
    journey = vtJourney(
        time = estimatedTime(response),
        nr_connections = getNumberOfConnections(response),
        start = coordinatePair(tripLegs[0].origin.stop_point.stop_area.latitude, tripLegs[0].origin.stop_point.stop_area.longitude),
        end = coordinatePair(tripLegs[lenTripLegs-1].destination.stop_point.stop_area.latitude, tripLegs[lenTripLegs-1].destination.stop_point.stop_area.longitude))
    return journey

def checkVtJourney(start: coordinatePair, end: coordinatePair, journey : vtJourney):
    radius = 4000 
    isNewJourney = False
    if journey.nr_connections > 0: # kan flyttas ut 
        stations = createStations(apiCallerVt(start, end, vtApiType.LOCATIONS, radius))
        farAway = stations[len(stations)-10:]

        for station in farAway:
            response = journey_api.journeys_get(origin_latitude=station.coord.latitude, origin_longitude=station.coord.longitude, destination_latitude=end.latitude, destination_longitude=end.longitude, transport_modes=[VTApiPlaneraResaWebV4ModelsJourneyTransportMode.TRAM, VTApiPlaneraResaWebV4ModelsJourneyTransportMode.BUS], only_direct_connections=True)
            if len(response.results) > 0:
                isNewJourney = True
                return getVtJourneyStats(response), isNewJourney
    print("No new journey was found")
    return journey, isNewJourney

#______main______
def main():
    radius = 1000
    testCordStart = coordinatePair(57.690012, 11.972992)  # Chalmersplatsen
    testCordEnd = _getCordByName("Studiegången")  

    #response = location_api.locations_by_coordinates_get(57.690012, 11.972992, radius_in_meters=radius)
    # response = apiCallerVt(testCordStart, _getCordByName("Studiegången"), vtApiType.LOCATIONS, radius=radius)

    # s = createStations(response)
    # print(type(s[0].coord.latitude))

    response = apiCallerVt(testCordStart, testCordEnd, vtApiType.JOURNEY, radius=radius)
    originalJourney = getVtJourneyStats(response)
    trip = checkVtJourney(testCordStart, testCordEnd, originalJourney)
    if trip[1]: # true
        getSosTrip
        
    # print(originalJourney.show())
    # print(trip['new'].show())



    # print(getNumberOfConnections(response1))
    # print(estimatedTime(response1))
    # print(response1.json())


if __name__ == '__main__':
    main()
