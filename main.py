import json
import requests
from enum import Enum


def getTokens():
    with open("apiToken.txt", "r") as apiTokenFile:
        apiTokenLines = apiTokenFile.readlines()
    vtToken = apiTokenLines[0].strip()
    sosToken = apiTokenLines[1].strip()
    googleToken = apiTokenLines[2].strip()
    return {"vt": vtToken, "sos": sosToken, "google": googleToken}


apiBaseUrlVt = 'https://ext-api.vasttrafik.se/pr/v4'
tokens = getTokens()
appIdSos = tokens.get("sos", '')
accessTokenVt = tokens.get("vt", '')
accessTokenGoogle = tokens.get("google", '')
vtHeaders = {
    'Authorization': 'Bearer ' + accessTokenVt
}

# Enums used to fetch different data from vtApi
# POSITIONS: Returns journey positions within a bounding box
# JOURNEY: Returns journeys matching the specified search parameters
# LOCATIONS: Returns locations matching the specified text (stop areas, addresses, points of interest and meta-stations)
vtApiType = Enum('vtApiType', ['POSITIONS', 'JOURNEY', 'LOCATIONS'])
googleApiMode = Enum('googleApiMode', ['WALK', 'BICYCLING', 'TRANSIT', 'DRIVE'])
googleTripMode = Enum('googleTripMode', ['WALK', 'BICYCLING', 'VOI'])


class coordinatePair:
    def __init__(self, latitude: int, longitude: int):
        self.latitude = latitude
        self.longitude = longitude


def main():
    print("Main running")
    sosTestCord = coordinatePair(57.687274, 11.979054)
    # apiCallerSos(sosTestCord)
    vtTestCordStart = coordinatePair(57.690012, 11.972992)
    vtTestCordEnd = coordinatePair(57.713417, 12.035972)
    #apiCallerVt(vtTestCordStart, vtTestCordEnd, vtApiType.POSITIONS)
    # getGid(vtTestCordStart)
    #apiCallerGoogleDirections(vtTestCordStart, vtTestCordEnd, googleApiMode.BICYCLING)
    trip = getGoogleTrip(vtTestCordStart, vtTestCordEnd, googleTripMode.VOI)
    print(trip)

def apiCallerGoogleDirections(start:coordinatePair, end:coordinatePair, mode: googleApiMode=None):
    url = ""
    if mode is None:
        url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
    else:
        match mode:
            case mode.WALK: url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&mode=walk&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
            case mode.BICYCLING: url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&mode=bicycling&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
            case mode.TRANSIT: url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&mode=transit&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
            case mode.DRIVE: url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
            case _: raise ValueError(f'Unsupported transport mode: {mode}')
    #print(url)
    response = requests.get(url)
    data = response.json()
    # print('- ' * 20)
    # print("RESPONSE")
    # print(json.dumps(data, indent=4, sort_keys=True))
    return data

def tripCost(duration, mode:googleTripMode):
    cost = 0
    if mode == googleTripMode.VOI:
        cost += 10 + 2.5*float(duration)
    if mode == googleTripMode.BICYCLING:
        cost += 20*(duration//30+1)
     
    return cost

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
    return trip


def apiCallerSos(center: coordinatePair) -> dict:
    radius = 500  # meters
    url = 'https://data.goteborg.se/SelfServiceBicycleService/v2.0/Stations/' + appIdSos + '?getclosingperiods=500&latitude=' + \
        str(center.latitude) + '&longitude=' + str(center.longitude) + \
        '&radius=' + str(radius) + '&format=json'
    return requestHandler(url, {})


def apiCallerVt(start: coordinatePair, end: coordinatePair, apiType: vtApiType) -> str:
    match apiType:
        case apiType.POSITIONS:
            urlEnd = '/positions?lowerLeftLat=' + str(start.latitude) + '&lowerLeftLong=' + str(
                start.longitude) + '&upperRightLat=' + str(end.latitude) + '&upperRightLong=' + str(end.longitude) + '&limit=100'
        case apiType.JOURNEY:
            startGid = getGid(start)
            endGid = getGid(end)
            urlEnd = '/journeys?originGid=' + \
                str(startGid) + '&destinationGid=' + str(endGid)
        case apiType.LOCATIONS:
            urlEnd = '/locations/by-coordinates?latitude=' + \
                str(start.latitude) + \
                '&longitude='+str(start.longitude) + \
                '&radiusInMeters=500&limit=10&offset=0'
        case _:
            print("Invalid apiType: " + apiType)
            exit()

    url = apiBaseUrlVt + urlEnd
    return requestHandler(url, vtHeaders)


def requestHandler(url: str, headers: dict) -> any:
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error in requestHandler")
        print(response.status_code)
        print(response.text)
        exit()

    data = response.json()
    print('- ' * 20)
    print("RESPONSE")
    print(json.dumps(data, indent=4, sort_keys=True))
    return data


def getGid(coordinatePair: coordinatePair) -> int:
    radius = 1000  # meters
    limit = 10
    urlEnd = '/locations/by-coordinates?latitude='+str(coordinatePair.latitude) + '&longitude=' + str(
        coordinatePair.longitude) + '&radiusInMeters=' + str(radius) + '&limit='+str(limit) + '&offset=0'
    response = requestHandler(apiBaseUrlVt + urlEnd, vtHeaders)
    closestResult = response["results"][0]
    print(closestResult)
    return closestResult.get("gid", None)


if __name__ == '__main__':
    main()
