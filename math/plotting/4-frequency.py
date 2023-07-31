#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Plot graph
plt.hist(student_grades, bins=range(0, 110, 10), edgecolor="black")

# Set the range of x-axis
plt.xticks(np.arange(0, 110, 10))
plt.xlim(0, 100)

# Set the range of y-axis
plt.ylim(0, 30)

# Plot style
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")

# Show graph
plt.show()
