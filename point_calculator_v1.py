import numpy as np
import cart_local_to_cart_global
# take in origin point as cartesian
# 
def subtract_vectors(a, b):
    x = a[0] - b[0]
    z = a[1] - b[1]
    y = a[2] - b[2]
    return [x, y, z]

def add_vectors(a, b):
    x = a[0] + b[0]
    y = a[1] + b[1]
    z = a[2] + b[2]
    return [x, y, z]

def magnitude(vec):
    mag = np.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)

BearingP = 0
BearingD = 0

t = float(input("Enter value t: "))
S = float(input("Enter value S: "))
h = float(input("Enter value h: "))

# Data for AB
Nab = S * np.cos(t)
Eab = S * np.sin(t)
Rab = [Nab, Eab, h]

print("For point C")
C = [float(input("Input the first param: ")), float(input("Input the second param: ")), float(input("Input the third param: "))]
print("For point D")
D = [float(input("Input the first param: ")), float(input("Input the second param: ")), float(input("Input the third param: "))]
print("For point E")
E = [float(input("Input the first param: ")), float(input("Input the second param: ")), float(input("Input the third param: "))]
print("For point P")
P = [float(input("Input the first param: ")), float(input("Input the second param: ")), float(input("Input the third param: "))]

# Convert to global
Rab = cart_local_to_cart_global.local_cart_to_global(Rab[0], Rab[1], Rab[2], 0, 0, 0)

Rbc = add_vectors(Rab, C)

Rcd = add_vectors(Rbc, D)

a = magnitude(subtract_vectors(P, Rcd))

b = magnitude(subtract_vectors(P, E))

c = magnitude(subtract_vectors(D, E))

Rdp = subtract_vectors(Rcd, P)
a1 = magnitude(Rdp)

i = Rdp[0]
j = Rdp[1]
theta = np.arctan(i/j)

angleP = 0
angleD = BearingP
if d[0] > P[0]:
    angleP = 360 - BearingP # THIS IS HARDCODED
else:
    angleP = BearingP - 360