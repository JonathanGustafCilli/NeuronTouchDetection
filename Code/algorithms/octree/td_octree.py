import numpy as np
from basics.Cube import Cube
from algorithms.octree.Octree import Octree

'''
TOUCH DETECTION WITH OCTREE
'''

def touch_detection(neurons, capacity, ax, verbose):
    
    if verbose: print("\nDebugging Octree:")
    
    # ---- BUILD OCTREE -----
    boundary = Cube(-250,-250,-250,500)
    octree = Octree(boundary, capacity, ax)
    i = 0
    for neuron in neurons: # O(m*d)
        for dendride in neuron.get_dendrites(): # O(d)
            octree.insert([dendride[1],dendride[2],dendride[3],i])
        i += 1

    # ---- FIND SYNAPSES -----
    synapses = []
    i = 0
    if verbose: print("The Octree has been build! Now running touch detection:")
    for neuron in neurons: # O(m*a)
        for axon in neuron.get_axons(): # O(a)
            range = Cube(axon[1]-3, axon[2]-3, axon[3]-3, 6)
            octree.query(range, synapses, i) # Unsure Time Complexity
        i += 1
    return synapses
