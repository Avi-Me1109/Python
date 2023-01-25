import numpy as np

input_vector = [1.72, 1.23]
weights_1 = [1.26, 0]
weights_2 = [2.17, 0.32]

dotProduct1 = np.dot(input_vector, weights_1)
dotProduct2 = np.dot(input_vector, weights_2)

if dotProduct1 > dotProduct2:
    print("Weights1 more similar")

else:
    print("Weights2 more similar")