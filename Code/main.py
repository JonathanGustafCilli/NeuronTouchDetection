import numpy as np
import neuron_plotter
import rpl_builder
from neuron import Neuron

# Path of the neuron: 
#path = "../Neurons/test.swc"
path = "../Neurons/Mouse/Striatum/904s5c5CNG.swc"
#path = "../Neurons/Mouse/Striatum/51-5-DE-cor-rep-ax.swc"

neuron = Neuron(swc=path)  
n = 5 # <-- number of neurons to place in the cube
rpl = rpl_builder.create_rpl(n) # <- generate random transformations for n number of neurons
neuron_plotter.plot(neuron, rpl) # <- plot the cube with the neurons inside

# Input: 0 = x-rotation (roll), 1 = y-rotation (pitch), 2 = z-rotation (yaw)
#neuron_plotter.rotating_plot(neuron, 2) # <- plot a rotating neuron 