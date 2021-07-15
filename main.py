import matplotlib.pyplot as plt
import numpy as np


def function(x):
    # return x**2
    # return 1 / (1 + np.exp(-x))
    # return 2 * np.sin(x) + 4
    # return np.cos(x) + np.exp(x)
    return np.log2(x)


def draw_rectangle(ax1, ax2, x1, x2, y1, y2, c):
    rectangle_x = [x1, x1, x2, x2, x1]
    rectangle_y = [y2, y1, y1, y2, y2]
    ax[ax1, ax2].plot(rectangle_x, rectangle_y, color=c)


def mensuration_by_parts1(f, ax1, ax2, start, finish, step=0.01):
    s = 0
    x = np.arange(start, finish, step)
    for i in x:
        fi = f(i)
        draw_rectangle(ax1, ax2, i, i+step, 0, fi, 'red')
        s += fi * step
    return s


def mensuration_by_parts2(f, ax1, ax2, start, finish, step=0.01):
    s = 0
    x = np.arange(start, finish, step)
    for i in x:
        fi = f(i+step)
        draw_rectangle(ax1, ax2, i, i + step, 0, fi, 'blue')
        s += fi * step
    return s


start = 4.0
finish = 5.0
step = 0.0001
x = np.arange(start, finish, step)
y = function(x)
fig, ax = plt.subplots(2, 2)
for i in range(2):
    for j in range(2):
        ax[i, j].plot(x, y, color='black')
fig.delaxes(ax[0, 1])
s1 = mensuration_by_parts1(function, 1, 0, start, finish, step=step)
s2 = mensuration_by_parts2(function, 1, 1, start, finish, step=step)
diff = abs(s2 - s1)
print(f's1 = {s1}, s2 = {s2}, diff = {diff}')
plt.show()
