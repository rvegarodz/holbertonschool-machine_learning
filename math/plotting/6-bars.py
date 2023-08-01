#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Data Manipulation
names = np.array(["Farrah", "Fred", "Felicia"])
fruits = np.array(["apples", "bananas", "oranges", "peaches"])
apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]

# Data Visualization
plt.bar(names, apples, color="red", width=0.5)
plt.bar(names, bananas, bottom=apples,
        color="yellow", width=0.5)
plt.bar(names, oranges, bottom=apples+bananas,
        color="#ff8000", width=0.5)
plt.bar(names, peaches, bottom=apples+bananas+oranges,
        color="#ffe5b4", width=0.5)

# Plot styling
plt.title("Number of Fruit per Person")
plt.legend(fruits, loc="upper right")
plt.ylabel("Quantity of Fruit")
plt.ylim(0, 80)
plt.show()
