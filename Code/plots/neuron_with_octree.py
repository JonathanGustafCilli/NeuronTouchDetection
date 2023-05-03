import sys
sys.path.append('../../code')
import main as main
from plotter import Plot
import algorithms.octree.td_octree as td_octree

'''
    Plot #m neurons in a cube of size 500x500x500 micrometers 
'''

plot = Plot()

path = "../../neurons/mouse/striatum/test_neuron.swc" # path of the neuron:
neurons = main.generate_neurons(path, 1)
td_octree.touch_detection(neurons, 100, plot, True)

plot.plot_neurons(neurons) # plot the neurons    

plot.show()