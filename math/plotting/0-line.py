#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plot graph
plt.plot(y, color='red')

# Set the range of x-axis
plt.xlim(0, 10)

# Display plot
plt.show()
