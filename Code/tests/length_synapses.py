import sys
sys.path.append('../../code')
import main as main
from basics.Neuron import Neuron
import algorithms.octree.td_octree as td_octree
import algorithms.linearsearch.td_linear_search as td_linearsearch
import algorithms.snudda.td_snudda as td_snudda


path = "../../neurons/mouse/striatum/test_neuron.swc" # path of the neuron:
neuron = Neuron(path) # <- create neuron from swc file  neurons = []
rpl = [[0,0,0,0,0,0,0],[1,100,0,0,180,0,0]]
neurons = []
for transformation in rpl:
    neuron_copy = neuron.copy() # O(n)
    neuron_copy.transform(transformation) # O(n)
    neurons.append(neuron_copy)


print("Checking octree:")
synapses = td_octree.touch_detection(neurons, 100, None, False)
print(len(synapses))
assert len(synapses) == 409
print("Test passed!")

'''
print("Checking Linear Search (this might take a while):")
synapses = []
synapses = td_linearsearch.touch_detection(neurons, False)
assert len(synapses) == 409
print("Test passed!")
'''
print("Checking Snudda:")
synapses = []
synapses = td_snudda.touch_detection(neurons)
assert len(synapses) == 409
print("Test passed!")


print("Everything passed!")