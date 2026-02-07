#cartesian to geodatic conversion
import math
def cartesian_to_geodetic(x, y, z):
    # NAD83 (GRS80) ellipsoid constants
    a = 6378137.0                # semi-major axis (m)
    f = 1 / 298.257222101        # flattening (GRS80)
    b = a * (1 - f)              # semi-minor axis (m)
    e2 = 2*f - f**2              # first eccentricity squared

    # Calculate longitude
    lon = math.atan2(y, x)

    # Calculate hypotenuse from x and y
    p = math.sqrt(x**2 + y**2)

    # Initial latitude approximation
    lat = math.atan2(z, p * (1 - e2))

    # Iteratively improve latitude approximation
    for _ in range(20):
        sin_lat = math.sin(lat)
        N = a / math.sqrt(1 - e2 * sin_lat * sin_lat)
        lat_new = math.atan2(z + e2 * N * sin_lat, p)
        if abs(lat_new - lat) < 1e-12:  # radians
            lat = lat_new
            break
        lat = lat_new

    # Calculate height
    N = a / math.sqrt(1 - e2 * math.sin(lat)**2)
    h = p / math.cos(lat) - N

    # Convert radians to degrees
    lat = math.degrees(lat)
    lon = math.degrees(lon)

    return lat, lon, h

int_input = input("Enter x coordinate: ")
x = float(int_input)
int_input = input("Enter y coordinate: ")   
y = float(int_input)
int_input = input("Enter z coordinate: ")
z = float(int_input)

latitude, longitude, height = cartesian_to_geodetic(x, y, z)
print(f"Latitude: {latitude:.6f} degrees")
print(f"Longitude: {longitude:.6f} degrees")
print(f"Height: {height:.2f} meters")

