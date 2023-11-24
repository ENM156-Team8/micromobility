import json
import requests
from enum import Enum
from apiHandler import *
from globals import coordinatePair, vtApiType, sosStation


def main():
    print("Main running")
    testCord = coordinatePair(57.687274, 11.979054)
    testCordStart = coordinatePair(57.690012, 11.972992)  # Chalmersplatsen
    testCordEnd = coordinatePair(57.696868, 11.987018)  # Korsvägen
    # apiCallerVt(TestCordStart, TestCordEnd, vtApiType.POSITIONS)
    # getGid(TestCordStart)
    # apiCallerSos(testCord)
    getSosTrip(testCordStart, testCordEnd)
    # apiCallerVt(testCordStart, testCordEnd, vtApiType.JOURNEY)


def getSosTrip(start: coordinatePair, end: coordinatePair):
    totalDuration = 0
    totalDistance = 0
    cost = 0
    instructions = ""
    segments = []

    # Get closest stations
    startStations = apiCallerSos(start)
    startStation = startStations[0]
    startStationCord = coordinatePair(
        startStation.latitude, startStation.longitude)

    endStations: [sosStation] = apiCallerSos(end)
    endStation = endStations[0]
    endStationCord = coordinatePair(
        endStation.latitude, endStation.longitude)

    # Walk to start station
    journey = apiCallerVt(start, startStationCord, vtApiType.WALKJOURNEY)
    if journey != -1:
        journey = journey["results"][0].get("destinationLink")
        distance = journey.get("distanceInMeters")
        duration = journey.get("plannedDurationInMinutes")
        totalDuration += duration
        totalDistance += distance
        instructions += "Walk " + str(startStation.distance) + \
            " meters to: " + startStation.name + ".\n"
        segments.append({"type": "walk", "distance": distance,
                        "duration": duration, "from": start.show(), "to": startStationCord.show()})

    # Bike betweem stations
    bikeJourney = apiCallerVt(
        startStationCord, endStationCord, vtApiType.BIKEJOURNEY)
    bikeJourney = bikeJourney["results"][0].get("destinationLink")
    bikeDistance = bikeJourney.get("distanceInMeters")
    bikeDuration = bikeJourney.get("plannedDurationInMinutes")
    totalDuration += bikeDuration
    totalDistance += bikeDistance
    cost += 20*(bikeDuration//20+1)
    instructions += "Bike " + \
        str(bikeDistance) + " meters to: " + \
        endStation.name + ".\n"
    segments.append({"type": "bike", "distance": bikeDistance,
                    "duration": bikeDuration, "from": startStationCord.show(), "to": endStationCord.show()})

    # Walk from end station
    journey = apiCallerVt(endStationCord, end, vtApiType.WALKJOURNEY)
    if journey != -1:
        journey = journey["results"][0].get("destinationLink")
        distance = journey.get("distanceInMeters")
        duration = journey.get("plannedDurationInMinutes")
        totalDuration += duration
        totalDistance += distance
        instructions += "Walk " + str(endStation.distance) + \
            " meters from " + \
            endStation.name + " to destination. \n"
        segments.append({"type": "walk", "distance": distance,
                        "duration": duration, "from": endStationCord.show(), "to": end.show()})

    trip = {"duration": totalDuration,
            "distance": totalDistance, "instructions": instructions, "segments": segments, "cost": cost}
    print("TRIP:")
    print(trip)
    print(trip.get("instructions", "No instructions"))


if __name__ == '__main__':
    main()
