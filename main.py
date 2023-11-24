import json
import requests
from enum import Enum
from apiHandler import *
from globals import coordinatePair, vtApiType


def main():
    print("Main running")
    testCord = coordinatePair(57.687274, 11.979054)
    testCordStart = coordinatePair(57.690012, 11.972992)  # Chalmersplatsen
    testCordEnd = coordinatePair(57.696868, 11.987018)  # Korsvägen
    # apiCallerVt(TestCordStart, TestCordEnd, vtApiType.POSITIONS)
    # getGid(TestCordStart)
    # apiCallerSos(testCord)
    getSosTrip(testCordStart, testCordEnd)


def getSosTrip(start: coordinatePair, end: coordinatePair):
    totalDuration = 0
    totalDistance = 0
    instructions = ""
    segments = []

    # Get closest stations
    startStation = apiCallerSos(start)[0]
    startStationCord = coordinatePair(
        startStation.get("Lat", "invalid"), startStation.get("Long", "invalid"))

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

    # Bike betweem stations
    bikeJourney = apiCallerVt(
        startStationCord, endStationCord, vtApiType.BIKEJOURNEY)
    bikeJourney = bikeJourney["results"][0].get("destinationLink")
    bikeDistance = bikeJourney.get("distanceInMeters")
    bikeDuration = bikeJourney.get("plannedDurationInMinutes")
    totalDuration += bikeDuration
    totalDistance += bikeDistance
    instructions += "Bike " + \
        str(bikeDistance) + " meters to: " + \
        endStation.get("Name", "No name") + ".\n"
    segments.append({"type": "bike", "distance": bikeDistance,
                    "duration": bikeDuration, "from": startStationCord, "to": endStationCord})

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


if __name__ == '__main__':
    main()
