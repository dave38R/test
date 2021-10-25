# Let's code an artificial neuron

import numpy as np 

def lin_com(input_layer, weights):

	np.append(1, input_layer)
	if len(input_layer) == len(weights):
		return sum(input_layer*weights)

	else:
		print("input_layer and weights are not the same size")
		return None
