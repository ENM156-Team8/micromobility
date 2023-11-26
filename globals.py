from enum import Enum


class coordinatePair:
    def __init__(self, latitude: int, longitude: int):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return "Lat: " + str(self.latitude) + ", Long: " + str(self.longitude)
    
    def to_dict(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude
        }


# Enums used to fetch different data from vtApi
# POSITIONS: Returns journey positions within a bounding box
# JOURNEY: Returns journeys matching the specified search parameters
# LOCATIONS: Returns locations matching the specified text (stop areas, addresses, points of interest and meta-stations)
vtApiType = Enum(
    'vtApiType', ['POSITIONS', 'JOURNEY', 'LOCATIONS', 'BIKEJOURNEY', 'WALKJOURNEY'])
