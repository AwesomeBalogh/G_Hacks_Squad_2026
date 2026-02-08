import numpy as np 

def cartesian_sphere():
    fg = 126.6901
    dg = 168.5144
    u = 3.8126

    d = (1712018.966, -328266.81849, 5179160.122)
    f = (, , ,) 
    fd = np.array(f - d)
    mag_fd = np.linalg.norm(fd)

    delta_h = (d[0] - f[0])
    delta_k = (d[1] - f[1])

    t = np.arcsin((delta_h + delta_k) / (2**0.5(fg + dg)) - numpy.pi / 4 

    G = numpy.array((d[0] + dg * (numpy.cos(t)), d[1] * (numpy.sin(t))

    return G 

    

    


                                     
                                     



