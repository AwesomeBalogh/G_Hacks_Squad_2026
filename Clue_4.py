import numpy as np


def pointE_from_pointD(D, P):
    """
    Solve Point E from:
      - Point D (ED, ND, UD)
      - Point P (EP, NP)
      - bearing D->E (deg, clockwise from North)
      - bearing E->P (deg, clockwise from North)
      - deltaU from D->E (meters)

    Returns: (EE, NE, UE)
    """
    northing_easting = [-505.2385, 36.3253]
    bearing_DE = 246.102478
    deltaU_DE = 1.1277  # meters

    ND = D[0]
    ED = D[1]
    UD = D[2]

    northed_p = P[0]  # P's Northing
    easted_p = P[1]  # P's Easting

    thetaD = np.radians(bearing_DE)  # bearing D->E in radians
    thetaP = np.radians(139.361144)

    # Differences from D to P in local East/North
    dE = easted_p - ED
    dN = northed_p - ND

    # Calculate t (the scalar to reach E from D along bearing DE)
    # t = (dE * np.cos(thetaP) - dN * np.sin(thetaP)) / (np.sin(thetaD - thetaP))
    t = (np.sin(thetaP) * dN - np.cos(thetaP) * dE) / (
        np.sin(thetaP) * np.cos(thetaD) - np.cos(thetaP) * np.sin(thetaD)
    )
    # Compute E's horizontal coordinates from point D
    EE = ED + t * np.sin(thetaD)
    NE = ND + t * np.cos(thetaD)

    # Apply vertical change
    UE = UD + deltaU_DE
    NEU_POINTE = np.array([NE, EE, UE])
    return NEU_POINTE


def E2D(D, P):
    bearingDE = np.radians(246.102478)
    bearingEP = np.radians(139.361144)
    h = 1.1277
    p_easting = 36.3253
    p_northing = -505.2385

    dw = P[0] - D[0]
    pw = P[1] - D[1]
    pd = np.sqrt(dw**2 + pw**2)

    theta_p = np.arctan2(pw, pd)
    beta = np.pi - (np.pi / 2) - theta_p

    c = bearingDE - (np.pi / 2) - beta
    q = (2 * np.pi) - bearingEP - theta_p
    omega = (np.pi) - c - q

    b = np.sin(q) * (pd / np.sin(omega))
    fish = np.sqrt(b**2 - h**2)
    N = fish * np.sin(np.pi - bearingDE)
    E = fish * np.cos(np.pi - bearingDE)
    U = h
    return [N, E, U]


# Example usage (replace with your real numbers)
if __name__ == "__main__":
    D = [1718425.41502, -3278870.9388, 5179417.611987]
    P = [-505.2385, 36.3253, 0]  # Example P coordinates
    print("Point E Coordinates (N, E, U):", pointE_from_pointD(D, P))
