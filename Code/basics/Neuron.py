import numpy as np
import math

'''
Variables used for defining TIME COMPLEXIY of the functions:
    n = number of segments in a neuron (i.e. number of rows in the swc file)
    s = number of soma segments in a neuron
    d = number of dendrite segments in a neuron
    a = number of axon segments in a neuron
    Such that: n = s+d+a
'''
class Neuron:
    def __init__(self, swc=None):
        if swc != None: 
            self.dendrites = None
            self.axons = None
            self.somas = None
            self.parse_swc(swc)

    def get_somas(self): return self.somas # O(1) 
    def get_dendrites(self): return self.dendrites # O(1)
    def get_axons(self): return self.axons # O(1)
    def get_neurites(self): # O(n) = O(s+d+a)
        neurites = []
        for soma in self.somas: neurites.append(soma)
        for dendrite in self.dendrites: neurites.append(dendrite)
        for axon in self.axons: neurites.append(axon)
        return np.array(neurites)

    def set_somas(self, somas): self.somas = somas # O(1)
    def set_dendrites(self, dendrites): self.dendrites = dendrites # O(1)
    def set_axons(self, axons): self.axons = axons # O(1)
    
    ''' Create a copy of the current neuron ''' 
    def copy(self): # O(n) = O(s+d+a)
        neuron = Neuron()
        neuron.set_somas(np.copy(self.somas))
        neuron.set_dendrites(np.copy(self.dendrites))
        neuron.set_axons(np.copy(self.axons))
        return neuron
    
    ''' 
    Parse the SWC file (contains the neuron's segments)
    input: location of the SWC file 
    ouput: 
        5xn Matrix (n being the number of segments)
        1st column contains the x-position of the segment
        2nd column contains the y-position of the segment
        3rd column contains the z-position of the segment
        4th column contains the size of the segment
        5th column contains the parent of the segment
    '''
    def parse_swc(self, swc): # O(2n)
        somas = []
        axons = []
        dendrites = []
        with open(swc,'r') as file: # O(n)
            for row in file: 
                row = row.split()
                # A segment is made out of: ID, x-pos, y-pos, z-pos, size, ParentID
                segment = [int(row[0]),float(row[2]),float(row[3]),float(row[4]),float(row[5])]
                if row[1] == '3' or row[1] == '4': dendrites.append(segment) # 3 & 4 = dendrites
                elif row[1] == '2': axons.append(segment) # 2 = axons
                elif row[1] == '1': somas.append(segment) # 1 = somas
        # Convert lists into arrays(Numpy):
        self.somas = np.array(somas) # O(s)
        self.axons = np.array(axons)  # O(a)
        self.dendrites = np.array(dendrites)  # O(d)
    
    ''' 3D Translation Transformation '''
    def translate(self, x, y, z): # O(n)
        for soma in self.somas: # O(s)
            soma[1] += x
            soma[2] += y
            soma[3] += z
        for dendrite in self.dendrites: # O(d)
            dendrite[1] += x
            dendrite[2] += y
            dendrite[3] += z
        for axon in self.axons: # O(a)
            axon[1] += x
            axon[2] += y
            axon[3] += z

    ''' All Rotations Transformation '''
    def rotate(self, a, b, g): # O(n)
        # a = yaw angle of rotation
        # b = pitch angle of rotation
        # g = roll angle of rotation
        rotation = np.array([
            [math.cos(a)*math.cos(b), math.cos(a)*math.sin(b)*math.sin(g) - math.sin(a)*math.cos(g), math.cos(a)*math.sin(b)*math.cos(g) + math.sin(a)*math.sin(g)],
            [math.sin(a)*math.cos(b), math.sin(a)*math.sin(b)*math.sin(g) + math.cos(a)*math.cos(g), math.sin(a)*math.sin(b)*math.cos(g) + math.cos(a)*math.sin(g)],
            [-math.sin(b), math.cos(b)*math.sin(g), math.cos(b)*math.cos(g)]
            ])
        for soma in self.somas: # O(s)
            c = np.dot(rotation, [soma[1],soma[2],soma[3]])
            soma[1] = c[0]
            soma[2] = c[1]
            soma[3] = c[2]
        for dendrite in self.dendrites: # O(d)
            c = np.dot(rotation, [dendrite[1],dendrite[2],dendrite[3]])
            dendrite[1] = c[0]
            dendrite[2] = c[1]
            dendrite[3] = c[2]
        for axon in self.axons: # O(a)
            c = np.dot(rotation, [axon[1],axon[2],axon[3]])
            axon[1] = c[0]
            axon[2] = c[1]
            axon[3] = c[2]

    ''' Apply Rotation and Translation Transformations 
        Faster than applying rotation and transformation separatly
    '''
    def transform(self, rpl_row): # O(n)
        # a = yaw angle of rotation
        # b = pitch angle of rotation
        # g = roll angle of rotation
        x = rpl_row[1]
        y = rpl_row[2]
        z = rpl_row[3]
        a = rpl_row[4]
        b = rpl_row[5]
        g = rpl_row[6]
        rotation = np.array([
            [math.cos(a)*math.cos(b), math.cos(a)*math.sin(b)*math.sin(g) - math.sin(a)*math.cos(g), math.cos(a)*math.sin(b)*math.cos(g) + math.sin(a)*math.sin(g)],
            [math.sin(a)*math.cos(b), math.sin(a)*math.sin(b)*math.sin(g) + math.cos(a)*math.cos(g), math.sin(a)*math.sin(b)*math.cos(g) + math.cos(a)*math.sin(g)],
            [-math.sin(b), math.cos(b)*math.sin(g), math.cos(b)*math.cos(g)]
        ])
        for soma in self.somas: # O(s)
            c = np.dot(rotation, [soma[1],soma[2],soma[3]])
            soma[1] = c[0] + x
            soma[2] = c[1] + y
            soma[3] = c[2] + z
        for dendrite in self.dendrites: # O(d)
            c = np.dot(rotation, [dendrite[1],dendrite[2],dendrite[3]])
            dendrite[1] = c[0] + x
            dendrite[2] = c[1] + y
            dendrite[3] = c[2] + z
        for axon in self.axons: # O(a)
            c = np.dot(rotation, [axon[1],axon[2],axon[3]])
            axon[1] = c[0] + x
            axon[2] = c[1] + y
            axon[3] = c[2] + z
