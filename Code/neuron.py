import numpy as np
import math

class Neuron:
    def __init__(self, swc=None):
        if swc != None: 
            self.swc = swc
            self.array = self.parse_swc(swc)

    def get_array(self): return self.array

    def set_array(self, array): self.array = array
    
    ''' Create a copy of the current neuron ''' 
    def copy(self):
        neuron = Neuron()
        neuron.set_array(np.copy(self.array))
        return neuron
    
    ''' 
    Parse the SWC file (contains the neuron's segments)
    input: location of the SWC file 
    ouput: 
        5xN Matrix (N being the number of segments)
        1st column contains the x-position of the segment
        2nd column contains the y-position of the segment
        3rd column contains the z-position of the segment
        4th column contains the size of the segment
        5th column contains the parent of the segment
    '''
    def parse_swc(self, swc):
        neurites = []
        with open(swc,'r') as file:
            for l in file:
                l = l.split()
                neurites.append([int(l[1]),float(l[2]),float(l[3]),float(l[4]),float(l[5])])
        return np.array(neurites)
    
    ''' 3D Translation Transformation '''
    def translate(self, x, y, z):
        for r in self.array:
            r[1] += x
            r[2] += y
            r[3] += z

    ''' All Rotations Transformation '''
    def rotate(self, a, b, g):
        # a = yaw angle of rotation
        # b = pitch angle of rotation
        # g = roll angle of rotation
        rotation = np.array([
            [math.cos(a)*math.cos(b), math.cos(a)*math.sin(b)*math.sin(g) - math.sin(a)*math.cos(g), math.cos(a)*math.sin(b)*math.cos(g) + math.sin(a)*math.sin(g)],
            [math.sin(a)*math.cos(b), math.sin(a)*math.sin(b)*math.sin(g) + math.cos(a)*math.cos(g), math.sin(a)*math.sin(b)*math.cos(g) + math.cos(a)*math.sin(g)],
            [-math.sin(b), math.cos(b)*math.sin(g), math.cos(b)*math.cos(g)]
            ])
        for r in self.array:
            c = np.dot(rotation, [r[1],r[2],r[3]])
            r[1] = c[0]
            r[2] = c[1]
            r[3] = c[2]
    
    ''' Roll Rotation Transformation '''
    def rotate_x(self, v):
        rotation = np.array([[1,0,0],[0,math.cos(v),-math.sin(v)],[0,math.sin(v),math.cos(v)]])
        for r in self.array:
            c = np.dot(rotation, [r[1],r[2],r[3]])
            r[1] = c[0]
            r[2] = c[1]
            r[3] = c[2]

    ''' Pitch Rotation Transformation '''
    def rotate_y(self, v):
        rotation = np.array([[math.cos(v),0,math.sin(v)],[0,1,0],[-math.sin(v),0,math.cos(v)]])
        for r in self.array:
            c = np.dot(rotation, [r[1],r[2],r[3]])
            r[1] = c[0]
            r[2] = c[1]
            r[3] = c[2]

    ''' Yaw Rotation Transformation '''
    def rotate_z(self, v):   
        rotation = np.array([[math.cos(v),-math.sin(v),0],[math.sin(v),math.cos(v),0],[0,0,1]])
        for r in self.array:
            c = np.dot(rotation, [r[1],r[2],r[3]])
            r[1] = c[0]
            r[2] = c[1]
            r[3] = c[2]