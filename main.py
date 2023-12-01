import requests
from enum import Enum
from apiHandler import *
from globals import coordinatePair, vtApiType, googleTripMode, googleApiMode








def main():
    print("Main running")
    # testCord = coordinatePair(57.687274, 11.979054)
    # testCordStart = coordinatePair(57.690012, 11.972992)  # Chalmersplatsen
    # testCordEnd = coordinatePair(57.696868, 11.987018)  # Korsvägen
    # # apiCallerVt(TestCordStart, TestCordEnd, vtApiType.POSITIONS)
    # # getGid(TestCordStart)
    # # apiCallerSos(testCord)
    # getSosTrip(testCordStart, testCordEnd)
    # getTripByTram("Chalmers", "Korsvägen")
    # sosTestCord = coordinatePair(57.687274, 11.979054)'
    # apiCallerSos(sosTestCord)
    googleTestCordStart = coordinatePair(57.690012, 11.972992)
    googleTestCordEnd = coordinatePair(57.713417, 12.035972)
    #apiCallerVt(vtTestCordStart, vtTestCordEnd, vtApiType.POSITIONS)
    # getGid(vtTestCordStart)
    #apiCallerGoogleDirections(vtTestCordStart, vtTestCordEnd, googleApiMode.BICYCLING)
    getGoogleTrip(googleTestCordStart, googleTestCordEnd, googleTripMode.VOI)
    


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


#Request google trip
#Either walking, bicycling or Voi
def getGoogleTrip(start:coordinatePair, end:coordinatePair, mode:googleTripMode):
    totalDuration = 0
    totalDistance = 0
    totalCost = 0
    match mode:
        case mode.WALK: 
            data = apiCallerGoogleDirections(start, end, googleApiMode.WALK)
        case mode.BICYCLING:
            data = apiCallerGoogleDirections(start, end, googleApiMode.BICYCLING)
        case mode.VOI:
            data = apiCallerGoogleDirections(start, end, googleApiMode.BICYCLING)
        case _:
            raise ValueError(f'Unsupported trip: {mode}')
    


    journey = data.get('routes', [{}])[0].get('legs', [{}])[0]
    totalDuration += int(journey.get('duration').get('text').split(" ")[0])
    totalDistance += float(journey.get('distance').get('text').split(" ")[0])
    totalCost += tripCost(totalDuration, mode)

    #print(f'{totalDuration},{totalDistance},{totalCost}')
    trip = {"duration" : totalDuration, "distance": totalDistance, "cost": totalCost}
    print("TRIP:")
    print(trip)

    return trip

def tripCost(duration, mode:googleTripMode):
    cost = 0
    if mode == googleTripMode.VOI:
        cost += 10 + 2.5*float(duration)
    if mode == googleTripMode.BICYCLING:
        cost += 20*(duration//30+1)
     
    return cost

if __name__ == '__main__':
    main()
