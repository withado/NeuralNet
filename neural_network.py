from math import e
from random import uniform, randint

class networkLayer() :
    def __init__(self, neuronCount_previousLayer, neuronCount_Current) :
        # initial variables
        self.weightCount, self.neuronCount = neuronCount_previousLayer, neuronCount_Current

        # create arrays for the layer's weights and values
        self.weights = [ [uniform(-1, 1) for i in range(self.weightCount)] for i in range(self.neuronCount)]
        #self.weights = [ [1 for i in range(self.weightCount)] for i in range(self.neuronCount)] # for testing purposes
        self.valuesBase = [0 for i in range(self.neuronCount)]
        self.values = self.valuesBase.copy()

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
        return error_previousLayer


class neuralNetwork() :

    def __init__(self, neuronsPerLayer) :
        self.layers = list()

        for layer, neurons in enumerate(neuronsPerLayer) :
            # if its the input layer, make it 0 connections
            if layer == 0 :
                self.layers.append(networkLayer(0, neurons))
                continue
            # otherwise, its connected to all in the previous layer
            self.layers.append(networkLayer(neuronsPerLayer[layer - 1], neurons))

    def insertInput(self, input, desiredOutput, inputLayer = 0) :
        self.desiredOutput = desiredOutput
        inputLayerValues = self.layers[inputLayer].values
        if len(input) == len(inputLayerValues) :
            self.layers[0].values = input
        else : return print("ERROR: INVALID INPUT")

    def fowardPropagate(self) :
        for layerIndex, layer in enumerate(self.layers[1:]):
            layer.propagate(self.layers[layerIndex].values)
    

    def backPropagate(self) :
        for layerIndex, layer in enumerate(reversed(self.layers)) :
            print(layerIndex)
            if layerIndex == 0 : 
                # if layer is the last layer, then determine initial layer error using the derivative of the cost function :)
                layerError = [( self.desiredOutput[index] - value ) for index, value in enumerate(self.layers[-1].values)]

                # defining the error for the next layer
                layerError = layer.determine_gradients(self.layers[layerIndex + 1].values, layerError)
                print("asdf")
                continue

            # as long as the layer is not the first layer, then
            if layer != self.layers[-1] :

                # define error for the next layer
                print (f"{self.layers[layerIndex].values} \n {self.layers[layerIndex+1].values}")
                layerError = layer.determine_gradients(self.layers[layerIndex + 1].values, layerError)





#########this part is easily changed for other problems##############
#####################################################################
# make those inputs
# theres probably a better way to do this btw im just lazy
outputs_key = ([0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1])
#outputs_key = ([0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0])
def create_input(quiet = True, inputToValues = True) :
    input = [0 for i in range(8)]
    num = randint(0,7)
    input[num] = 1
    correct_output = outputs_key[num]
    return input, correct_output
#####################################################################





e = neuralNetwork([8, 4, 3])
input, correct_output = create_input()
e.insertInput(input, correct_output)

print(e.desiredOutput)
for i in range(10) :
    e.fowardPropagate()
    print(e.layers[-1].values)
    e.backPropagate()
# Test
'''e = networkLayer(1, 2)
for i in range(100) :
    e.propagate([1])
    print ("weights:", e.weights, "\n", "values:", e.values)
    e.determine_gradients([1], [(0 - e.values[0]), (0 - e.values[1])])
    print(e.weightGradient)'''