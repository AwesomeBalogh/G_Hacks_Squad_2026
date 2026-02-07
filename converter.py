import numpy as np
def geo_to_cart(lat, lon, h):
    a = 6378137  # WGS84
    e2 = 0.00669438
    lat, lon = np.radians(lat), np.radians(lon)
    sin_lat, cos_lat = np.sin(lat), np.cos(lat)
    N = a / np.sqrt(1 - e2 * sin_lat**2)
    X = (N + h) * cos_lat * np.cos(lon)
    Y = (N + h) * cos_lat * np.sin(lon)
    Z = (N * (1 - e2) + h) * sin_lat
    return X, Y, Z


print(geo_to_cart(37.7749,-122.4194, 0))