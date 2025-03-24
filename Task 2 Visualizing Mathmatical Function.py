#Visualizing Mathmatical Functions

import numpy as np
import matplotlib.pyplot as plt

# First plot data and functions
def f(x):
    return np.exp(-x**2) + 3 * np.sin(x + np.pi / 4)

x_values = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_values = f(x_values)

# Second plot data and functions
def x(t):
    return 2 * np.sin(t) * np.exp(np.cos(t))
def y(t):
    return -3 * np.cos(t) * np.exp(np.sin(2 * t))

t_values = np.linspace(0, 2 * np.pi, 500)
x_t = x(t_values)
y_t = y(t_values)

# Create a figure with two subplots combined
plt.figure(figsize=(12, 6))

# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x_values, y_values, label=r'$f(x) = e^{-x^2} + 3 \sin(x + \frac{\pi}{4})$', color='g')
plt.title("Plot of Function", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.legend(loc='upper right')
plt.grid(True)

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x_t, y_t, label=r'Parametric curve', color='r')
plt.title("Parametric Plot", fontsize=10)
plt.xlabel("x(t)", fontsize=8)
plt.ylabel("y(t)", fontsize=8)
plt.legend()

# Saves the plots side by side to a png file called plots.png
plt.tight_layout
plt.savefig("plots.png")
