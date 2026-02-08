import sys
import parser
import geo_to_global_cart
import global_cart_to_geo
import local_bearing_to_enu
import local_to_global
import global_to_local
import Clue_4
import Clue_5

# BESTPOSA,USB1,0,51.5,FINESTEERING,2404,603797.000,03000800,cdba,18018;SOL_COMPUTED,NARROW_INT,51.07899643518,-114.13251416136,1114.2977,-16.6000,WGS84,0.0079,0.0056,0.0141,"3920",1.000,0.000,34,31,31,30,00,21,7f,37*a5cec5c7
print("Paste log line: ")
print("NOTE: You need to press Ctrl+Z (Ctrl+D on linux) to continue instead of enter")
data = sys.stdin.read()
print()
A_geo = [
    float(parser.get_log_data("lat", data)),
    float(parser.get_log_data("lon", data)),
    float(parser.get_log_data("height", data)),
]
A_cart = geo_to_global_cart.geo_to_cart(A_geo[0], A_geo[1], A_geo[2])
print(f"A is {A_geo}")

# Clue 1 in bearing, distance, and delta h
Clue_1 = [153.371958, 128.5967, -3.7103]
B_offset_enu = local_bearing_to_enu.bearing_to_enu(Clue_1[0], Clue_1[1], Clue_1[2])
B_offset_cart = local_to_global.local_to_global_cart(
    B_offset_enu[0], B_offset_enu[1], B_offset_enu[2], A_geo[0], A_geo[1], A_geo[2]
)
B = B_offset_cart + A_cart
B_geo = global_cart_to_geo.cartesian_to_geodetic(B[0], B[1], B[2])
print(f"B is {B_geo}")

Clue_2 = [-74.7377, -69.2944, -76.4427]
C = B + Clue_2
C_geo = global_cart_to_geo.cartesian_to_geodetic(C[0], C[1], C[2])
print(f"C is {C_geo}")

Clue_3 = [15.3513, -131.4161, -1.5663]
D_offset_cart = local_to_global.local_to_global_cart(
    Clue_3[0], Clue_3[1], Clue_3[2], C_geo[0], C_geo[1], C_geo[2]
)
D = C + D_offset_cart
D_geo = global_cart_to_geo.cartesian_to_geodetic(
    D[0],
    D[1],
    D[2],
)
print(f"D is {D_geo}")

D_offset = D - A_cart

D_neu = global_to_local.global_cart_to_local(
    D_offset[0], D_offset[1], D_offset[2], A_geo[0], A_geo[1], A_geo[2]
)
print(D_neu)

p_neu_offset = [-505.2385, 36.3253, 0]
p_cart_offset = local_to_global.local_to_global_cart(
    p_neu_offset[0], p_neu_offset[1], p_neu_offset[2], A_geo[0], A_geo[1], A_geo[2]
)
P = p_cart_offset + A_cart
P_geo = global_cart_to_geo.cartesian_to_geodetic(P[0], P[1], P[2])
P_neu = global_to_local.global_cart_to_local(
    P[0], P[1], P[2], A_geo[0], A_geo[1], A_geo[2]
)

print(D_neu)
E_neu = Clue_4.E2D(D_neu, p_neu_offset)
E_global_offset = local_to_global.local_to_global_cart(
    E_neu[0], E_neu[1], E_neu[2], A_geo[0], A_geo[1], A_geo[2]
)
E = A_cart + E_global_offset
E_geo = global_cart_to_geo.cartesian_to_geodetic(E[0], E[1], E[2])
print(f"E is {E_geo}")

F_legacy_local_offset = [-151.2606, 33.6304, -3.6288]

F_offset = Clue_5.transformation(F_legacy_local_offset)
F = E + F_offset
F_geo = global_cart_to_geo.cartesian_to_geodetic(F[0], F[1], F[2])
print(f"F is {F_geo}")


