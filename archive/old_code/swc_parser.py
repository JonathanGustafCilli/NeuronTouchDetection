import numpy as np

def get_neuron():
    neurites = []
    with open('51-5-DE-cor-rep-ax.swc','r') as file:
        for l in file:
            l = l.split()
            neurites.append([int(l[1]),float(l[2]),float(l[3]),float(l[4]),float(l[5])])
    return np.array(neurites)
     