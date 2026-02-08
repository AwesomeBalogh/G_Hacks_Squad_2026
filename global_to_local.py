import numpy as np
import numpy.matlib
import geo_to_global_cart as g2c
import global_cart_to_geo as c2g

def global_cart_to_local(X, Y, Z, phi, lamda, h):
    # Build nupmy array
    global_cart = np.array([X, Y, Z])

    # Build rotation matrix
    rotation1 = [(-1 * np.sin(phi) * np.cos(lamda)), (-1 * np.sin(phi) * np.sin(lamda)), (np.cos(phi))]
    rotation2 = [(-1 * np.sin(lamda)), (np.cos(lamda)), 0]
    rotation3 = [(np.cos(phi) * np.cos(lamda)), (np.cos(phi) * np.sin(lamda)), (np.sin(phi))]
    rotation_matrix = [rotation1, rotation2, rotation3]

    # Multiply the global cartesian vector by the rotation matrix
    local_cart = np.matmul(rotation_matrix, global_cart)
    return local_cart


if __name__ == "__main__":
    print("What are the global cartesian coordinates? (X, Y, Z)")
    x = float(input("Input X: "))
    y = float(input("Input Y: "))
    z = float(input("Input Z: "))
    g = c2g.cartesian_to_geodetic(X, Y, Z)
    p = np.radians(g[0])
    l = np.radians(g[1])
    h = g[2]
    cart = global_cart_to_local(x, y, z, p, l, h)
    print(cart)