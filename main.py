import requests
import json


with open("api-token.txt", "r") as apiTokenFile:
    apiTokenLines = apiTokenFile.readlines()


API_BASE_URL_VT = 'https://ext-api.vasttrafik.se/pr/v4'
ACCESS_TOKEN_VT = apiTokenLines[0].strip()
APPID_SOS = apiTokenLines[1].strip()


def main():
    print("Hello World!")
    #get_sos()
    


def get_sos():
    r = requests.get('https://data.goteborg.se/SelfServiceBicycleService/v2.0/Stations/' + APPID_SOS + '?getclosingperiods=500&latitude=57.687274&longitude=11.979054&radius=500&format=json'
                     )
    print("test sos")
    print(r)
    print(r.json())


def get_vt():
    url = API_BASE_URL_VT + '/positions?lowerLeftLat=57.721723&lowerLeftLong=12.011882&upperRightLat=57.737549&upperRightLong=12.039268&limit=100'
    headers = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN_VT
    }
    res = requests.get(url, headers=headers)
    print("test vt")
    print(res)
    print(res.content)


if __name__ == '__main__':
    main()
