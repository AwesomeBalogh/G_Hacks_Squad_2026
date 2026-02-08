import math
from typing import List, Tuple, Optional

Vec3 = Tuple[float, float, float]
Vec2 = Tuple[float, float]

def spheres_xy_solutions_given_z(
    F: Vec3, rF: float,
    D: Vec3, rD: float,
    z: float,
    eps: float = 1e-12
) -> List[Vec2]:
    """
    Given two spheres:
        (x-xF)^2 + (y-yF)^2 + (z-zF)^2 = rF^2
        (x-xD)^2 + (y-yD)^2 + (z-zD)^2 = rD^2

    Solve for intersection points (x,y) in the plane at the specified z.

    Returns:
        A list of 0, 1, or 2 (x,y) solutions.

    Notes:
      - If the plane z does not cut a sphere, that sphere contributes no circle -> no solutions.
      - If the two circles do not intersect (or are coincident), returns [] (or handles tangent as 1 point).
    """

    xF, yF, zF = F
    xD, yD, zD = D

    # --- Reduce each sphere to a circle at height z ---
    # Circle radii in XY at this z:
    # (x-xc)^2 + (y-yc)^2 = r^2 - (z-zc)^2
    RF2 = rF * rF - (z - zF) * (z - zF)
    RD2 = rD * rD - (z - zD) * (z - zD)

    if RF2 < -eps or RD2 < -eps:
        return []  # plane misses at least one sphere

    RF = math.sqrt(max(0.0, RF2))
    RD = math.sqrt(max(0.0, RD2))

    # --- Solve circle-circle intersection in XY ---
    dx = xD - xF
    dy = yD - yF
    d = math.hypot(dx, dy)

    # Same centers (degenerate)
    if d < eps:
        # If radii match, infinite intersections (coincident circles) -> ambiguous
        # If radii differ, none.
        return []

    # No intersection cases
    if d > RF + RD + eps:
        return []  # too far apart
    if d < abs(RF - RD) - eps:
        return []  # one circle inside the other

    # Distance from F-center to the line-of-centers intersection point
    a = (RF*RF - RD*RD + d*d) / (2.0 * d)

    # Height from that point to each intersection point
    h2 = RF*RF - a*a
    if h2 < -eps:
        return []
    h = math.sqrt(max(0.0, h2))

    # Base point P along the line from F to D
    xP = xF + a * dx / d
    yP = yF + a * dy / d

    # Perpendicular unit vector
    rx = -dy / d
    ry =  dx / d

    # Tangent (one solution) if h ≈ 0
    if h < eps:
        return [(xP, yP)]

    # Two intersection points
    sol1 = (xP + h * rx, yP + h * ry)
    sol2 = (xP - h * rx, yP - h * ry)
    return [sol1, sol2]


# (Optional) helper to *print* the two sphere equations as strings:
def sphere_equations(F: Vec3, rF: float, D: Vec3, rD: float) -> Tuple[str, str]:
    xF, yF, zF = F
    xD, yD, zD = D
    eqF = f"(x-{xF})^2 + (y-{yF})^2 + (z-{zF})^2 = {rF}^2"
    eqD = f"(x-{xD})^2 + (y-{yD})^2 + (z-{zD})^2 = {rD}^2"
    return eqF, eqD
