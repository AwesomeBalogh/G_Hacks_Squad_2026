import numpy as np

def bearing_to_enu(bearing_deg, distance, delta_h):
    theta = np.radians(bearing_deg)

    dN = distance * np.cos(theta)
    dE = distance * np.sin(theta)
    dU = delta_h

    return np.array([dE, dN, dU])

deg = float(input("Enter the bearing in degrees: "))
dist = float(input("Enter the distance: "))
delta_h = float(input("Enter the change in height (optional, default is 0): "))
enu_vector = bearing_to_enu(deg, dist, delta_h)
print("ENU Vector:", enu_vector)