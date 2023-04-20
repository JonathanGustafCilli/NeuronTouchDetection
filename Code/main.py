import numpy as np
import neuron_plotter
import rpl_builder
from neuron import Neuron
import total_search

# Path of the neuron: 
path = "../Neurons/Mouse/Striatum/test_neuron.swc"

# Taken from NeuroMorpho.org:
#path = "../Neurons/Mouse/Striatum/904s5c5CNG.swc"

# Taken from Snudda:
#path = "../Neurons/Mouse/Striatum/51-5-DE-cor-rep-ax.swc"
#path = "../Neurons/Mouse/Striatum/46-3-DE-cor-rep-ax.swc"
#path = "../Neurons/Mouse/Striatum/21-6-DE-cor-rep-ax.swc"
#path = "../Neurons/Mouse/Striatum/WT-P270-09-15ak-cor.swc"

neuron = Neuron(path) # <- create neuron from swc file  

m = 5 # <- number of neurons to place in the cube
rpl = rpl_builder.create_rpl(m) # <- generate random transformations for n number of neurons

neurons = []
for transformation in rpl:
    neuron_copy = neuron.copy() # O(n)
    neuron_copy.transform(transformation) # O(n)
    neurons.append(neuron_copy)

neuron_plotter.plot(neurons, True) # <- plot the cube with the neurons inside

#synapses = total_search.search_synapses(neurons)
#if synapses.size>0: neuron_plotter.plot_w_synapses(neurons, synapses) # <- plot the neurons + synapses
#else: print("No synapses found!")
