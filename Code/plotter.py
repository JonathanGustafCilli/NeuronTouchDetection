import matplotlib.pyplot as plt
import numpy as np

class Plot:
    def __init__(self):
        # Properties of the plot: 
        plt.style.use('dark_background')
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.set_zlabel('Z Axis')
        self.ax.set_zlim(-400,400)
        self.ax.set_xlim(-400,400)
        self.ax.set_ylim(-400,400)

    def plot_cube(self, x, y, z, size, color):
        # Plot the red boundary (cube's edges):
        x2 = x + size
        y2 = y + size
        z2 = z + size
        self.ax.plot3D([x2,x2],[y2,y2],[z,z2],color)
        self.ax.plot3D([x,x],[y2,y2],[z,z2],color)
        self.ax.plot3D([x2,x2],[y,y],[z,z2],color)
        self.ax.plot3D([x,x],[y,y],[z,z2],color)
        self.ax.plot3D([x,x2],[y2,y2],[z2,z2],color)
        self.ax.plot3D([x,x2],[y2,y2],[z,z],color)
        self.ax.plot3D([x,x2],[y,y],[z2,z2],color)
        self.ax.plot3D([x,x2],[y,y],[z,z],color)
        self.ax.plot3D([x2,x2],[y,y2],[z2,z2],color)
        self.ax.plot3D([x,x],[y,y2],[z2,z2],color)
        self.ax.plot3D([x2,x2],[y,y2],[z,z],color)
        self.ax.plot3D([x,x],[y,y2],[z,z],color)
   
    def plot_neurons(self, neurons):
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
            self.ax.scatter(neurites[:,1], neurites[:,2], neurites[:,3], s=neurites[:,4], c=colors, marker='o') # O(n)?
    
    def plot_synapses(self, synapses):
        array = np.array(synapses)
        if array.size>0: self.ax.scatter(array[:,0], array[:,1], array[:,2], s=[30 for v in array[:,0]], c=["magenta" for v in array[:,0]], marker='o')
        else: print("No synapses found! Nothing to plot.")

    def show(self):
        self.fig.show()
        input("Continue..")