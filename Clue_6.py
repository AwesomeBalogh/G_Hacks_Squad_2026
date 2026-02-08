import numpy as np 

def cartesian_sphere(d, f):
    fg = 126.6901
    dg = 168.5144
    u = 3.8126
    
    fd = np.array(f) - np.array(d)

    delta_h = (d[0] - f[0])
    delta_k = (d[1] - f[1])

    t = np.arcsin((delta_h + delta_k) / (2**0.5 * (fg + dg))) - np.pi / 4 

    G = [d[0] + dg * (np.cos(t)), d[1] + (np.sin(t)), u]

    return G 

    

    


                                     
                                     



