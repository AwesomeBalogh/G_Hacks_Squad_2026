import numpy as np

def pointE_from_pointD(D):
    """
    Solve Point E from:
      - Point D (ED, ND, UD)
      - Point P (EP, NP)
      - bearing D->E (deg, clockwise from North)
      - bearing E->P (deg, clockwise from North)
      - deltaU from D->E (meters)

    Returns: (EE, NE, UE)
    """
    ND = D[0]
    ED = D[1]
    UD = D[2]

    NP = ND -505.2385  # P's Northing
    EP = ED + 36.3253  # P's Easting
    thetaD = np.radians(246.102478) # bearing D->E in radians
    thetaP = np.radians((139.361144 + 180.0) % 360.0) # bearing P->E in radians
    deltaU_DE = 1.1277  # meters

    # Differences from D to P in local East/North
    dE = EP - ED
    dN = NP - ND

    # Calculate t (the scalar to reach E from D along bearing DE)
    t = (dE * np.cos(thetaP) - dN * np.sin(thetaP)) / (np.sin(thetaD - thetaP))

    # Compute E's horizontal coordinates from point D
    EE = ED + t * np.sin(thetaD)
    NE = ND + t * np.cos(thetaD)

    # Apply vertical change
    UE = UD + deltaU_DE
    NEU_POINTE = np.array([NE, EE, UE])
    return NEU_POINTE


# Example usage (replace with your real numbers)
if __name__ == "__main__":
    D = [1718425.41502, -3278870.9388, 5179417.611987]
    print ("Point E Coordinates (N, E, U):", pointE_from_pointD(D))

