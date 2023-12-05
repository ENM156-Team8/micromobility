from enum import Enum


class coordinatePair:
    def __init__(self, latitude: int, longitude: int):
        self.latitude = latitude
        self.longitude = longitude

    def show(self):
        return f'{self.latitude, self.longitude}'

# Class for a Styr&Ställ station


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


# Enums used to fetch different data from vtApi
# POSITIONS: Returns journey positions within a bounding box
# JOURNEY: Returns journeys matching the specified search parameters
# LOCATIONS: Returns locations matching the specified text (stop areas, addresses, points of interest and meta-stations)
vtApiType = Enum(
    'vtApiType', ['POSITIONS', 'JOURNEY', 'LOCATIONS', 'BIKEJOURNEY', 'WALKJOURNEY', 'TRAMJOURNEY'])

# Enums to fetch different data from googleApi
# WALK: Returns directions for walking
# BICYCLING: Returns directions for bicycling
# TRANSIT: Returns directions for public transport
# DRIVE: Returns directions for driving
googleApiMode = Enum(
    'googleApiMode', ['WALK', 'BICYCLING', 'TRANSIT', 'DRIVE'])

# Enums to choose tripMode in getGoogleDirections
# WALK: Returns a walking trip
# BICYCLING: Returns bicycling trip
# VOI: Retruns Voi trip
googleTripMode = Enum(
    'googleTripMode', ['WALK', 'BICYCLING', 'VOI'])
