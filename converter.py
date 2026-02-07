# This will convert cartesian coordinates to geospacial
import numpy as np
def geo_to_cart(lat, lon, height):
    a = 6378137  # WGS84
    e = 0.00669438
    # Convert to radians
    lat_rad, lon_rad = np.radians(lat), np.radians(lon)

    N = a / np.sqrt(1 - (e * np.sin(lat_rad)**2))
    X = (N + height) * np.cos(lat_rad) * np.cos(lon_rad)
    Y = (N + height) * np.cos(lat_rad) * np.sin(lon_rad)
    Z = ((N * (1 - e**2)) + height) * np.sin(lat_rad)
    return [X, Y, Z]
