import json
import requests
from enum import Enum


apiBaseUrlVt = 'https://ext-api.vasttrafik.se/pr/v4'
appIdSos = ''
accessTokenVt = ''
vtHeaders = {
    'Authorization': 'Bearer ' + accessTokenVt
}

vtApiType = Enum('vtApiType', ['POSITIONS', 'JOURNEY', 'LOCATIONS'])


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
    # apiCallerVt(vtTestCordStart, vtTestCordEnd, vtApiType.POSITIONS)
    getGid(vtTestCordStart)


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
