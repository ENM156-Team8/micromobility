
__all__ = ["apiCallerSos", "apiCallerVt"]


import requests
from globals import coordinatePair, vtApiType

# General


def getTokens():
    with open("apiToken.txt", "r") as apiTokenFile:
        apiTokenLines = apiTokenFile.readlines()
    vtToken = apiTokenLines[0].strip()
    sosToken = apiTokenLines[1].strip()
    return {"vt": vtToken, "sos": sosToken}


def getMapsToken():
    with open("apiToken.txt", "r") as apiTokenFile:
        apiTokenLines = apiTokenFile.readlines()
    mapsToken = apiTokenLines[2].strip()
    return mapsToken


apiBaseUrlVt = 'https://ext-api.vasttrafik.se/pr/v4'
tokens = getTokens()
appIdSos = tokens.get("sos", '')
accessTokenVt = tokens.get("vt", '')
vtHeaders = {
    'Authorization': 'Bearer ' + accessTokenVt
}


def requestHandler(url: str, headers: dict) -> any:
    response = requests.get(url, headers=headers)
    # the coordinates are percieved as identical
    if response.status_code == 400 and response.json().get("errorCode") == 2020:
        return (-1)
    if response.status_code != 200:
        print("Error in requestHandler")
        print(response.status_code)
        print(response.text)
        exit()

    data = response.json()
    # print('- ' * 20)
    # print("RESPONSE")
    # print(json.dumps(data, indent=4, sort_keys=True))
    return data


# Styr och Ställ

def apiCallerSos(center: coordinatePair) -> dict:
    radius = 500  # meters
    url = 'https://data.goteborg.se/SelfServiceBicycleService/v2.0/Stations/' + appIdSos + '?getclosingperiods=500&latitude=' + \
        str(center.latitude) + '&longitude=' + str(center.longitude) + \
        '&radius=' + str(radius) + '&format=json'
    return requestHandler(url, {})

# Västtrafik


def apiCallerVt(start: coordinatePair, end: coordinatePair, apiType: vtApiType) -> str:
    match apiType:
        case apiType.POSITIONS:
            urlEnd = '/positions?lowerLeftLat=' + str(start.latitude) + '&lowerLeftLong=' + str(
                start.longitude) + '&upperRightLat=' + str(end.latitude) + '&upperRightLong=' + str(end.longitude) + '&limit=100'
        case apiType.JOURNEY:
            startGid = getGid(start)
            endGid = getGid(end)
            urlEnd = '/journeys?originGid=' + \
                str(startGid) + '&destinationGid=' + \
                str(endGid)
        case apiType.BIKEJOURNEY:
            startGid = getGid(start)
            endGid = getGid(end)
            urlEnd = '/journeys?originGid=' + \
                str(startGid) + '&destinationGid=' + \
                str(endGid) + "&transportModes=bike"
        case apiType.WALKJOURNEY:
            startGid = getGid(start)
            endGid = getGid(end)
            urlEnd = '/journeys?originGid=' + \
                str(startGid) + '&destinationGid=' + \
                str(endGid) + "&transportModes=walk"
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

# Helper to get station id


def getGid(coordinatePair: coordinatePair) -> int:
    radius = 1000  # meters
    limit = 10
    urlEnd = '/locations/by-coordinates?latitude='+str(coordinatePair.latitude) + '&longitude=' + str(
        coordinatePair.longitude) + '&radiusInMeters=' + str(radius) + '&limit='+str(limit) + '&offset=0'
    response = requestHandler(apiBaseUrlVt + urlEnd, vtHeaders)

    # get closest result that is of type "stoparea"
    for result in response["results"]:
        if result["locationType"] == "stoparea":
            closestResult = result
            break

    return closestResult.get("gid", None)
