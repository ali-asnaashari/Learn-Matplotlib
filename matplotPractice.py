import matplotlib.pyplot as plt

# Part1
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 1, 6, 5, 6, 8, 2, 5, 4, 4]
plt.plot(x, y)
plt.show()
"""

# Part2
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 1, 6, 5, 6, 8, 2, 5, 4, 4]
# create window
plt.figure(figsize=(10, 8))
plt.plot(x, y)
# title
plt.title("my first plot \n Ali asnaashari", fontsize=13)
plt.show()
