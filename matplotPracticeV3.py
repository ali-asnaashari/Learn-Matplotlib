import matplotlib.pyplot as plt
import numpy as np

x = list(range(1, 13))
y = np.random.randint(20, 60, 12)

# Part1
plt.bar(x, y)
plt.show()
