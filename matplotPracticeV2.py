import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)

# Part1
"""
fig = plt.figure(figsize=(10, 8))
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
"""

# Part2
"""
fig = plt.figure(figsize=(10, 8))
plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel("X")
plt.ylabel("F(X)")
plt.show()
"""

# Part3
fig = plt.figure(figsize=(10, 8))
plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel("X")
plt.ylabel("F(X)")
plt.xticks(np.arange(0, 2 * np.pi + 0.01, np.pi / 4),
           ['0', '$\pi/4$', '$\pi/2$', '$3\pi4/$', '$\pi$', '$5\pi/4$', '$3\pi/2$', '$7\pi/4$', '$2\pi$'])
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.show()
