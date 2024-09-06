# 1. Write a Python program that computes the value of the Gaussian distribution at a given vector X. Hence, plot the effect of varying mean and variance to the normal distribution.

import numpy as np
import matplotlib.pyplot as plt

def gaussian_distribution(x, mean, variance):
    return (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-((x - mean) ** 2) / (2 * variance))

x_values = np.linspace(-10, 10, 1000)

means = [0, 0, 0]
variances = [1, 2, 3]

for mean, variance in zip(means, variances):
    y_values = gaussian_distribution(x_values, mean, variance)
    plt.plot(x_values, y_values, label=f"Mean: {mean}, Variance: {variance}")

plt.title("Gaussian Distribution with Varying Mean and Variance")
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
