import numpy as np
import numpy.matlib
import geo_to_global_cart as g2c
import global_cart_to_geo as c2g

def global_cart_to_local(X, Y, Z):
    # Build nupmy array
    geo = c2g.cartesian_to_geodetic(X, Y, Z)
    phi = geo[0]
    lamda = geo[1]
    h = geo[2]
    global_cart = np.array([X, Y, Z])

    # Build rotation matrix
    rotation1 = [(-1 * np.sin(phi) * np.cos(lamda)), (-1 * np.sin(phi) * np.sin(lamda)), (np.cos(phi))]
    rotation2 = [(-1 * np.sin(lamda)), (np.cos(lamda)), 0]
    rotation3 = [(np.cos(phi) * np.cos(lamda)), (np.cos(phi) * np.sin(lamda)), (np.sin(phi))]
    rotation_matrix = [rotation1, rotation2, rotation3]

    # Multiply the global cartesian vector by the rotation matrix
    local_cart = np.matmul(global_cart, rotation_matrix)
    return local_cart


if __name__ == "__main__":
    print("What are the global cartesian coordinates? (X, Y, Z)")
    cart = global_cart_to_local(float(input("Input X: ")), float(input("Input Y: ")), float(input("Input Z: ")))
    print(cart)