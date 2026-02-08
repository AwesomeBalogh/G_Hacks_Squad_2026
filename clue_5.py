import math

def E_to_F(E_current):
    """
    Input:
        E_current = (E, N)   # Point E in CURRENT coordinate system

    Output:
        F_current = (E, N)   # Point F in CURRENT coordinate system
    """

    # ----------------------------
    # GIVEN DATA (Clue #5)
    # ----------------------------

    # Common stations
    legacy_1 = (150.0, 225.0)
    legacy_2 = (450.0, 600.0)

    current_1 = (123.2447, 489.4949)
    current_2 = (170.0614, 1063.8712)

    # Legacy offset E → F
    dE_legacy = 33.6304
    dN_legacy = -151.2606

    # ----------------------------
    # Build similarity transform
    # ----------------------------

    # Baseline vectors
    dE_old = legacy_2[0] - legacy_1[0]
    dN_old = legacy_2[1] - legacy_1[1]

    dE_new = current_2[0] - current_1[0]
    dN_new = current_2[1] - current_1[1]

    # Scale
    s = math.hypot(dE_new, dN_new) / math.hypot(dE_old, dN_old)

    # Rotation
    theta = math.atan2(dN_new, dE_new) - math.atan2(dN_old, dE_old)

    c = math.cos(theta)
    sn = math.sin(theta)

    # 2x2 matrix A = sR
    a11 = s * c
    a12 = -s * sn
    a21 = s * sn
    a22 = s * c

    # ----------------------------
    # Transform offset (NO translation)
    # ----------------------------

    dE_curr = a11 * dE_legacy + a12 * dN_legacy
    dN_curr = a21 * dE_legacy + a22 * dN_legacy

    # ----------------------------
    # Apply offset to Point E
    # ----------------------------

    F_E = E_current[0] + dE_curr
    F_N = E_current[1] + dN_curr

    return (F_E, F_N)
