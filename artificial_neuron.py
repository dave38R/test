# Let's code an artificial neuron

import numpy as np 

def lin_com(input_layer, weights):

	np.append(1, input_layer)
	if len(input_layer) == len(weights):
		return sum(input_layer*weights)

	else:
		print("input_layer and weights are not the same size")
		return None

def activation_function(x):
  return 1/(1 + np.exp(-x))
def activation_derivative(x):
  return activation_function(x)(1 - activation_function(x))

def cost_function(y_gotten, y_wanted):
  return 1/2*(y_gotten - y_wanted)**2

def cost_derivative(y_gotten, y_wanted) : 
  return y_gotten - y_wanted


def forward_propagation(input_layer, weights):
  return activation_function(lin_com(input_layer, weights))

def backward_propagation(input_layer, weights, y__wanted, learning_rate):
  y_gotten = forward_propagation(input_layer, weights)

  for i in range(len(weights)):
    old_weight = weight[i]
    new_weight = old_weight - cost_derivative(y_gotten, y_wanted)*activation_derivative(lin_com(input_layer, weights))*input_layer[i]