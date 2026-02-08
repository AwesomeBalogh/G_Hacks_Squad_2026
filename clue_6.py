import math
from typing import List, Tuple

Vec3 = Tuple[float, float, float]
Vec2 = Tuple[float, float]

def solve_G_xy_given_z(F: Vec3, D: Vec3, z: float) -> List[Vec2]:
    """
    Solves for possible (x,y) locations of Point G given z.

    Inputs:
        F = (xF, yF, zF)   center of sphere F
        D = (xD, yD, zD)   center of sphere D
        z                 assumed height of G

    Returns:
        []                no solution
        [(x,y)]           tangent solution
        [(x1,y1),(x2,y2)] two valid solutions
    """

    # ----------------------------
    # GIVEN VALUES (from Clue 6)
    # ----------------------------
    S_FG = 126.6901   # meters
    S_DG = 168.5144   # meters
    deltaU = 3.8126   # meters

    # Adjust sphere centers vertically
    xF, yF, zF = F
    xD, yD, zD = D

    zF += deltaU
    zD += deltaU

    # ----------------------------
    # Reduce spheres to circles at z
    # ----------------------------
    RF2 = S_FG**2 - (z - zF)**2
    RD2 = S_DG**2 - (z - zD)**2

    if RF2 < 0 or RD2 < 0:
        return []  # plane does not intersect one or both spheres

    RF = math.sqrt(RF2)
    RD = math.sqrt(RD2)

    # ----------------------------
    # Circle–circle intersection
    # ----------------------------
    dx = xD - xF
    dy = yD - yF
    d = math.hypot(dx, dy)

    if d == 0:
        return []  # coincident centers → undefined

    if d > RF + RD or d < abs(RF - RD):
        return []  # no intersection

    a = (RF**2 - RD**2 + d**2) / (2 * d)
    h2 = RF**2 - a**2

    if h2 < 0:
        return []

    h = math.sqrt(h2)

    xP = xF + a * dx / d
    yP = yF + a * dy / d

    rx = -dy / d
    ry =  dx / d

    if h == 0:
        return [(xP, yP)]

    sol1 = (xP + h * rx, yP + h * ry)
    sol2 = (xP - h * rx, yP - h * ry)

    return [sol1, sol2]
