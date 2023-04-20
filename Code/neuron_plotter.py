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
def plot(neurons, show_figure):
    
    # Properties of the plot: 
    plt.style.use('dark_background')
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_zlim(-400,400)
    ax.set_xlim(-400,400)
    ax.set_ylim(-400,400)

    # Plot all neurons:
    for neuron in neurons:
        
        # Assign random colors to the neuron: 
        r = np.round(np.random.rand(),1)
        g = np.round(np.random.rand(),1)
        b = np.round(np.random.rand(),1)
        colors = []
        for _ in range(neuron.get_somas().shape[0]): colors.append([1,0,0,1])
        for _ in range(neuron.get_dendrites().shape[0]): colors.append([r,g,b,0.2])
        for _ in range(neuron.get_axons().shape[0]): colors.append([r,g,b,1])
        
        neurites = neuron.get_neurites() # <- get the complete matrix of the neuron O(n)
        ax.scatter(neurites[:,1], neurites[:,2], neurites[:,3], s=neurites[:,4], c=colors, marker='o') # O(n)?
    
    # Plot the red cube's edges:
    ax.plot3D([250,250],[250,250],[-250,250],'red')
    ax.plot3D([-250,-250],[250,250],[-250,250],'red')
    ax.plot3D([250,250],[-250,-250],[-250,250],'red')
    ax.plot3D([-250,-250],[-250,-250],[-250,250],'red')
    ax.plot3D([-250,250],[250,250],[250,250],'red')
    ax.plot3D([-250,250],[250,250],[-250,-250],'red')
    ax.plot3D([-250,250],[-250,-250],[250,250],'red')
    ax.plot3D([-250,250],[-250,-250],[-250,-250],'red')
    ax.plot3D([250,250],[-250,250],[250,250],'red')
    ax.plot3D([-250,-250],[-250,250],[250,250],'red')
    ax.plot3D([250,250],[-250,250],[-250,-250],'red')
    ax.plot3D([-250,-250],[-250,250],[-250,-250],'red')

    if show_figure: plt.show() # <- show the figure
    else: return ax

def plot_w_synapses(neurons, synapses):
    ax = plot(neurons, False)
    # Plot the synapses:
    ax.scatter(synapses[:,0], synapses[:,1], synapses[:,2], s=[30 for v in synapses[:,0]], c=["magenta" for v in synapses[:,0]], marker='o')
    plt.show()