import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import math
import matplotlib.colors as mcolors

'''
Variables used for defining TIME COMPLEXIY of the functions:
    m = number of neurons
    n = number of segments in a neuron (i.e. number of rows in the swc file)
    s = number of soma segments in a neuron
    d = number of dendrite segments in a neuron
    a = number of axon segments in a neuron
    Such that: n = s+d+a
'''
def plot(neuron, rpl):
    
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
    names = list(mcolors.TABLEAU_COLORS) 

    # Transform and plot all neurons
    i=-1
    for t in rpl: # O(m*4n)
        i+=1
        copy_neuron = neuron.copy() # <- create a copy of the input neuron O(n)
        copy_neuron.transform(t) # <- transform the neuron (rotation & translation) O(n)
        neurites = copy_neuron.get_neurites() # <- get the matrix of the neuron O(n)
        # Plot the neuron:
        ax.scatter(neurites[:,1], neurites[:,2], neurites[:,3], s=neurites[:,4], c=[names[i] for _ in neurites[:,0]], marker='o') # O(n)?
        
    
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

    plt.show() # <- show the figure


''' ------------- NO NEED TO READ THE CODE BELOW ! ------------- 
    It is used to test the rotation transformations on the neuron.
'''
'''
N = None

def rotating_plot(neuron,t):
    
    global N
    colors = ['red', 'red', 'blue', 'green', 'purple']
    N = neuron

    plt.style.use('dark_background')
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    def update(f):
        global N

        ax.clear()
        v = math.pi/100

        if t==0: 
            N.rotate_x(v)
            ax.plot3D([-500,500],[0,0],[0,0],'purple')
        elif t==1: 
            N.rotate_y(v)
            ax.plot3D([0,0],[-500,500],[0,0],'purple')
        elif t==2: 
            N.rotate_z(v)
            ax.plot3D([0,0],[0,0],[-500,+500],'purple')

        neurites = N.get_array()
        ax.scatter(neurites[:,1], neurites[:,2], neurites[:,3], s=neurites[:,4], c=[colors[int(v)] for v in neurites[:,0]], marker='o')
        ax.set_zlim(-500,500)
        ax.set_xlim(-500,500)
        ax.set_ylim(-500,500)
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')        
        
    ani = FuncAnimation(fig, update, frames=2, interval=100, repeat=True)
    plt.show()


def plot3(neuron, rpl, synapses):
    
    colors = ['magenta', 'cyan'] # <- used to make soma = red, axons = blue, etc.
    
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
    
    ax.scatter(synapses[:,0], synapses[:,1], synapses[:,2], s=[30 for v in synapses[:,0]], c=["blue" for v in synapses[:,0]], marker='o')
    # Transform and plot all neurons
    i = 0
    for t in rpl:
        copy_neuron = neuron.copy() # <- create a copy of the input neuron
        copy_neuron.rotate(t[4],t[5],t[6]) # <- rotate the neuron
        #copy_neuron.rotate_x(t[4]) 
        #copy_neuron.rotate_y(t[5])
        #copy_neuron.rotate_z(t[6])
        copy_neuron.translate(t[1],t[2],t[3]) # <- move the neuron
        neurites = copy_neuron.get_array() # <- get the matrix of the neuron
        # Plot the neuron:
        ax.scatter(neurites[:,1], neurites[:,2], neurites[:,3], s=neurites[:,4], c=[colors[i] for v in neurites[:,0]], marker='o')
        i += 1
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

    plt.show() # <- show the figure
'''