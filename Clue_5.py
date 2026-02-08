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
    legacy_angle = np.arctan2(legacy_northing_distance, legacy_easting_distance)

    current_northing_distance = current_northing[1] - current_northing[0]
    current_easting_distance = current_easting[1] - current_easting[0]
    current_distance = np.sqrt(current_easting_distance**2 + current_northing_distance**2)
    current_angle = np.arctan2(current_northing_distance, current_easting_distance)

    scale = current_distance / legacy_distance
    rotation = current_angle - legacy_angle
    rotation_deg = np.rad2deg(rotation)

    s_cos = scale * np.cos(rotation)
    s_sin = scale * np.sin(rotation)

    x_rotation = legacy_easting[0] * s_cos - legacy_northing[0] * s_sin
    y_rotation = legacy_easting[0] * s_sin - legacy_northing[0] * s_cos

    x_translation = current_easting[0] - x_rotation
    y_translation = current_northing[0] - y_rotation

    N_final = scale * (V[1] * np.cos(rotation) - V[0] * np.sin(rotation))
    E_final = scale * (V[1] * np.sin(rotation) + V[0] * np.cos(rotation))
    

    return [N_final, E_final, V[2]]

