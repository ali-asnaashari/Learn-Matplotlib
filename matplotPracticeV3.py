import matplotlib.pyplot as plt
import numpy as np
import calendar

x = list(range(1, 13))
y = np.random.randint(20, 60, 12)

# Part1
'''
plt.bar(x, y)
plt.show()
'''

# Part2
'''
fig = plt.figure(figsize=(15, 10))
plt.bar(x, y)
plt.xticks(range(1, 13), calendar.month_name[1:], fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel("sales", fontsize=14)
plt.show()
'''

# Part3
fig = plt.figure(figsize=(15, 10))
plot1 = plt.bar(x, y)
plt.xticks(range(1, 13), calendar.month_name[1:], fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel("sales", fontsize=14)
for rect in plot1:
    # print(rect)
    height = rect.get_height()
    width = rect.get_width()
    xpos = rect.get_x()
    color = rect.get_facecolor()
    # ha = horizontal alignment
    plt.text(xpos + width / 2, height * 1.01, f'{height}', fontsize=14, ha='center', color=color)
plt.show()
