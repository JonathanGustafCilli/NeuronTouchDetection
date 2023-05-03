from basics.Cube import Cube
from plotter import Plot
import numpy as np
from algorithms.snudda.Hypervoxel import Hypervoxel
import time
'''
SE_F = Cube(0, 0, 0, s)
    SW_F = Cube(s, 0, 0, s)
    NE_F = Cube(0, s, 0, s)
    NW_F = Cube(s, s, 0, s)
    SE_B = Cube(0, 0, s, s)
    SW_B = Cube(s, 0, s, s)
    NE_B = Cube(0, s, s, s)
    NW_B = Cube(s, s, s, s)
'''
def touch_detection(neurons):
    
    start = time.time()
    
    print("Starting")
    
    s = 252
    hypervoxels = [
        Hypervoxel(Cube(0-s, 0-s, 0-s, s)),
        Hypervoxel(Cube(0, 0-s, 0-s, s)),
        Hypervoxel(Cube(0-s, 0, 0-s, s)),
        Hypervoxel(Cube(0, 0, 0-s, s)),
        Hypervoxel(Cube(0-s, 0-s, 0, s)),
        Hypervoxel(Cube(0, 0-s, 0, s)),
        Hypervoxel(Cube(0-s, 0, 0, s)),
        Hypervoxel(Cube(0, 0, 0, s))
    ]

    print("Hypervoxoling")
    for hypervoxel in hypervoxels:
        i = 0
        for neuron in neurons:
            found = False
            for dendrite in neuron.get_dendrites():
                if found: break
                if hypervoxel.boundary.contains([dendrite[1], dendrite[2], dendrite[3]]):
                    hypervoxel.insert(i)
                    found = True
            if not found:
                for axon in neuron.get_axons():
                    if found: break
                    if hypervoxel.boundary.contains([axon[1], axon[2], axon[3]]):
                        hypervoxel.insert(i)
                        found = True
            i += 1    
    
    print("Querying")
    synapses = []
    for hypervoxel in hypervoxels:
        voxels = np.zeros(shape=(85,85,85))
        for neuron_id in hypervoxel.neuron_IDs:
            for dendrite in neurons[neuron_id].get_dendrites():
                if hypervoxel.boundary.contains([dendrite[1], dendrite[2], dendrite[3]]): 
                   voxels[int(abs(dendrite[1])/3),int(abs(dendrite[2])/3),int(abs(dendrite[3])/3)] = 1 
        for neuron_id in hypervoxel.neuron_IDs:
            for axon in neurons[neuron_id].get_axons():
                if hypervoxel.boundary.contains([axon[1], axon[2], axon[3]]): 
                    if voxels[int(abs(axon[1])/3),int(abs(axon[2])/3),int(abs(axon[3])/3)] == 1: 
                       synapses.append([axon[1],axon[2],axon[3]])
    
    print("Time:",(time.time()-start)/60)
    print(len(synapses))
    return synapses
    