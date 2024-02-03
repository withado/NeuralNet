from math import e
from random import uniform

class networkLayer() :
    def __init__(self, neuronCount_previousLayer, neuronCount_Current) :
        # initial variables
        self.weightCount, self.neuronCount = neuronCount_previousLayer, neuronCount_Current

        # create arrays for the layer's weights and values
        self.weights = [ [uniform(-1, 1) for i in range(self.weightCount)] for i in range(self.neuronCount)]
        #self.weights = [ [1 for i in range(self.weightCount)] for i in range(self.neuronCount)] # for testing purposes
        self.valuesBase = [0 for i in range(self.neuronCount)]

    # 1) feed an input (usually previous layer)
    def propagate(self, input) :
        self.values=self.valuesBase.copy()
        # 2) go through each neuron
        for neuronIndex, value in enumerate(self.values) :
            # 3) go through weights of said neuron
            for neuronIndex_input, weight in enumerate(self.weights[neuronIndex]) :
                # 4) determine value of neuron (z = sigma_n(input_n * weight_n) + bias_neuron) 
                # for now, we will just be working with the alteration of the weights
                self.values[neuronIndex] += input[neuronIndex_input] * weight + 0


    def determine_gradients(self, values_previousLayer, layerError) : 
        self.weightGradient = list()
        error_previousLayer = [0 for i in values_previousLayer]


        for neuronIndex, value in enumerate(self.values) :
            # create a list for all the neuron's weights in the graidents list
            self.weightGradient.append(list())

            # 1) find dZ/dW(n)
            for neuronIndex_previousLayer, weight in enumerate(self.weights[neuronIndex]) :
                # dZ/dW = a_(layer - 1)
                weightError = layerError[neuronIndex] * values_previousLayer[neuronIndex_previousLayer]
                self.weightGradient[neuronIndex].append(weightError)
                error_previousLayer[neuronIndex_previousLayer] -= weightError
        # enact the weightsGradient array upon the weights
        for neuronIndex, weights in enumerate(self.weights) :
            for connectedNeuron, weight in enumerate(weights) :
                self.weights[neuronIndex][connectedNeuron] += self.weightGradient[neuronIndex][connectedNeuron] * .1 # NOTE: ADD LEARNING RATE


class neuralNetwork() :
    def __init__(self, neuronsPerLayer) :
        self.layers = list()
        for layer, neurons in enumerate(neuronsPerLayer) :
            if layer == 0 :
                self.layers.append(networkLayer(0, neurons))
                continue
            self.layers.append(networkLayer(neuronsPerLayer[layer - 1], neurons))



e = neuralNetwork([3, 4, 6])

# Test
'''e = networkLayer(1, 2)
for i in range(100) :
    e.propagate([1])
    print ("weights:", e.weights, "\n", "values:", e.values)
    e.determine_gradients([1], [(0 - e.values[0]), (0 - e.values[1])])
    print(e.weightGradient)'''