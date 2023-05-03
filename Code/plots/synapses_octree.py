import sys
sys.path.append('../../code')
import main as main
from plotter import Plot
import algorithms.octree.td_octree as td_octree

'''
    Plot #m neurons in a cube of size 500x500x500 micrometers 
'''

plot = Plot()

while(True):
    path = "../../neurons/mouse/striatum/test_neuron.swc" # path of the neuron:
    neurons = main.generate_neurons(path, 3)
    synapses = td_octree.touch_detection(neurons, 100, None, False)
    if len(synapses) > 0: break

print("Tot number of synapses:",len(synapses))
plot.plot_cube(-250, -250, -250, 500, "red") # plot the boundary
plot.plot_neurons(neurons) # plot the neurons    
plot.plot_synapses(synapses) # <- plot the synapses
plot.show()