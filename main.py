import requests
import json
from ast import literal_eval


class sosStation:
    def __init__(self, name, lat, long, dist, open, availableBikes):
        self.name = name
        self.lat = lat
        self.long = long
        self.dist = dist
        self.open = open
        self.availableBikes = availableBikes

    def show(self):
        return f'{self.name, self.lat, self.long, self.dist, self.open, self.availableBikes}'
    
class vtStation:
    def __init__(self, name, gid, lat, long, dist):
        self.name = name
        self.gid = gid
        self.lat = lat
        self.long = long
        self.dist = dist
    
    def show(self):
        return f'{self.name,self.gid, self.lat, self.long, self.dist}'


with open("apiToken.txt", "r") as apiTokenFile:
    apiTokenLines = apiTokenFile.readlines()


API_BASE_URL_VT = 'https://ext-api.vasttrafik.se/pr/v4'
ACCESS_TOKEN_VT = apiTokenLines[0].strip()
APPID_SOS = apiTokenLines[1].strip()


def main():
    print("Hello World!")
    sosData = get_sos()
    sSos1 = formatResponseSos(sosData)
    for n in sSos1:
        print(n.show())
    vtData = get_vt()
    sVt1 = formatResponseVt(vtData)
    for n in sVt1:
        print(n.show())
    

def formatResponseSos(jData):
    stations = []
    for n in jData:
       stations.append(sosStation(n['Name'], n['Lat'], n['Long'], n['Distance'], n['IsOpen'], n['AvailableBikes']))
    return stations
    
def formatResponseVt(jDataStr):
    jData = json.loads(jDataStr)
    stations = []
    for n in jData["results"]:
        stations.append(vtStation(n["name"], n["gid"], n["latitude"], n["longitude"], n["straightLineDistanceInMeters"]))
    return stations



def get_sos():
    r = requests.get('https://data.goteborg.se/SelfServiceBicycleService/v2.0/Stations/' + APPID_SOS + '?getclosingperiods=500&latitude=57.687274&longitude=11.979054&radius=500&format=json'
                     )
    print("Styr och ställ")
    print(r)
    #print(r.json())
    return r.json()


def get_vt():
    url = API_BASE_URL_VT + '/locations/by-coordinates?latitude=57.708734&longitude=11.974764&radiusInMeters=500&limit=10&offset=0'
    headers = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN_VT
    }
    
    response = requests.get(url, headers=headers)
    data = literal_eval(response.content.decode('utf8'))
    jsonData = json.dumps(data, indent=4, sort_keys=True)

    print('- ' * 20)
    print("västtrafik")
    #print(jsonData)
    return jsonData


if __name__ == '__main__':
    main()
