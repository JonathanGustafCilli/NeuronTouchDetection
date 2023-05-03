import matplotlib.pyplot as plt
import matplotlib.colors as mcolors 
import numpy as np

'''
Variables used for defining TIME COMPLEXIY of the functions:
    m = number of neurons
    n = number of segments in a neuron (i.e. number of rows in the swc file)
    s = number of soma segments in a neuron
    d = number of dendrite segments in a neuron
    a = number of axon segments in a neuron
    Such that: n = s+d+a
'''

def plot_cube(ax, x, y, z, size, color):
    # Plot the red boundary (cube's edges):
    x2 = x + size
    y2 = y + size
    z2 = z + size
    ax.plot3D([x2,x2],[y2,y2],[z,z2],color)
    ax.plot3D([x,x],[y2,y2],[z,z2],color)
    ax.plot3D([x2,x2],[y,y],[z,z2],color)
    ax.plot3D([x,x],[y,y],[z,z2],color)
    ax.plot3D([x,x2],[y2,y2],[z2,z2],color)
    ax.plot3D([x,x2],[y2,y2],[z,z],color)
    ax.plot3D([x,x2],[y,y],[z2,z2],color)
    ax.plot3D([x,x2],[y,y],[z,z],color)
    ax.plot3D([x2,x2],[y,y2],[z2,z2],color)
    ax.plot3D([x,x],[y,y2],[z2,z2],color)
    ax.plot3D([x2,x2],[y,y2],[z,z],color)
    ax.plot3D([x,x],[y,y2],[z,z],color)

def plot(neurons, ax):
    # Plot all neurons:
    for neuron in neurons:
        
        # Assign random colors to the neuron: 
        r = np.round(np.random.rand(),1)
        g = np.round(np.random.rand(),1)
        b = np.round(np.random.rand(),1)
        colors = []
        for _ in range(neuron.get_somas().shape[0]): colors.append([1,0,0,1])
        for _ in range(neuron.get_dendrites().shape[0]): colors.append([r,g,b,0.7])
        for _ in range(neuron.get_axons().shape[0]): colors.append([r*0.7,g*0.7,b*0.7,1])
        
        neurites = neuron.get_neurites() # <- get the complete matrix of the neuron O(n)
        ax.scatter(neurites[:,1], neurites[:,2], neurites[:,3], s=neurites[:,4], c=colors, marker='o') # O(n)?
    
    plot_cube(ax, -250, -250, -250, 500, "red")

    

def plot_w_synapses(neurons, synapses, ax):
    plot(neurons, ax)
    # Plot the synapses:
    ax.scatter(synapses[:,0], synapses[:,1], synapses[:,2], s=[30 for v in synapses[:,0]], c=["magenta" for v in synapses[:,0]], marker='o')
    