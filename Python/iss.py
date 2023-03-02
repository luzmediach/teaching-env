from math import radians, degrees, sin, cos, asin, acos, sqrt
import time, json, urllib.request

def iss_location():
    """ 
        call opennotify api
        returns list of [lat, lon time]
    """
    response = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
    mydata = response.read()
    iss = str(mydata,'utf-8')
    pos = json.loads(iss)
    lat = pos['iss_position']['latitude']
    lon = pos['iss_position']['longitude']
    timest = pos['timestamp']
    return [float(lat),float(lon), int(timest)]


def great_circle(coord1, coord2, height=0):
    """
        coord = [lat, lon]
        height = height above 0 in km , default=0
        returns distance in km
    """
    lat1, lon1 =coord1
    lat2, lon2 =coord2
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    return (6378 + height) * (acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)))