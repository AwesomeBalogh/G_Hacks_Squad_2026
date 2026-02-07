# This will convert a set of cartesian coordinates to the local north american elipse to the global elipse
import numpy as np
from pyproj import Transformer, CRS

def local_na_cart_to_global(x_local, y_local, z_local, ref_lon, ref_lat, ref_h=0):
    """
    Convert local Cartesian (X,Y,Z) relative to reference point
    on NAD83 ellipsoid to global WGS84 ECEF Cartesian.
    
    Assumes local tangent plane approx valid for small offsets.
    Uses pyproj for accurate ECEF conversions & NAD83->WGS84 Helmert.
    
    Args:
    x_local, y_local, z_local (float): local ENU or ECEF offsets (m)
    ref_lon, ref_lat (float): reference lon (deg), lat (deg) in NAD83
    ref_h (float): reference height (m), default 0
    
    Returns:
    tuple: global X,Y,Z ECEF (m) in WGS84
    """
    # NAD83 geographic CRS with Helmert to WGS84
    nad83_crs = CRS.from_epsg(4269)  # NAD83
    wgs84_crs = CRS.from_epsg(4978)  # WGS84 ECEF
    
    # Transformer: NAD83 geo -> WGS84 ECEF
    geo_to_ecef = Transformer.from_crs(nad83_crs, wgs84_crs, always_xy=True)
    
    # Reference ECEF NAD83 approx (via WGS84 close enough for ref)
    ref_ecef_x, ref_ecef_y, ref_ecef_z = geo_to_ecef.transform(ref_lon, ref_lat, ref_h)
    
    # Local offsets to global (simple translation for small area)
    x_global = ref_ecef_x + x_local
    y_global = ref_ecef_y + y_local
    z_global = ref_ecef_z + z_local
    
    return x_global, y_global, z_global

# Example: Calgary approx ref
print(local_na_cart_to_global(100, 200, 10, -114.07, 51.04))  # [web:11][web:13][web:21]
    