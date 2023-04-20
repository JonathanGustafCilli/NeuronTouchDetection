import random
import math
import numpy as np

def create_rpl(n):
    brain_cube_length = 200
    rpl = []
    for i in range(n):
        # Translation:
        t_x = random.randint(-(brain_cube_length/2)-1,(brain_cube_length/2)-1)
        t_y = random.randint(-(brain_cube_length/2)-1,(brain_cube_length/2)-1)
        t_z = random.randint(-(brain_cube_length/2)-1,(brain_cube_length/2)-1)
        # Rotation:
        v_x = 2*math.pi*random.uniform(0, 1)
        v_y = 2*math.pi*random.uniform(0, 1)
        v_z = 2*math.pi*random.uniform(0, 1)
        rpl.append([i,t_x,t_y,t_z,v_x,v_y,v_z])
    return rpl

#f = open("rpl.txt", "w")
#f.write(f"{i} {t_x} {t_y} {t_z} {v_x} {v_y} {v_z}\n")
#f.close()