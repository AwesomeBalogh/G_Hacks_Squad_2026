import sys
import parser
import geo_to_global_cart
import local_bearing_to_enu
import local_to_global

# #BESTPOSA,USB1,0,51.5,FINESTEERING,2404,603797.000,03000800,cdba,18018;SOL_COMPUTED,NARROW_INT,51.07899643518,-114.13251416136,1114.2977,-16.6000,WGS84,0.0079,0.0056,0.0141,"3920",1.000,0.000,34,31,31,30,00,21,7f,37*a5cec5c7
print("Paste log line: ")
print("NOTE: You need to press Ctrl+Z (Ctrl+D on linux) to continue instead of enter")
data = sys.stdin.read()
print()
A_geo = [
    float(parser.get_log_data("lat", data)),
    float(parser.get_log_data("lon", data)),
    float(parser.get_log_data("height", data))
]
A_cart = geo_to_global_cart.geo_to_cart(A_geo[0], A_geo[1], A_geo[2])
print(f"A is {A_cart}")

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
print(B_offset_cart)
B = B_offset_cart + A_cart
print(f"B is {B}")

Clue_2 = [-74.7377, -69.2944, -76.4427]
C = B + Clue_2 
print(f"C is {C}")


