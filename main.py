# A Perceptron consists of one or more inputs, a processor and a single output.

import numpy as np
import random

weight = []
learning_rate = 0.01

def assign_random_weight(n):
    """Assigns random weight. """
    for i in range(n):
        weight.append(random.randrange(-1, 1))

def train(inputs, desired_output):
    """Train the network against known data. """
    guess_output = processor(inputs)
    error = desired_output - guess_output
    for i in range(len(inputs)):
        weight[i] += learning_rate * inputs[i] * error

def processor(inputs):
    """Returns output based on the input. """
    return activate(np.sum(inputs))

def activate(sum):
    """Returns 1 if the sum is greater than 0 and -1  if the sum is lesser than 0. """
    if(sum > 0):
        return 1
    return -1

def f(x):
    return 2*x + 1


# Assign random weights
assign_random_weight(2)

# Train the perceptron with some data. 
for i in range(20000):
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    if(y < f(x)):
        train([x, y], -1)
    else:
        train([x, y], 1)        


total_right_assumptions = 0.
total_values_predicted = 100

for i in range(total_values_predicted):
    x, y = random.uniform(-10, 10), random.uniform(-10, 10)
    actual_value = activate(f(x))
    predicted_value = processor([x, y])
    if(actual_value == predicted_value):
        total_right_assumptions += 1
    print(x, y, processor([x, y]), activate(f(x)))

print("Total right assumptions.", (total_right_assumptions / total_values_predicted) * 100)