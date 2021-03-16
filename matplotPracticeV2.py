import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)

# Part1
fig = plt.figure(figsize=(10, 8))
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
