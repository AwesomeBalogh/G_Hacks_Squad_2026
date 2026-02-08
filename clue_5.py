import numpy as np 

def transformation(V):
    legacy_easting = [150, 450]
    legacy_northing = [225, 600]
    current_easting = [123.2447, 170.0614]
    current_northing = [489.4949, 1063.8712]

    legacy_offset_neu = [-151.2606, 33.6304, -3.6288]

    legacy_easting_distance = legacy_easting[1] - legacy_easting[0]
    legacy_northing_distance = legacy_northing[1] - legacy_northing[0]
    legacy_distance = np.sqrt(legacy_easting_distance**2 + legacy_northing_distance**2)

    

    return V

