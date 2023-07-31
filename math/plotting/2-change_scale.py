#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Plot graph
plt.plot(x, y)

# Scale the y-axis
plt.yscale("log")

# Set the range of x-axis
plt.xlim(0, x[x.size - 1])

# Plot style
plt.title("Exponential Decay of C-14")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")

# Show graph
plt.show()
