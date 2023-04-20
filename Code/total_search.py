from neuron import Neuron
import numpy as np
import time

'''
Variables used for defining TIME COMPLEXIY of the functions:
    m = number of neurons
    n = number of segments in a neuron (i.e. number of rows in the swc file)
    s = number of soma segments in a neuron
    d = number of dendrite segments in a neuron
    a = number of axon segments in a neuron
    Such that: n = s+d+a
'''
def search_synapses(neurons):
    start = time.time()
    len_axons = len(neurons[0].get_axons())
    len_neurons = len(neurons)
    synapses = []
    i = 0 # <- counter of number of queried neurons
    for query_neuron in neurons:
        axons = query_neuron.get_axons() # O(1)
        a = 0 # <- counter of queried axons
        print(f"Checking synapses between neuron {i} and {[x for x in range(len_neurons) if x>i]}")      
        for axon in axons: 
            j = 0 # <- counter of visited neuron 
            for other_neuron in neurons:
                if j>i:
                    dendrites = other_neuron.get_dendrites() # O(1)
                    for dendrite in dendrites: # O(d)
                        distance = np.linalg.norm(np.array([axon[1],axon[2],axon[3]])-np.array([dendrite[1],dendrite[2],dendrite[3]]))
                        if distance < 3: synapses.append([axon[1],axon[2],axon[3]])
                j += 1 
            a += 1
            if a%100==0: print(f"\rProgress: {round((a/len_axons)*100,2)}%\r", end='')
        i += 1
        print(f"Found {len(synapses)} synapses")             
    end = time.time()
    print(f"The algorithm took: {(end-start)/60} minutes and found {len(synapses)} synapses!")
    return np.array(synapses)
