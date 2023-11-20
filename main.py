import json
import requests
import pprint
from enum import Enum

with open("apiToken.txt", "r") as apiTokenFile:
    apiTokenLines = apiTokenFile.readlines()

ACCESS_TOKEN_VT = apiTokenLines[0].strip()

apiBaseUrlVt = 'https://ext-api.vasttrafik.se/pr/v4'
appIdSos = ''
accessTokenVt = ACCESS_TOKEN_VT
vtHeaders = {
    'Authorization': 'Bearer ' + accessTokenVt
}

# Enums used to fetch different data from vtApi
# POSITIONS: Returns journey positions within a bounding box
# JOURNEY: Returns journeys matching the specified search parameters
# LOCATIONS: Returns locations matching the specified text (stop areas, addresses, points of interest and meta-stations)
vtApiType = Enum('vtApiType', ['POSITIONS', 'JOURNEY', 'LOCATIONS', 'LOCATIONSBYTEXT'])


class coordinatePair:
    def __init__(self, latitude: int, longitude: int):
        self.latitude = latitude
        self.longitude = longitude


def main():
    print("Main running")
    sosTestCord = coordinatePair(57.687274, 11.979054)
    # apiCallerSos(sosTestCord)
    vtTestCordStart = coordinatePair(57.721723, 11.974764)
    vtTestCordEnd = coordinatePair(57.737549, 12.039268)
    #apiCallerVt(vtTestCordStart, vtTestCordEnd, vtApiType.POSITIONS)
    #getGid(vtTestCordStart)
    #apiCallerVt(vtTestCordStart,vtTestCordEnd,vtApiType.LOCATIONSBYTEXT)
    #getCordByName()
    getTripByTram("Chalmers", "Korsvägen")


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
    #print(url)
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
    #print(closestResult)
    return closestResult.get("gid", None)

# lite fulkod :)
# call api with name of station 
def apiCallerVtByName(station: str) -> coordinatePair:
    urlEnd = '/locations/by-text?q=' + station + '&limit=10&offset=0'
    url = apiBaseUrlVt + urlEnd
    return requestHandler(url, vtHeaders)

def getCordByName(station: str) -> coordinatePair: # output. format json response and receive time
    data = apiCallerVtByName(station)
    lat = data.get("results")[0].get("latitude")
    long = data.get("results")[0].get("longitude")
    return coordinatePair(lat,long) 

def getTripByTram(start: str, end: str):
    data = apiCallerVt(getCordByName(start), getCordByName(end), vtApiType.JOURNEY)
    print(json.dumps(data.get("results")[0], indent=4, sort_keys=True))

    
if __name__ == '__main__':
    main()
