import numpy as np
import numpy.matlib
import geo_to_global_cart as g2c
import global_cart_to_geo as c2g

def local_to_global_cart(N, E, U, phi, lamda, h):
    # Build nupmy array
    global_cart = np.array([N, E, U])

    # Build rotation matrix
    rotation1 = [(-1 * np.sin(phi) * np.cos(lamda)), (-1 * np.sin(phi) * np.sin(lamda)), (np.cos(phi))]
    rotation2 = [(-1 * np.sin(lamda)), (np.cos(lamda)), 0]
    rotation3 = [(np.cos(phi) * np.cos(lamda)), (np.cos(phi) * np.sin(lamda)), (np.sin(phi))]
    rotation_matrix = np.transpose([rotation1, rotation2, rotation3])

    # Multiply the global cartesian vector by the rotation matrix
    local_cart = np.matmul(rotation_matrix, global_cart)
    return local_cart



if __name__ == "__main__":
    print("What are the global cartesian coordinates? (N, Y, Z)")
    n = float(input("Input N: "))
    e = float(input("Input E: "))
    u = float(input("Input U: "))
    g = c2g.cartesian_to_geodetic(n, e, u)
    p = np.radians(g[0])
    l = np.radians(g[1])
    h = g[2]
    cart = local_to_global_cart(n, e, u, p, l, h)
    print(cart)