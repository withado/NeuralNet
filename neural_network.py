from math import e
from random import uniform

class networkLayer() :
    def __init__(self, neuronCount_previousLayer, neuronCount_Current) :
        self.weightCount, self.neuronCount = neuronCount_previousLayer, neuronCount_Current

    def create_layer(self) :
        self.weights = [ [uniform(-1, 1) for i in range(self.weightCount)] for i in range(self.neuronCount)]
        print(self.weights)

e = networkLayer(6, 6)
e.create_layer()
