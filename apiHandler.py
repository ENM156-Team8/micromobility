
__all__ = ["apiCallerSos", "apiCallerVt", "_getCordByName", "apiCallerGoogleDirections"]



import requests
from globals import coordinatePair, vtApiType, googleApiMode

# General

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
        case apiType.TRAMJOURNEY:
            startGid = getGid(start)
            endGid = getGid(end)
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
    return requestHandler(url, vtHeaders)


# call api with name of station 
def _apiCallerVtByName(station: str) -> coordinatePair:
    urlEnd = '/locations/by-text?q=' + station + '&limit=10&offset=0'
    url = apiBaseUrlVt + urlEnd
    return requestHandler(url, vtHeaders)


def _getCordByName(station: str) -> coordinatePair: 
    data = _apiCallerVtByName(station)
    lat = data.get("results")[0].get("latitude")
    long = data.get("results")[0].get("longitude")
    return coordinatePair(lat,long) 

# Helper to get station id

def getGid(coordinatePair: coordinatePair) -> int:
    radius = 1000  # meters
    limit = 10
    urlEnd = '/locations/by-coordinates?latitude='+str(coordinatePair.latitude) + '&longitude=' + str(
        coordinatePair.longitude) + '&radiusInMeters=' + str(radius) + '&limit='+str(limit) + '&offset=0'
    response = requestHandler(apiBaseUrlVt + urlEnd, vtHeaders)
    closestResult = response["results"][0]
    # print(closestResult)
    return closestResult.get("gid", None)

#Google

def apiCallerGoogleDirections(start:coordinatePair, end:coordinatePair, mode: googleApiMode=None):
    url = ""
    if mode is None:
        url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
    else:
        match mode:
            case mode.WALK:
                url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&mode=walk&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
            
            case mode.BICYCLING:
                url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&mode=bicycling&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
            
            case mode.TRANSIT:
                url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&mode=transit&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
            
            case mode.DRIVE:
                url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start.latitude},{start.longitude}&destination={end.latitude},{end.longitude}&key={accessTokenGoogle}'
            
            case _: 
                raise ValueError(f'Unsupported transport mode: {mode}')
    
    #print(url)
    response = requests.get(url)
    data = response.json()
    # print('- ' * 20)
    # print("RESPONSE")
    # print(data, indent=4, sort_keys=True)
    return data

