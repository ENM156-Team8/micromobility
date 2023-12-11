
from apiHandler import *
from globals import coordinatePair, vtApiType, googleTripMode, googleApiMode, trip, waypoint
from pprint import pprint
import json
from openapi_client.models.vt_api_planera_resa_web_v4_models_journey_transport_mode import VTApiPlaneraResaWebV4ModelsJourneyTransportMode
from main import getSosTrip, getGoogleTrip

class vtStation:

    def __init__(self, name, gid, latitude, longitude, distance):
        self.name = name
        self.gid = gid
        # self.latitude = latitude
        # self.longitude = longitude
        self.coord = coordinatePair(latitude, longitude)
        self.distance = distance
    
    def show(self):
        return f'{self.name, self.gid, self.coord, self.distance}'
    
class vtJourney:
    def __init__(self, time, nr_connections, start: coordinatePair, end: coordinatePair, waypoints: list):
        self.time = time
        self.nr_connections = nr_connections
        self.start = start
        self.end = end
        self.waypoints = waypoints
        
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

def getVtWaypoints(tripLegs):
    waypoints =[]
    for leg in tripLegs:
        startCord = coordinatePair(leg.origin.stop_point.stop_area.latitude, leg.origin.stop_point.stop_area.longitude)
        endCord = coordinatePair(leg.destination.stop_point.stop_area.latitude, leg.destination.stop_point.stop_area.longitude)
        way = waypoint(start = startCord,
                destination = endCord,
                mode = googleApiMode.TRANSIT,
                duration = leg.estimated_duration_in_minutes,
                distance = None,
                line = {leg.service_journey.line.designation, leg.service_journey.line.background_color, leg.service_journey.line.foreground_color})
        waypoints.append(way)
    return waypoints


def getVtJourneyStats(response) -> vtJourney:
    #print(response)
    tripLegs = response.results[0].trip_legs
    lenTripLegs = len(tripLegs)
    journey = vtJourney(
        time = estimatedTime(response),
        nr_connections = getNumberOfConnections(response),
        start = coordinatePair(tripLegs[0].origin.stop_point.stop_area.latitude, tripLegs[0].origin.stop_point.stop_area.longitude),
        end = coordinatePair(tripLegs[lenTripLegs-1].destination.stop_point.stop_area.latitude, tripLegs[lenTripLegs-1].destination.stop_point.stop_area.longitude),
        waypoints = getVtWaypoints(tripLegs))
    return journey


def checkVtJourney(start: coordinatePair, end: coordinatePair, journey : vtJourney):
    radius = 4000 
    isNewJourney = False
    if journey.nr_connections > 0: # kan flyttas ut 
        stations = createStations(apiCallerVt(start, end, vtApiType.LOCATION, radius))

        for station in stations:
            print(station.show())

        if len(stations) >= 20:
            farAway = stations[len(stations)-20:]
        else:
            farAway = stations 

        for station in farAway:
            response = journey_api.journeys_get(origin_latitude=station.coord.latitude, origin_longitude=station.coord.longitude, destination_latitude=end.latitude, destination_longitude=end.longitude, transport_modes=[VTApiPlaneraResaWebV4ModelsJourneyTransportMode.TRAM, VTApiPlaneraResaWebV4ModelsJourneyTransportMode.BUS], only_direct_connections=True)
            print(response.json())
            if len(response.results) > 0:
                isNewJourney = True
                return getVtJourneyStats(response), isNewJourney
    print("No new journey was found")
    return journey, isNewJourney


def combineVtAndSos(start: coordinatePair, vt: vtJourney):
    bikeJourney = getSosTrip(start, vt.start)   #(start point, end: new journey start point)
    if bikeJourney == None:
        return None
    newTripTotalTime = bikeJourney.duration + vt.time 
    way = bikeJourney.waypoints + vt.waypoints
    cost = bikeJourney.cost + 35 #TODO calculate cost
    sosVtTrip = trip(waypoints = way,
                duration = newTripTotalTime,
                cost = cost)
     
    return sosVtTrip #(list of waypoints including start cord, end cord and transportmode for each tripleg)


def combineVtAndVoi(start: coordinatePair, vt: vtJourney):
    voiJourney = getGoogleTrip(start, vt.start, googleTripMode.VOI)
    newTripTotalTime = voiJourney.duration + vt.time
    
    cost = 35 + voiJourney.cost #TODO calculate cost
    voiVtTrip = trip(waypoints = voiJourney.waypoints + vt.waypoints, 
                duration = newTripTotalTime, 
                cost = cost)
    return voiVtTrip

    
def getTripSuggestions(start: coordinatePair, end: coordinatePair): # return dict of trips
    # todo: combine different waypoints to a trip dict, convert originaljourney and combinedtrips to trips
    
    tripDictionary = {}
    tripDictionary["sosTrip"] = getSosTrip(start, end) #garanterad en trip
    response = apiCallerVt(start, end, vtApiType.JOURNEY, radius=1000)
    vtOriginal = getVtJourneyStats(response)
    tripDictionary["originalJourney"] =  trip(waypoints = vtOriginal.waypoints,
                                            duration = vtOriginal.time,
                                            cost = 35)#garanterad en trip
   
    vtTrip = checkVtJourney(start, end, vtOriginal)
    if vtTrip[1]: # true, there is a new jour
        combinedVtAndSos: trip = combineVtAndSos(start, vtTrip[0]) #garanterat en trip
        combinedVtAndVoi: trip = combineVtAndVoi(start, vtTrip[0]) #garanterat en trip
        tripDictionary["combinedTrips"] = {combinedVtAndSos, combinedVtAndVoi}
    return tripDictionary
        
 


#______main______
def main():
    testCordStart = coordinatePair(57.690012, 11.972992)  # Chalmersplatsen
    testCordEnd = _getCordByName("Studiegången")  
    print("THE ANSWER _________________________\n", getTripSuggestions(testCordStart, testCordEnd))

    #response = location_api.locations_by_coordinates_get(57.690012, 11.972992, radius_in_meters=radius)
    # response = apiCallerVt(testCordStart, _getCordByName("Studiegången"), vtApiType.LOCATIONS, radius=radius)

    # s = createStations(response)
    # print(type(s[0].coord.latitude))

    

        



    #bikeJourney2 = getSosTrip(start, vt.end) #start and end point for original trip
    #if bikeJourney2 < originalJourney.getEstimatedTime:
    #    return bikeJourney2 #(as list of waypoints)
    #else:
    #    return originalJourney #(as list of waypoints)
        
    # print(originalJourney.show())
    # print(trip['new'].show())



    # print(getNumberOfConnections(response1))
    # print(estimatedTime(response1))
    # print(response1.json())


if __name__ == '__main__':
    main()
