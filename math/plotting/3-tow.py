#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Plot graph
plt.plot(x, y1, linestyle="dashed", color="red")
plt.plot(x, y2, color="green")

# Set the range of x-axis
plt.xlim(0, x[x.size - 1])

# Set the range of y-axis
plt.ylim(0)

# Plot style
plt.title("Exponential Decay of Radioactive Elements")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")

# Plot legend style
plt.legend(["C-14", "Ra-226"], loc="upper right")

# Show graph
plt.show()
