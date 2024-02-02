from math import e
from random import uniform

class networkLayer() :
    def __init__(self, neuronCount_previousLayer, neuronCount_Current) :
        self.weightCount, self.neuronCount = neuronCount_previousLayer, neuronCount_Current
        self.weights = [ [uniform(-1, 1) for i in range(self.weightCount)] for i in range(self.neuronCount)]
        self.values = [0 for i in range(self.neuronCount)]
        print('done')

    def propagate(self, input) :
        for neuronIndex, value in enumerate(self.values) :
            for neuronIndex_input, weight in enumerate(self.weights) :
                self.values[neuronIndex] += input[neuronIndex_input] * weight


e = networkLayer(6, 6)
