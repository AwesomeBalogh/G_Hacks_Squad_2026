import numpy as np

def E2D(D_offset_a, P_offset_a):
    bearingDE = np.radians(246.102478)
    bearingEP = np.radians(139.361144)
    h = 1.1277
    p_easting = 36.3253
    p_northing = -505.2385

    dw = P_offset_a[1] - D_offset_a[1]  # delta Easting (x direction)
    pw = P_offset_a[0] - D_offset_a[0]  # delta Northing (y direction)
    pd = np.sqrt(dw**2 + pw**2)         #distance betweeen flat P and D
    theta_p = np.arctan2(dw, pw)        #angle DPW in radians
    beta = np.pi - (np.pi / 2) - theta_p    #agle WDP in radians

    c = bearingDE - (np.pi / 2) - beta  #angle EDP in radians
    q = (2 * np.pi) - bearingEP - theta_p   #angle EPD in radians
    omega = (np.pi) - c - q         #angle DEP in radians

    b = np.sin(q) * (pd / np.sin(omega))    #distance between flat D and flat E
    iota = 2*np.pi - bearingDE - np.pi/2
    Easting_EtoD_offset = np.cos(iota) * b
    Northing_EtoD_offset = np.sin(iota) * b
    
    offset_etod = [Northing_EtoD_offset, Easting_EtoD_offset, h]

    a_to_e = offset_etod + D_offset_a

    North = a_to_e[0]
    East = a_to_e[1]
    Up = a_to_e[2]
    return [North, East, Up]


# Example usage (replace with your real numbers)
if __name__ == "__main__":
    D = [1718425.41502, -3278870.9388, 5179417.611987]
    P = [-505.2385, 36.3253, 0]  # Example P coordinates
    print("Point E Coordinates (N, E, U):", E2D(D, P))
