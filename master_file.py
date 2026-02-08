import geo_to_global_cart
import local_bearing_to_enu
import local_to_global

A_geo = [float(input("Input Latitude: ")), float(input("Input Longditude: ")), float(input("Input h: "))]
A_cart = geo_to_global_cart.geo_to_cart(A_geo[0], A_geo[1], A_geo[2])

# Clue 1 in bearing, distance, and delta h
Clue_1 = [153.371958, 128.5967, -3.7103] 
B_offset_enu = local_bearing_to_enu.bearing_to_enu(
    Clue_1[0], 
    Clue_1[1], 
    Clue_1[2]
)
B_offset_cart = local_to_global.local_to_global_cart(
    B_offset_enu[0], 
    B_offset_enu[1], 
    B_offset_enu[2], 
    A_geo[0],
    A_geo[1],
    A_geo[2]
)
B = B_offset_cart + A_cart
print(B)