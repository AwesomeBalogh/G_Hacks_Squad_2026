import numpy as np 

def cartesian_sphere(D, F):
    fg = 126.6901
    dg = 168.5144
    u = 3.8126

    fd = np.array(f - d)
    mag_fd = np.linalg.norm(fd)

    delta_h = (d[0] - f[0])
    delta_k = (d[1] - f[1])

    t = np.arcsin((delta_h + delta_k) / (2**0.5(fg + dg)) - numpy.pi / 4 )

    G = np.array((d[0] + dg * (numpy.cos(t)), d[1] * (numpy.sin(t))))

    return G 

    

    


                                     
                                     



