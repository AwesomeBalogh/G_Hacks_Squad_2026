import numpy as np
import math
import geo_to_cart
import cart_to_geo

def deg_to_rad(deg):
    return deg * math.pi / 180

def local_cart_to_geo_ecef(x_e, y_e, z_e, ref_lon, ref_lat, ref_h, a=6378137, f=1/298.257223563):
    """Local Cartesian offsets (m) to full ECEF on same ellipsoid.
    Assumes small offsets; approx via ref ECEF translation."""

    ref_X, ref_Y, ref_Z = geo_to_cart.geo_to_cart(ref_lat, ref_lon, ref_h)
    X = ref_X + x_e
    Y = ref_Y + y_e
    Z = ref_Z + z_e
    return X, Y, Z

def helmert_transform(XYZ_in, tx, ty, tz, rx, ry, rz, s):
    """7-param Helmert: NAD83 ECEF -> WGS84 ECEF (m, arcsec, ppm)."""

    XYZ = np.array(XYZ_in)
    R = np.array([
        [1,     rz*math.pi/648000, -ry*math.pi/648000],
        [-rz*math.pi/648000, 1,     rx*math.pi/648000],
        [ry*math.pi/648000, -rx*math.pi/648000, 1]
    ])  # Rotation matrix (arcsec to rad)
    scale_mat = np.eye(3) * (1 + s / 1e6)
    XYZ_out = np.dot(scale_mat @ R, XYZ) + np.array([tx, ty, tz])
    return XYZ_out

def local_cart_to_global(x_local, y_local, z_local, ref_lon, ref_lat, ref_h=0):
    """
    Local Cartesian (X,Y,Z m) on NAD83 (GRS80) to global WGS84 ECEF.
    NAD83 params from NGS; ~1m accuracy.[web:21]
    """
    # GRS80 (NAD83): a=6378137m, f=1/298.257222101
    a_grs80, f_grs80 = 6378137.0, 1/298.257222101
    ref_Xn, ref_Yn, ref_Zn = geo_to_cart.geo_to_cart(ref_lat, ref_lon, ref_h)
    
    # Local offsets to NAD83 ECEF
    Xn = ref_Xn + x_local
    Yn = ref_Yn + y_local
    Zn = ref_Zn + z_local
    
    # Helmert params NAD83(2011)->WGS84(G2139) approx (NGS historical)
    tx, ty, tz = 0.000, 0.000, 1.310  # m
    rx, ry, rz = 0.060, 0.000, 0.010  # arcsec
    s = -0.89  # ppm
    
    Xw, Yw, Zw = helmert_transform([Xn, Yn, Zn], tx, ty, tz, rx, ry, rz, s)
    return Xw, Yw, Zw

# Example Calgary
if __name__ == "__main__":
    print("NAD83 Local Cart to WGS84 ECEF")
    x = float(input("Local X (m): "))
    y = float(input("Local Y (m): "))
    z = float(input("Local Z (m): "))
    lon = float(input("Ref Lon (deg): "))
    lat = float(input("Ref Lat (deg): "))
    h = float(input("Ref H (m, default 0): ") or "0")
    
    Xw, Yw, Zw = local_cart_to_global(x, y, z, lon, lat, h)
    print(f"WGS84: X={Xw:.3f}, Y={Yw:.3f}, Z={Zw:.3f} m")
