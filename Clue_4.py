import numpy as np

def pointE_from_pointD(D, P, bearing_DE_deg, bearing_EP_deg, deltaU_DE):
    """
    Solve Point E from:
      - Point D (ED, ND, UD)
      - Point P (EP, NP)
      - bearing D->E (deg, clockwise from North)
      - bearing E->P (deg, clockwise from North)
      - deltaU from D->E (meters)

    Returns: (EE, NE, UE)
    """
    ED, ND, UD = D
    EP, NP = P

    # Convert bearings to radians
    thetaD = np.radians(bearing_DE_deg)

    # Convert E->P bearing to P->E bearing by adding 180 degrees
    thetaP = np.radians((bearing_EP_deg + 180.0) % 360.0)

    # Differences from D to P in local East/North
    dE = EP - ED
    dN = NP - ND

    # Solve for t (distance along D->E ray)
    denom = np.sin(thetaD - thetaP)
    if abs(denom) < 1e-12:
        raise ValueError("Bearings are parallel or nearly parallel; no stable intersection.")

    t = (dE * np.cos(thetaP) - dN * np.sin(thetaP)) / denom

    # Compute E's horizontal coordinates from point D
    EE = ED + t * np.sin(thetaD)
    NE = ND + t * np.cos(thetaD)

    # Apply vertical change last
    UE = UD + deltaU_DE

    return EE, NE, UE


# Example usage (replace with your real numbers)
if __name__ == "__main__":
    # Point D (E, N, U)
    D = (0.0, 0.0, 0.0)  # <-- replace

    # Point P (E, N)
    P = (36.3253, -505.2385)

    bearing_DE = 246.102478  # deg
    bearing_EP = 139.361144  # deg
    deltaU_DE = 1.1277       # m

    EE, NE, UE = pointE_from_pointD(D, P, bearing_DE, bearing_EP, deltaU_DE)
    print("Point E:")
    print(f"E = {EE:.4f} m")
    print(f"N = {NE:.4f} m")
    print(f"U = {UE:.4f} m")
