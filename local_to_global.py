import numpy as np
import numpy.matlib
import geo_to_global_cart as g2c
import global_cart_to_geo as c2g

def local_to_global_cart(N, E, U, phi, lamda, h):
    # Build nupmy array
    global_cart = np.array([N, E, U])
    rphi = np.radians(phi)
    rlamda = np.radians(lamda)
    # Build rotation matrix
    rotation1 = [(-1 * np.sin(rphi) * np.cos(rlamda)), (-1 * np.sin(rphi) * np.sin(rlamda)), (np.cos(rphi))]
    rotation2 = [(-1 * np.sin(rlamda)), (np.cos(rlamda)), 0]
    rotation3 = [(np.cos(rphi) * np.cos(rlamda)), (np.cos(rphi) * np.sin(rlamda)), (np.sin(rphi))]
    rotation_matrix = np.transpose([rotation1, rotation2, rotation3])

    # Multiply the global cartesian vector by the rotation matrix
    local_cart = np.matmul(rotation_matrix, global_cart)
    return local_cart



if __name__ == "__main__":
    # Example usage (replace with your real numbers)
    N =  -114.9570891 # meters
    E = 57.63661089   # meters
    U = -3.7103   # meters
    phi = 51.07899643518     # degrees
    lamda = -114.13251416136  # degrees
    h = 1114.2977      # meters

    global_cartesian = local_to_global_cart(N, E, U, phi, lamda, h)
    print("Global Cartesian Coordinates (X, Y, Z):", global_cartesian)