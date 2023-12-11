from enum import Enum


class coordinatePair:
    def __init__(self, latitude: int, longitude: int):
        self.latitude = latitude
        self.longitude = longitude

    def show(self):
        return f'{self.latitude, self.longitude}'
    def __str__(self):
        return "Lat: " + str(self.latitude) + ", Long: " + str(self.longitude)
    
    def to_dict(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude
        }

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


class trip:
    def __init__(self, waypoints: list, duration: int):
        self.waypoints = waypoints
        self.duration = duration

    def to_dict(self):
        return {
            'waypoints': [waypoint.to_dict() for waypoint in self.waypoints],
            'duration': self.duration
        }

class waypoint:
    def __init__(self, start: str, destination: str, mode, duration: int, distance: int, line: tuple):
        self.start = start
        self.destination = destination
        self.mode = mode
        self.duration = duration
        self.distance = distance
        self.line = line
    
    def to_dict(self):
        return {
            'start': self.start,
            'destination': self.destination,
            'mode': self.mode,
            'duration': self.duration,
            'distance': self.distance,
            'line': self.line
        }


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

