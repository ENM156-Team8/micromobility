
__all__ = ["apiCallerSos", "apiCallerVt", "_getCordByName"]



import requests
from globals import coordinatePair, vtApiType
import time
import openapi_client
#from openapi_client.rest import ApiException
from pprint import pprint


# General

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

configuration = openapi_client.Configuration(
    host = "https://ext-api.vasttrafik.se/pr/v4",
    access_token = "eyJ4NXQiOiJaV05sTURNNE56SmpZelZrT1dFNU16RTFNalF5TTJaaE5XSm1ORE0zWkRVMk9HRXdOVGxqWVRjNE1tWTNPRGcwWW1JeFlqSTFPVGMzTjJWallqZzRNdyIsImtpZCI6IlpXTmxNRE00TnpKall6VmtPV0U1TXpFMU1qUXlNMlpoTldKbU5ETTNaRFUyT0dFd05UbGpZVGM0TW1ZM09EZzBZbUl4WWpJMU9UYzNOMlZqWWpnNE13X1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJ0U1RGUGF2UmkwZ2xGbFhaYmxCTkVKWVkySXNhIiwiYXV0IjoiQVBQTElDQVRJT04iLCJiaW5kaW5nX3R5cGUiOiJyZXF1ZXN0IiwiaXNzIjoiaHR0cHM6XC9cL2V4dC1hcGkudmFzdHRyYWZpay5zZVwvdG9rZW4iLCJ0aWVySW5mbyI6eyJVbmxpbWl0ZWQiOnsidGllclF1b3RhVHlwZSI6InJlcXVlc3RDb3VudCIsImdyYXBoUUxNYXhDb21wbGV4aXR5IjowLCJncmFwaFFMTWF4RGVwdGgiOjAsInN0b3BPblF1b3RhUmVhY2giOnRydWUsInNwaWtlQXJyZXN0TGltaXQiOjAsInNwaWtlQXJyZXN0VW5pdCI6bnVsbH19LCJrZXl0eXBlIjoiUFJPRFVDVElPTiIsInN1YnNjcmliZWRBUElzIjpbeyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6ImFwaTAwMTMtcHIiLCJjb250ZXh0IjoiXC9wclwvdjQiLCJwdWJsaXNoZXIiOiJhZG1pbiIsInZlcnNpb24iOiJ2NCIsInN1YnNjcmlwdGlvblRpZXIiOiJVbmxpbWl0ZWQifV0sImF1ZCI6Imh0dHBzOlwvXC9leHQtYXBpLnZhc3R0cmFmaWsuc2UiLCJuYmYiOjE3MDE2OTI4MDksImFwcGxpY2F0aW9uIjp7Im93bmVyIjoidFNURlBhdlJpMGdsRmxYWmJsQk5FSllZMklzYSIsInRpZXJRdW90YVR5cGUiOm51bGwsInRpZXIiOiJVbmxpbWl0ZWQiLCJuYW1lIjoibWljcm9tb2JpbGl0ZXQtc29zLXZ0IiwiaWQiOjE3MTksInV1aWQiOiJmOTA2MmNlMC1hZDY1LTQ3ZTUtODljNC0yMmI3MzdmZTc2OTYifSwiYXpwIjoidFNURlBhdlJpMGdsRmxYWmJsQk5FSllZMklzYSIsInNjb3BlIjoiYXBpbTpzdWJzY3JpYmUiLCJleHAiOjE3MDE3NzkyMDksImlhdCI6MTcwMTY5MjgwOSwiYmluZGluZ19yZWYiOiIzNGRhOGI4NWVlN2Y4M2UzNDE5YzU5YWY4NTVhN2E5NiIsImp0aSI6IjYyOTgxNGU1LTNjZDUtNGM4MS1iNWEyLWNiNDg5NWNhN2FmYiJ9.cPzkuiw8yOK_DTdZjygvKDwLW82QjYyAzVWGDBEuGtnHTv88hEAXBrZCq9KztQ2SyS_c57usPvlxanTn5iJxUdXNtEfNmq73wOIKtmyOArNMM4vnLdXq5W2QgPW9dyRzYMdJOerXfXJL7hdBdxIUlsbT_fd7ZK76tjbLlPhKlksjALfo9WivhcewzfUM2QFDFMhgilmOXykIBSi5_V_s5_aKoDDxxpHT0tGR1ynBJdruJsup6JSDzpvhSjrNkd6heJv4vzDFlb0qvD3rwCc_KaYkYYoUKekK8c9DtiETvP9g4nod0AGebWcx-dZKUyfqOFOZpjSOpoc-MHYbztHlVw"
)

api_client = openapi_client.api_client(configuration)
location_api = openapi_client.locations_api(api_client)
journey_api = openapi_client.journeys_api(api_client)

instance.journey_api.journeys_get(params)

#todo: read about instance openapi


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
