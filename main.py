import json
import requests

from globals import coordinatePair, vtApiType, googleTripMode, googleApiMode, sosStation, trip, waypoint
import threading
import time
from enum import Enum
from apiHandler import *
from globals import coordinatePair, vtApiType, googleTripMode, googleApiMode


def main():
    testCord = coordinatePair(57.687274, 11.979054)
    testCordStart = coordinatePair(57.690012, 11.972992)  # Chalmersplatsen
    testCordEnd = coordinatePair(57.696868, 11.987018)  # Korsvägen
    googleTestCordStart = coordinatePair(57.690012, 11.972992)
    googleTestCordEnd = coordinatePair(57.713417, 12.035972)
    getSosTrip(testCordStart, testCordEnd)


def getSosTrip(start: coordinatePair, end: coordinatePair) -> trip:
    '''
    Calculates the shortest trip from start to end using Styr&Ställ stations.
    :return: shortest trip as a dictionary with keys: duration, distance, instructions, segments, cost
    '''
    start_time = time.time()

    # Get closest stations
    startStations: [sosStation] = apiCallerSos(start)
    endStations: [sosStation] = apiCallerSos(end)

    #if no possible trips 
    if (len(startStations) == 0 or len(endStations) == 0):
        return None

    possibleTrips = []
    for startStation in startStations:
 
        if startStation.open == True and startStation.availableBikes > 0:
            #print("här1")
            startStationCord = coordinatePair(
                startStation.latitude, startStation.longitude)

            # Walk to start station
            firstWalk = getGoogleTrip(
                start, startStationCord, googleTripMode.WALK)
            # print(firstWalk.waypoints.show())
            startDistance = firstWalk.waypoints[0].distance
            startDuration = firstWalk.duration
            firstWaypoint = waypoint(
                start, startStationCord, googleApiMode.WALK, startDuration, startDistance, None)

            threads = list()
            for endStation in endStations:
                #print("här2")
                if endStation.open == True:
                    ("starting thread")
                    x = threading.Thread(
                        target=_calculateTripHelper, args=(endStation.name, firstWaypoint, startStationCord, endStation, end, possibleTrips))
                    threads.append(x)
                    x.start()

            for thread in threads:
                thread.join()

    print(possibleTrips)
    shortestTrip = possibleTrips[0]
    for oneTrip in possibleTrips:
        if oneTrip.duration < shortestTrip.duration:
            shortestTrip = oneTrip

    print("Shortest trip:", shortestTrip.show())
    print("--- %s seconds ---" % (time.time() - start_time))
    return shortestTrip


def _calculateTripHelper(name, firstWaypoint, startStationCord, endStation, end, possibleTrips):
    '''
    Helper for getSosTrip used concurrently to calculate trip from start to end station.
    :return: 1 if trip was calculated, -1 if not
    '''
    print("running ")
    totalDuration = firstWaypoint.duration
    cost = 0
    waypoints = []
    waypoints.append(firstWaypoint)
    endStationCord = coordinatePair(
        endStation.latitude, endStation.longitude)

    # Bike betweem stations
    bikeJourney = getGoogleTrip(startStationCord, endStationCord,
                                googleTripMode.BICYCLING)
    bikeDistance = bikeJourney.waypoints[0].distance
    bikeDuration = bikeJourney.duration
    totalDuration += bikeDuration
    cost += bikeJourney.cost
    waypoints.append(waypoint(startStationCord, endStationCord,
                     googleApiMode.BICYCLING, bikeDuration, bikeDistance, None))

    # Walk from end station
    endWalk = getGoogleTrip(endStationCord, end, googleTripMode.WALK)
    distance = endWalk.waypoints[0].distance
    duration = endWalk.duration
    totalDuration += duration
    waypoints.append(waypoint(endStationCord, end,
                        googleApiMode.WALK, duration, distance, None))

    calculatedTrip = trip(waypoints, totalDuration, cost)
    print(calculatedTrip)
    possibleTrips.append(calculatedTrip)
    return 1


# requests tram trip info
""" def getTripByTram(startStation: str, endStation: str):
    startStationCord = _getCordByName(startStation)
    endStationCord = _getCordByName(endStation)
    segments = []
    data = apiCallerVt(startStationCord, endStationCord, vtApiType.TRAMJOURNEY)

    # format response
    tramJourney = data.get("results")[0].get("tripLegs")[0]

    # ex. how arrival/departure might look like:
    # 2023-11-24T13:52:00.0000000+01:00
    arrival = tramJourney.get("estimatedArrivalTime")
    departure = tramJourney.get("estimatedDepartureTime")
    duration = tramJourney.get("estimatedDurationInMinutes")

    # todo: implement what type of info we want regarding tramline
    tramInfo = tramJourney.get("serviceJourney")

    segments.append({"type": "tram", "duration": duration,
                     "from": startStationCord, "to": endStationCord,
                     "departure": departure, "arrival": arrival})

    # TESTING
    # with open("response.txt", "w") as f:
    #    f.write(json.dumps(tramJourney, indent=4, sort_keys=True))
    print(segments)
    return segments """


def getGoogleTrip(start: coordinatePair, end: coordinatePair, mode: googleTripMode) -> trip:
    '''
    Request google trip
    Either walking, bicycling or Voi
    '''
    totalDuration = 0
    totalDistance = 0
    totalCost = 0
    tripMode = None

    match mode:
        case mode.WALK:
            data = apiCallerGoogleDirections(start, end, googleApiMode.WALK)
            tripMode = googleApiMode.WALK
        case mode.BICYCLING:
            data = apiCallerGoogleDirections(
                start, end, googleApiMode.BICYCLING)
            tripMode = googleApiMode.BICYCLING
        case mode.VOI:
            data = apiCallerGoogleDirections(
                start, end, googleApiMode.BICYCLING)
            tripMode = googleApiMode.BICYCLING
        case _:
            raise ValueError(f'Unsupported trip: {mode}')

    # print('- ' * 20)
    # print("RESPONSE")
    # print(json.dumps(data, indent=4, sort_keys=True))

    journey = data.get('routes', [{}])[0].get('legs', [{}])[0]
    durationText = journey.get('duration').get('text')
    distanceText = journey.get('distance').get('text')

    totalDuration += int(durationText.split(" ")[0])
    totalDistance += float(distanceText.split(" ")[0])
    totalCost += _tripCost(totalDuration, mode)

    # print(f'{totalDuration},{totalDistance},{totalCost}')
    waypoints = [waypoint(start, end, mode, totalDuration, totalDistance, None)]
    calculatedTrip = trip(waypoints, totalDuration, totalCost)
    # print("TRIP:")
    # print(trip)

    return calculatedTrip



def _tripCost(duration, mode: googleTripMode):
    '''
    Calculates cost of a trip
    '''
    cost = 0
    if mode == googleTripMode.VOI:
        cost += 10 + 2.5*float(duration)
    elif mode == googleTripMode.BICYCLING:
        cost += 20*(duration//30+1)

    return cost


if __name__ == '__main__':
    main()