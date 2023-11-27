from enum import Enum


class coordinatePair:
    def __init__(self, latitude: int, longitude: int):
        self.latitude = latitude
        self.longitude = longitude


# Enums used to fetch different data from vtApi
# POSITIONS: Returns journey positions within a bounding box
# JOURNEY: Returns journeys matching the specified search parameters
# LOCATIONS: Returns locations matching the specified text (stop areas, addresses, points of interest and meta-stations)
vtApiType = Enum(
    'vtApiType', ['POSITIONS', 'JOURNEY', 'LOCATIONS', 'BIKEJOURNEY', 'WALKJOURNEY', 'TRAMJOURNEY'])
