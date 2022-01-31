from math import radians, cos, sin, asin, sqrt

def calculate_distance_based_on_lon_lat(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    https://en.wikipedia.org/wiki/Great-circle_distance

    Args:
        lon1 ([type]): [description]
        lat1 ([type]): [description]
        lon2 ([type]): [description]
        lat2 ([type]): [description]

    Returns:
        [type]: [description]
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    r = 6378137.0# Radius of earth in kilometers. Use 3956 for miles
    return c * r