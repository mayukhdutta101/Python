#Write a python program to implement linear regression.

import numpy as np
import matplotlib.pyplot as plt

def linear_regression(X, y):
    X_b = np.c_[np.ones((len(X), 1)), X]
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    return theta_best

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

theta = linear_regression(X, y)

X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta)

plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression")
plt.show()
