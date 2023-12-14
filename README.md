# Västtrafik-Micromobility

### Run dev enviroment
**Install Västtrafik API client:**
Download the python client from: https://developer.vasttrafik.se/apis/13/v4#, unzip and install it using the following command:

```batch
cd python-client
python setup.py install
```

If you get an error saying that there are fields missing for OpenAPI you can try the following fix:
In setup.py, replace line 29 `"pydantic >= 1.10.5, < 2",` with `    "pydantic >= 1.10.5",`

**Windows:**
Execute the following commands, or simply run the included run.bat file
```batch
cd WebApp
pip install -r requirements.txt
python webApp.py
```

**Linux:**
Execute the following commands, or simply run the included run.sh file
```bash
cd WebApp
pip install -r requirements.txt
python3 webApp.py
```

Remember to put the apiToken.txt file in /WebApp with the API tokens in this exact order:
```txt
<västtrafik_token>
<styr&ställ_token>
<googleMaps_token>
```

By default the site is opened on localhost:5000

### Dependencies
* Python 3
* pip
* Flask
* Västtrafik OpenAPI client
