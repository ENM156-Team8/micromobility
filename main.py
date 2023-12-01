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
    getTripByTram("Chalmers", "Korsvägen")


def getSosTrip(start: coordinatePair, end: coordinatePair) -> dict[str, any]:
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

    # Bike between stations
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

    return trip

    
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


if __name__ == '__main__':
    main()
