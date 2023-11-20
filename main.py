import json
import requests
import json
from enum import Enum

#Class for a Styr&Ställ station
class sosStation:
    def __init__(self, name, latitude, longitude, distance, open, availableBikes):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.open = open
        self.availableBikes = availableBikes

    def show(self):
        return f'{self.name, self.latitude, self.longitude, self.distance, self.open, self.availableBikes}'

#Class for a Västtrafik station
class vtStation:
    def __init__(self, name, gid, latitude, longitude, distance):
        self.name = name
        self.gid = gid
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
    
    def show(self):
        return f'{self.name,self.gid, self.latitude, self.longitude, self.distance}'

class vtPosition:
    def __init__(self, name, direction, latitude, longitude, transportMode):
        self.name = name
        self.direction = direction
        self.latitude = latitude
        self.longitude = longitude
        self.transportMode = transportMode
    def show(self):
        return f'{self.name, self.direction, self. latitude, self.longitude, self.transportMode}'

class coordinatePair:
    def __init__(self, latitude: int, longitude: int):
        self.latitude = latitude
        self.longitude = longitude



def getTokens():
    with open("apiToken.txt", "r") as apiTokenFile:
        apiTokenLines = apiTokenFile.readlines()
    vtToken = apiTokenLines[0].strip()
    sosToken = apiTokenLines[1].strip()
    return {"vt": vtToken, "sos": sosToken}


apiBaseUrlVt = 'https://ext-api.vasttrafik.se/pr/v4'
tokens = getTokens()
appIdSos = tokens.get("sos", '')
accessTokenVt = tokens.get("vt", '')
vtHeaders = {
    'Authorization': 'Bearer ' + accessTokenVt
}

# Enums used to fetch different data from vtApi
# POSITIONS: Returns journey positions within a bounding box
# JOURNEY: Returns journeys matching the specified search parameters
# LOCATIONS: Returns locations matching the specified text (stop areas, addresses, points of interest and meta-stations)
vtApiType = Enum('vtApiType', ['POSITIONS', 'JOURNEY', 'LOCATIONS'])
vtResponseType = Enum('vtResponseType', ['POSITIONS', 'JOURNEY', 'LOCATIONS'])




def main():
    print("Main running")
    sosTestCord = coordinatePair(57.687274, 11.979054)
    sosData = apiCallerSos(sosTestCord)
    vtTestCordStart = coordinatePair(57.721723, 11.974764)
    vtTestCordEnd = coordinatePair(57.737549, 12.039268)
    vtData = apiCallerVt(vtTestCordStart, vtTestCordEnd, vtApiType.LOCATIONS)
    
    # getGid(vtTestCordStart)
   
    
    # sSos1 = formatResponseSos(sosData)
    # for n in sSos1:
    #     print(n.show())

    vt = formatResponseVt(vtData, vtResponseType.LOCATIONS)
    for n in vt:
        print(n.show())
    
#Takes the response from the Styr&Ställ API and returns a list of the stations and their status. 
def formatResponseSos(jData):
    stations = []
    for n in jData:
       stations.append(sosStation(n['Name'], n['Lat'], n['Long'], n['Distance'], n['IsOpen'], n['AvailableBikes']))
    return stations
    
#Takes the response from the Västtrafik API and returns a condensed list of the wanted attributes.
#NOTE: Not finished, needs logic for the case: .JOURNEY
def formatResponseVt(jData, type:vtResponseType):
    list = []
    match type:
        case vtResponseType.LOCATIONS:
            for n in jData['results']:
                list.append(vtStation(n['name'], n['gid'], n['latitude'], n['longitude'], n['straightLineDistanceInMeters']))
            
        case vtResponseType.POSITIONS:
            for n in jData:
                list.append(vtPosition(n['name'], n['direction'], n['latitude'], n['longitude'], n['line']['transportMode']))
            
        case vtResponseType.JOURNEY:
            print("NOTE: Not implemented.")
            exit()
        
        case _:
            print("Invalid vtResponseType" + vtResponseType)
            exit()

    return list

    


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
