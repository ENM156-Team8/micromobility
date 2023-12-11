

__all__ = ["apiCallerSos", "apiCallerVt",
           "_getCordByName", "apiCallerGoogleDirections"]


import json
import requests
from globals import coordinatePair, vtApiType, googleApiMode, sosStation

# General


def _getTokens():
    with open("apiToken.txt", "r") as apiTokenFile:
        apiTokenLines = apiTokenFile.readlines()
    vtToken = apiTokenLines[0].strip()
    sosToken = apiTokenLines[1].strip()
    googleToken = apiTokenLines[2].strip()
    return {"vt": vtToken, "sos": sosToken, "google": googleToken}


def getMapsToken():
    with open("apiToken.txt", "r") as apiTokenFile:
        apiTokenLines = apiTokenFile.readlines()
    mapsToken = apiTokenLines[2].strip()
    return mapsToken


apiBaseUrlVt = 'https://ext-api.vasttrafik.se/pr/v4'
tokens = _getTokens()
appIdSos = tokens.get("sos", '')
accessTokenVt = tokens.get("vt", '')
accessTokenGoogle = tokens.get("google", '')
vtHeaders = {
    'Authorization': 'Bearer ' + accessTokenVt
}


def _requestHandler(url: str, headers: dict) -> any:
    response = requests.get(url, headers=headers)
    # the coordinates are percieved as identical
    if response.status_code == 400 and response.json().get("errorCode") == 2020:
        return (-1)
    if response.status_code != 200:
        print("Error in requestHandler")
        print(response.status_code)
        print(response.text)
        print(url)
        print(headers)
        exit()

        errorData = {
            "url": url,
            "statusCode": response.status_code,
            "message": json.loads(response.text)['fault']['message'],
            "description": json.loads(response.text)['fault']['description']
        }
        raise Exception(errorData)

    data = response.json()
    # print('- ' * 20)
    # print("RESPONSE")
    # print(json.dumps(data, indent=4, sort_keys=True))
    return data


# Styr och Ställ

def apiCallerSos(center: coordinatePair) -> [sosStation]:
    radius = 500  # meters
    url = 'https://data.goteborg.se/SelfServiceBicycleService/v2.0/Stations/' + appIdSos + '?getclosingperiods=500&latitude=' + \
        str(center.latitude) + '&longitude=' + str(center.longitude) + \
        '&radius=' + str(radius) + '&format=json'
    response = _requestHandler(url, {})
    return formatResponseSos(response)


def formatResponseSos(jData):
    stations = []
    for n in jData:
        newStation = sosStation(
            n['Name'], n['Lat'], n['Long'], n['Distance'], n['IsOpen'], n['AvailableBikes'])
        stations.append(newStation)
    return stations

# Västtrafik


def apiCallerVt(start: coordinatePair, end: coordinatePair, apiType: vtApiType) -> str:
    match apiType:
        case apiType.POSITIONS:
            urlEnd = '/positions?lowerLeftLat=' + str(start.latitude) + '&lowerLeftLong=' + str(
                start.longitude) + '&upperRightLat=' + str(end.latitude) + '&upperRightLong=' + str(end.longitude) + '&limit=100'
        case apiType.JOURNEY:
            startGid = _getGid(start)
            endGid = _getGid(end)
            urlEnd = '/journeys?originGid=' + \
                str(startGid) + '&destinationGid=' + \
                str(endGid)
        case apiType.BIKEJOURNEY:
            startGid = _getGid(start)
            endGid = _getGid(end)
            urlEnd = '/journeys?originGid=' + \
                str(startGid) + '&destinationGid=' + \
                str(endGid) + "&transportModes=bike"
        case apiType.WALKJOURNEY:
            startGid = _getGid(start)
            endGid = _getGid(end)
            urlEnd = '/journeys?originGid=' + \
                str(startGid) + '&destinationGid=' + \
                str(endGid) + "&transportModes=walk"
        case apiType.TRAMJOURNEY:
            startGid = _getGid(start)
            endGid = _getGid(end)
            urlEnd = '/journeys?originGid=' + \
                str(startGid) + '&destinationGid=' + \
                str(endGid) + '&transportModes=tram'
        case apiType.LOCATIONS:
            urlEnd = '/locations/by-coordinates?latitude=' + \
                str(start.latitude) + \
                '&longitude='+str(start.longitude) + \
                '&radiusInMeters=500&limit=10&offset=0'
        case _:
            print("Invalid apiType: " + apiType)
            exit()

    url = apiBaseUrlVt + urlEnd
    return _requestHandler(url, vtHeaders)


# call api with name of station
def _apiCallerVtByName(station: str) -> coordinatePair:
    urlEnd = '/locations/by-text?q=' + station + '&limit=10&offset=0'
    url = apiBaseUrlVt + urlEnd
    return _requestHandler(url, vtHeaders)


def _getCordByName(station: str) -> coordinatePair:
    data = _apiCallerVtByName(station)
    lat = data.get("results")[0].get("latitude")
    long = data.get("results")[0].get("longitude")
    return coordinatePair(lat, long)


# call api with name of station
def _apiCallerVtByName(station: str) -> coordinatePair:
    urlEnd = '/locations/by-text?q=' + station + '&limit=10&offset=0'
    url = apiBaseUrlVt + urlEnd
    return _requestHandler(url, vtHeaders)


def _getCordByName(station: str) -> coordinatePair:
    data = _apiCallerVtByName(station)
    lat = data.get("results")[0].get("latitude")
    long = data.get("results")[0].get("longitude")
    return coordinatePair(lat, long)

# Helper to get station id


def _getGid(coordinatePair: coordinatePair) -> int:
    radius = 1000  # meters
    limit = 10
    urlEnd = '/locations/by-coordinates?latitude='+str(coordinatePair.latitude) + '&longitude=' + str(
        coordinatePair.longitude) + '&radiusInMeters=' + str(radius) + '&limit='+str(limit) + '&offset=0'
    response = _requestHandler(apiBaseUrlVt + urlEnd, vtHeaders)
    closestResult = response["results"][0]
    # print(closestResult)
    for result in response["results"]:
        if result.get("gid", None) != None:
            closestResult = result
            return closestResult.get("gid")
    print("no valid gid found")
    print(response)
    exit()
    return -1


def apiCallerGoogleDirections(start: coordinatePair, end: coordinatePair, mode: googleApiMode = None):
    url = ""
    # print(mode)
    if mode is None:
        url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
    else:
        match mode:
            case mode.WALK:
                url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&mode=walking&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'

            case mode.BICYCLING:
                url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&mode=bicycling&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'

            case mode.TRANSIT:
                url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&mode=transit&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'

            case mode.DRIVE:
                url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'

            case _:
                raise ValueError(f'Unsupported transport mode: {mode}')

    # print(url)
    response = requests.get(url)
    data = response.json()
    # print('- ' * 20)
    # print("RESPONSE")
    # print(json.dumps(data, indent=4, sort_keys=True))
    return data
