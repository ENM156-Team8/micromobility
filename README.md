# Västtrafik-Micromobility

### Run dev enviroment
**Windows:**
Execute the following commands, or simply run the included run.bat file
```batch
pip install -r WebApp/requirements.txt
python WebApp/webApp.py
```

**Linux:**
Execute the following commands, or simply run the included run.sh file
```bash
pip install -r WebApp/requirements.txt
python3 WebApp/webApp.py
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
