from math import e
from random import uniform

class networkLayer() :
    def __init__(self, neuronCount_previousLayer, neuronCount_Current) :
        # initial variables
        self.weightCount, self.neuronCount = neuronCount_previousLayer, neuronCount_Current

        # create arrays for the layer's weights and values
        self.weights = [ [uniform(-1, 1) for i in range(self.weightCount)] for i in range(self.neuronCount)]
        self.values = [0 for i in range(self.neuronCount)]

    # 1) feed an input (usually previous layer)
    def propagate(self, input) :
        # 2) go through each neuron
        for neuronIndex, value in enumerate(self.values) :
            # 3) go through weights of said neuron
            for neuronIndex_input, weight in enumerate(self.weights) :
                # 4) determine value of neuron (z = sigma_n(input_n * weight_n) + bias_neuron) 
                # for now, we will just be working with the alteration of the weights
                self.values[neuronIndex] += input[neuronIndex_input] * weight

# Test
e = networkLayer(6, 6)
