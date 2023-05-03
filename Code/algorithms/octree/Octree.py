import numpy as np
from basics.Cube import Cube 
class Octree:
    def __init__(self, boundary :Cube, capacity, plot = None):
        self.boundary = boundary
        self.capacity = capacity
        self.counter = 0
        self.points = []
        self.divided = False
        self.plot = plot
        if plot!=None: plot.plot_cube(self.boundary.x, self.boundary.y, self.boundary.z, self.boundary.size, 'red')
            
    
    '''
        Subdived the boundary into 8 smaller cubes.
        E.g. nomenclature: 
        SE_F stands for South East Front cube
        NW_B stands for North West Back cube 
    '''
    def subdived(self):
        SE_F = Cube(self.boundary.x, self.boundary.y, self.boundary.z, self.boundary.size/2)
        self.SE_F = Octree(SE_F, self.capacity, self.plot)
        SW_F = Cube(self.boundary.x+self.boundary.size/2, self.boundary.y, self.boundary.z, self.boundary.size/2)
        self.SW_F = Octree(SW_F, self.capacity, self.plot)
        NE_F = Cube(self.boundary.x, self.boundary.y+self.boundary.size/2, self.boundary.z, self.boundary.size/2)
        self.NE_F = Octree(NE_F, self.capacity, self.plot)
        NW_F = Cube(self.boundary.x+self.boundary.size/2, self.boundary.y+self.boundary.size/2, self.boundary.z, self.boundary.size/2)
        self.NW_F = Octree(NW_F, self.capacity, self.plot)

        SE_B = Cube(self.boundary.x, self.boundary.y, self.boundary.z+self.boundary.size/2, self.boundary.size/2)
        self.SE_B = Octree(SE_B, self.capacity, self.plot)
        SW_B = Cube(self.boundary.x+self.boundary.size/2, self.boundary.y, self.boundary.z+self.boundary.size/2, self.boundary.size/2)
        self.SW_B = Octree(SW_B, self.capacity, self.plot)
        NE_B = Cube(self.boundary.x, self.boundary.y+self.boundary.size/2, self.boundary.z+self.boundary.size/2, self.boundary.size/2)
        self.NE_B = Octree(NE_B, self.capacity, self.plot)
        NW_B = Cube(self.boundary.x+self.boundary.size/2, self.boundary.y+self.boundary.size/2, self.boundary.z+self.boundary.size/2, self.boundary.size/2)
        self.NW_B = Octree(NW_B, self.capacity, self.plot)
        
        self.divided = True

    '''
        Insert the point in the octree.
    '''
    def insert(self, point):
        if (not self.boundary.contains(point)): return False
        if (self.counter<self.capacity):
            self.points.append(point)
            self.counter += 1
        else:
            if (not self.divided): 
                self.subdived()
                for p in self.points:
                    self.insert_helper(p)
            self.insert_helper(point)
    '''
        Insert point into the suboctree
    '''
    def insert_helper(self, point):
        if self.SE_F.insert(point): return True
        elif self.SW_F.insert(point): return True
        elif self.NE_F.insert(point): return True
        elif self.NW_F.insert(point): return True
        elif self.SE_B.insert(point): return True
        elif self.SW_B.insert(point): return True
        elif self.NE_B.insert(point): return True
        elif self.NW_B.insert(point): return True

    '''
        Find all points that are 3 micrometers from the query point.
    '''
    def query(self, range, found, neuronID):
        if self.boundary.intersect(range):
            if self.divided:
                self.SE_F.query(range, found, neuronID)
                self.SW_F.query(range, found, neuronID)
                self.NE_F.query(range, found, neuronID)
                self.NW_F.query(range, found, neuronID)
                self.SE_B.query(range, found, neuronID)
                self.SW_B.query(range, found, neuronID)
                self.NE_B.query(range, found, neuronID)
                self.NW_B.query(range, found, neuronID)
            else:
                for p in self.points:
                    if p[3] != neuronID:
                        if np.linalg.norm(np.array([p[0],p[1],p[2]])-np.array([range.x+3,range.y+3,range.z+3])) < 3:
                            found.append(p)
                