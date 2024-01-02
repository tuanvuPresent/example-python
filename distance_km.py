def distance_km(coordinate1, coordinate2):
    R = 6373.0
    lat1, lon1 = radians(coordinate1[0]), radians(coordinate1[1])
    lat2, lon2 = radians(coordinate2[0]), radians(coordinate2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
