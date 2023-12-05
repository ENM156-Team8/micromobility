import requests
from enum import Enum
from apiHandler import *
from globals import coordinatePair, vtApiType
import json


def main():
    print("Main running")
    testCord = coordinatePair(57.687274, 11.979054)
    testCordStart = coordinatePair(57.690012, 11.972992)  # Chalmersplatsen
    #testCordEnd = coordinatePair(57.696868, 11.987018)  # Korsvägen
    testCordEnd = coordinatePair(57.719998787966006, 12.932556366328921) # Borås Station
    # apiCallerVt(TestCordStart, TestCordEnd, vtApiType.POSITIONS)
    # getGid(TestCordStart)
    # apiCallerSos(testCord)
    #getSosTrip(testCordStart, testCordEnd)
    #getTripByTram("Chalmers", "Korsvägen")
    getVsTrip("Chalmers", "Kapellplatsen")


def getSosTrip(start: coordinatePair, end: coordinatePair):
    totalDuration = 0
    totalDistance = 0
    totalCostSOS = 0
    instructions = ""
    segments = []

    # Get closest stations
    startStation = apiCallerSos(start)[0]
    startStationCord = coordinatePair(
        startStation.get("Lat", "invalid"), startStation.get("Long", "invalid"))
    
        
    try: apiCallerSos(end)[0]
    except: print("Ingen station i närheten")
    endStation = apiCallerSos(end)[0]
    endStationCord = coordinatePair(
        endStation.get("Lat", "invalid"), endStation.get("Long", "invalid"))

    # Walk to start station
    journey = apiCallerVt(start, startStationCord, vtApiType.WALKJOURNEY)
    if journey != -1:
        journey = journey["results"][0].get("destinationLink")
        distance = journey.get("distanceInMeters")
        duration = journey.get("plannedDurationInMinutes")
        totalDuration += duration
        totalDistance += distance
        instructions += "Walk " + str(startStation.get("Distance", "invalid")) + \
            " meters to: " + startStation.get("Name", "No name") + ".\n"
        segments.append({"type": "walk", "distance": distance,
                        "duration": duration, "from": start, "to": startStationCord})

    # Bike between stations
    bikeJourney = apiCallerVt(
        startStationCord, endStationCord, vtApiType.BIKEJOURNEY)
    bikeJourney = bikeJourney["results"][0].get("destinationLink")
    bikeDistance = bikeJourney.get("distanceInMeters")
    bikeDuration = bikeJourney.get("plannedDurationInMinutes")
    bikeCost = 20*(bikeDuration//30)
    totalCostSOS += bikeCost
    totalDuration += bikeDuration
    totalDistance += bikeDistance
    instructions += "Bike " + \
        str(bikeDistance) + " meters to: " + \
        endStation.get("Name", "No name") + ".\n"
    segments.append({"type": "bike", "distance": bikeDistance,
                    "duration": bikeDuration, "from": startStationCord, "to": endStationCord, "cost": totalCostSOS})

    # Walk from end station
    journey = apiCallerVt(endStationCord, end, vtApiType.WALKJOURNEY)
    if journey != -1:
        journey = journey["results"][0].get("destinationLink")
        distance = journey.get("distanceInMeters")
        duration = journey.get("plannedDurationInMinutes")
        totalDuration += duration
        totalDistance += distance
        instructions += "Walk " + str(endStation.get("Distance", "invalid")) + \
            " meters from " + \
            endStation.get("Name", "No name") + " to destination. \n"
        segments.append({"type": "walk", "distance": distance,
                        "duration": duration, "from": endStationCord, "to": end})

    trip = {"duration": totalDuration,
            "distance": totalDistance, "instructions": instructions, "segments": segments}
    print("TRIP:")
    print(trip)
    print(trip.get("instructions", "No instructions"))

    
# requests tram trip info
def getVsTrip(startStation: str, endStation: str):
    startStationCord = _getCordByName(startStation)
    endStationCord = _getCordByName(endStation)
    segments = []
    data = apiCallerVt(startStationCord, endStationCord, vtApiType.JOURNEY)

    journey = data.get("results")[0].get("tripLegs")[1]

    with open("response.txt", "w") as f:
        f.write(json.dumps(journey, indent=4, sort_keys=True))

    # format response
    if len(journey) > 1: 
        # there is a connection
        
        # we're only interested in the first connection
        totalConnectionTime = journey.get("estimatedConnectingTimeInMinutes") + journey.get("estimatedDurationInMinutes")
        boolMissCon = journey.get("isRiskOfMissingConnection")
        start = journey.get("origin").get("stopPoint").get("stopArea")
        startLat = round(start.get("latitude"), 6)
        startLong = round(start.get("longitude"), 6)

        end = journey.get("destination").get("stopPoint").get("stopArea")
        endLat = round(end.get("latitude"), 6)
        endLong = round(end.get("longitude"), 6)

        startCord = coordinatePair(startLat, startLong)
        print(endLat)
        print(endLong)
        endCord = coordinatePair(endLat, endLong)

        getSosTrip(startCord, endCord)

    #print(totalConnectionTime)
    #print(boolMissCon)


    # hämta bytesstation
    # skicka in kordinater i sos
    # jämföra om sos går snabbare eller inte än vt


    # TESTING
    #with open("response.txt", "w") as f:
    #    f.write(json.dumps(tramJourney, indent=4, sort_keys=True))

    # ex. how arrival/departure might look like:
    # 2023-11-24T13:52:00.0000000+01:00
    #arrival = tramJourney.get("estimatedArrivalTime")
    #departure = tramJourney.get("estimatedDepartureTime")
    #duration = tramJourney.get("estimatedDurationInMinutes")

    # todo: implement what type of info we want regarding tramline
    #tramInfo = tramJourney.get("serviceJourney")

    #segments.append({"type": "tram", "duration": duration, 
    #                 "from": startStationCord, "to": endStationCord, 
    #                 "departure": departure, "arrival": arrival})
    

    #print(segments)
    return None


if __name__ == '__main__':
    main()
