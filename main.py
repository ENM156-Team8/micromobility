import json
import requests

from globals import coordinatePair, vtApiType, googleTripMode, googleApiMode, sosStation
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


def getSosTrip(start: coordinatePair, end: coordinatePair):
    '''
    Calculates the shortest trip from start to end using Styr&Ställ stations.
    :return: shortest trip as a dictionary with keys: duration, distance, instructions, segments, cost
    '''
    start_time = time.time()

    # Get closest stations
    startStations: [sosStation] = apiCallerSos(start)
    endStations: [sosStation] = apiCallerSos(end)

    possibleTrips = []
    for startStation in startStations:
        if startStation.open == True and startStation.availableBikes > 0:
            startStationCord = coordinatePair(
                startStation.latitude, startStation.longitude)

            # Walk to start station
            firstWalk = getGoogleTrip(
                start, startStationCord, googleTripMode.WALK)
            if firstWalk != -1:
                startDistance = firstWalk.get("distance")
                startDuration = firstWalk.get("duration")
                startInstructions = firstWalk.get("instructions")
                startSegment = {"type": "walk", "distance": startDistance,
                                "duration": startDuration, "from": start.show(), "to": startStationCord.show()}

                threads = list()
                for endStation in endStations:
                    if endStation.open == True:
                        x = threading.Thread(
                            target=_calculateTripHelper, args=(endStation.name, startDuration, startDistance, startInstructions, startSegment, startStationCord, endStation, end, possibleTrips))
                        threads.append(x)
                        x.start()

                for thread in threads:
                    thread.join()

    shortestTrip = possibleTrips[0]
    for trip in possibleTrips:
        if trip.get("duration") < shortestTrip.get("duration"):
            shortestTrip = trip

    print("Shortest trip:", shortestTrip)
    print("--- %s seconds ---" % (time.time() - start_time))
    return shortestTrip


def _calculateTripHelper(name, startDuration, startDistance, startInstructions, startSegment, startStationCord, endStation, end, possibleTrips):
    '''
    Helper for getSosTrip used concurrently to calculate trip from start to end station.
    :return: 1 if trip was calculated, -1 if not
    '''
    totalDuration = startDuration
    totalDistance = startDistance
    cost = 0
    instructions = startInstructions
    segments = [startSegment]

    endStationCord = coordinatePair(
        endStation.latitude, endStation.longitude)

    # Bike betweem stations
    bikeJourney = getGoogleTrip(startStationCord, endStationCord,
                                googleTripMode.BICYCLING)
    bikeDistance = bikeJourney.get("distance")
    bikeDuration = bikeJourney.get("duration")

    totalDuration += bikeDuration
    totalDistance += bikeDistance
    cost = bikeJourney.get("cost")
    instructions += bikeJourney.get("instructions")
    segments.append({"type": "bike", "distance": bikeDistance,
                    "duration": bikeDuration, "from": startStationCord.show(), "to": endStationCord.show()})

    # Walk from end station
    endWalk = getGoogleTrip(endStationCord, end, googleTripMode.WALK)
    if endWalk != -1:
        distance = endWalk.get("distance")
        duration = endWalk.get("duration")
        totalDuration += duration
        totalDistance += distance
        instructions += endWalk.get("instructions")
        segments.append({"type": "walk", "distance": distance,
                        "duration": duration, "from": endStationCord.show(), "to": end.show()})

    trip = {"duration": totalDuration,
            "distance": totalDistance, "instructions": instructions, "segments": segments, "cost": cost}
    possibleTrips.append(trip)
    return 1


# requests tram trip info
def getTripByTram(startStation: str, endStation: str):
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
    return segments


def getGoogleTrip(start: coordinatePair, end: coordinatePair, mode: googleTripMode):
    '''
    Request google trip
    Either walking, bicycling or Voi
    '''
    totalDuration = 0
    totalDistance = 0
    totalCost = 0
    instructions = ""

    match mode:
        case mode.WALK:
            data = apiCallerGoogleDirections(start, end, googleApiMode.WALK)
            instructions += "\n Walk "
        case mode.BICYCLING:
            data = apiCallerGoogleDirections(
                start, end, googleApiMode.BICYCLING)
            instructions += "\n Bike "
        case mode.VOI:
            data = apiCallerGoogleDirections(
                start, end, googleApiMode.BICYCLING)
            instructions += "\n Voi "
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

    instructions += f'{distanceText} from {journey.get("start_address")} for {durationText} to {journey.get("end_address")}.' + \
        "\n" + f'This trip will cost you: {totalCost} kr.'

    # print(f'{totalDuration},{totalDistance},{totalCost}')
    trip = {"duration": totalDuration, "distance": totalDistance,
            "cost": totalCost, "instructions": instructions}
    # print("TRIP:")
    # print(trip)

    return trip


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
