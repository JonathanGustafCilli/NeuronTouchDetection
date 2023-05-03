import time
from basics.Neuron import Neuron
import basics.rpl_builder as rpl_builder
import algorithms.linearsearch.td_linear_search as td_linear_search 
import algorithms.octree.td_octree as td_octree 
import algorithms.snudda.td_snudda as td_snudda 

def generate_neurons(type :str, quantity: int):
    neuron = Neuron(type) # <- create neuron from swc file  
    rpl = rpl_builder.create_rpl(quantity) # <- generate random transformations for n number of neurons    
    neurons = []
    for transformation in rpl:
        neuron_copy = neuron.copy() # O(n)
        neuron_copy.transform(transformation) # O(n)
        neurons.append(neuron_copy)
    return neurons    

if __name__ == '__main__':
    # Path of the neuron: 
    path = "../neurons/mouse/striatum/test_neuron.swc"
    #path = "../Neurons/Mouse/Striatum/51-5-DE-cor-rep-ax.swc"
    
    # Number of neurons:
    m = 10 
    neurons = generate_neurons(path, m)
    td_snudda.touch_detection(neurons)
    
    '''
    start_timer = time.time()
    synapses = td_octree.touch_detection(neurons, None, True)
    end_timer = time.time()
    minutes = (end_timer-start_timer)/60
    print("\n--- Touch Detection with Octree ---")
    print(f"  * took: {int(minutes)}m {int(((minutes%1)*60)*1000)/1000}s")
    print("  * synapses counted:", len(synapses))
    
    if len(synapses)>0:    
        start_timer = time.time()
        synapses = td_linear_search.touch_detection(neurons, True)
        end_timer = time.time()
        minutes = (end_timer-start_timer)/60
        print("\n--- Touch Detection with TotSearch ---")
        print(f"  * took: {int(minutes)}m {int(((minutes%1)*60)*1000)/1000}s")
        print("  * synapses counted:", len(synapses))
    '''
    
