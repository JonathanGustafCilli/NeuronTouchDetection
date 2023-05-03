from basics.Cube import Cube 
import numpy as np

class Hypervoxel:
    def __init__(self, boundary:Cube):
        self.boundary = boundary
        self.neuron_IDs = []

    def insert(self, neuron_id):
        self.neuron_IDs.append(neuron_id)