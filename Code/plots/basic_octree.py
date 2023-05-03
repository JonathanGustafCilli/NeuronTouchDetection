import numpy as np
import random
import sys
sys.path.append('../../code')
from basics.Cube import Cube
from algorithms.octree.Octree import Octree
from plotter import Plot

plot = Plot()
boundary = Cube(-250, -250, -250, 500)
octree = Octree(boundary, plot)

points = []
for i in range(61):
    point = [random.randint(-250, 0), random.randint(-250, 0), random.randint(-250, 0), 0]
    points.append(point)
    octree.insert(point)

points_array = np.array(points)
plot.ax.scatter(points_array[:,0], points_array[:,1], points_array[:,2], s = [10 for _ in points_array[:,2]], c= ['green' for _ in points_array[:,2]], marker='o') # O(n)?


# FOUND CLOSE TO ME
'''
range = Cube(-200, -100, -100, 100)
plot.plot_cube(range.x, range.y, range.z, range.size, 'blue')

found = []
octree.query(range, found, 1)
print(found)
found_array = np.array(found)
plot.ax.scatter(found_array[:,0], found_array[:,1], found_array[:,2], s = [15 for _ in found_array[:,2]], c= ['magenta' for _ in found_array[:,2]], marker='o') # O(n)?
'''
plot.show()
