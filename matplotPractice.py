import matplotlib.pyplot as plt

# Part1
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 1, 6, 5, 6, 8, 2, 5, 4, 4]
plt.plot(x, y)
plt.show()
"""

# Part2
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 1, 6, 5, 6, 8, 2, 5, 4, 4]
# create window
plt.figure(figsize=(10, 8))
plt.plot(x, y)
# title
plt.title("my first plot \n Ali asnaashari", fontsize=13)
plt.show()
"""

# Part3
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 1, 6, 5, 6, 8, 2, 5, 4, 4]
# create window
plt.figure(figsize=(10, 8))
plt.plot(x, y)
# title
plt.title("my first plot \n Ali asnaashari", fontsize=13)
# xlabel
plt.xlabel("x", fontsize=14)
# ylabel --> latex form
plt.ylabel("$y = x^2$", fontsize=14)
plt.show()
"""

# Part4
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 1, 6, 5, 6, 8, 2, 5, 4, 4]
# create window
plt.figure(figsize=(10, 8))
plt.plot(x, y, linewidth=4, color="blue", linestyle="--")
# title
plt.title("my first plot \n Ali asnaashari", fontsize=13)
# xlabel
plt.xlabel("x", fontsize=14)
# ylabel --> latex form
plt.ylabel("$y = x^2$", fontsize=14)
plt.show()
"""

# Part5
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 1, 6, 5, 6, 8, 2, 5, 4, 4]
# create window
plt.figure(figsize=(10, 8))
plt.plot(x, y, linewidth=4, color="blue", linestyle="--", marker="o", markersize=12, markerfacecolor="lightblue",
         markeredgecolor="black")
# title
plt.title("my first plot \n Ali asnaashari", fontsize=13)
# xlabel
plt.xlabel("x", fontsize=14)
# ylabel --> latex form
plt.ylabel("$y = x^2$", fontsize=14)
plt.show()
"""

# Part6
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 1, 6, 5, 6, 8, 2, 5, 4, 4]
# create window
plt.figure(figsize=(10, 8))
plt.plot(x, y, linewidth=4, color="blue", linestyle="--", marker="o", markersize=12, markerfacecolor="lightblue",
         markeredgecolor="black")
# title
plt.title("my first plot \n Ali asnaashari", fontsize=13)
# xlabel
plt.xlabel("x", fontsize=14)
# ylabel --> latex form
plt.ylabel("$y = x^2$", fontsize=14)
# Fully display the numbers on the x-axis
plt.xticks(x)
plt.grid(which="both")
plt.show()
"""