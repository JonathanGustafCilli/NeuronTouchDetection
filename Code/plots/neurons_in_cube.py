import sys
sys.path.append('../../code')
from basics.Neuron import Neuron
import main as main
from plotter import Plot
import basics.rpl_builder as rpl_builder

'''
    Plot #m neurons in a cube of size 500x500x500 micrometers 
'''

path = "../../neurons/mouse/striatum/test_neuron.swc" # path of the neuron: 
m = 5 # number of neurons:

neurons = main.generate_neurons(path, m)

plot = Plot()
plot.plot_cube(-250, -250, -250, 500, "red") # plot the boundary
plot.plot_neurons(neurons) # plot the neurons    
plot.show()