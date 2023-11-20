import requests

url = "https://ext-api.vasttrafik.se/token"

# For Authorization under headers:
# copy-paste personal Autentiseringsnyckel from VT site 
# replace code (after Basic...) with personal Autentiseringsnyckel
headers = {
    "Content-Type": "application/x-www-form-urlencoded", 
    "Authorization": "Basic SG5lNG9DSktxQmFGWnM4MGgzbFk2TVFYY2tZYTpnUjlHWDVEUTlGbW1FaXd0cU1FRnl6ZFpTTlFh"
}

data = {
    "grant_type": "client_credentials"
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    access_token = response.json().get('access_token')
    print("Access token:", access_token)
else:
    print("Failed to retrieve access token. Status code:", response.status_code)
