#!/usr/bin/env python3
import random
import math
from matplotlib import scale
import matplotlib.pyplot as plt
import sys
import numpy as np

# print(sys.argv) #points (x1,y1),(x2,y2),(x3,y3)
# x1 = int(sys.argv[1])
# y1 = int(sys.argv[2])
# x2 = int(sys.argv[3])
# y2 = int(sys.argv[4])
# x3 = int(sys.argv[5])
# y3 = int(sys.argv[6])

# print(x1, y1, x2, y2, x3, y3)

# def area(x1, y1, x2, y2, x3, y3):
#     return abs((x1 * (y2 - y3) + x2 * (y3 - y1)+ x3 * (y1 - y2))/ 2.0) 

# tri_area = area(x1, y1, x2, y2, x3, y3)

# # triangle is guaranteed to be in quadrant
# x_bound = max(x1, x2, x3)
# y_bound = max(y1, y2, y3)

# count = 0
# xs = []
# ys = []
# tri_xs = []
# tri_ys = []

# for i in range(1, 5001):
#         x = random.uniform(0, 1)*x_bound
#         y = random.uniform(0, 1)*y_bound

#         A1 = area(x, y, x2, y2, x3, y3)
#         A2 = area(x1, y1, x, y, x3, y3)
#         A3 = area(x1, y1, x2, y2, x, y)

#         if tri_area == (A1+A2+A3):
#                 count+=1
#                 tri_xs.append(x)
#                 tri_ys.append(y)
#         else:
#                 xs.append(x)
#                 ys.append(y)
                
# plt.plot(xs, ys, 'o', color='black', markersize=0.5)
# plt.plot(tri_xs, tri_ys, 'o', color='blue', markersize=0.5)
# plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1])
# plt.show()

# print(count)

count = 0
xs = []
ys = []
under_xs = []
under_ys = []

for i in range(1, 101):
        x = random.uniform(0, 1)*2*math.pi
        y = random.uniform(0, 1)*2 - 1
        if y < math.sin(x):
                count+=1
                under_xs.append(x)
                under_ys.append(y)
        else:
                xs.append(x)
                ys.append(y)

plt.plot(xs, ys, 'o', color='black', markersize=0.5)
plt.plot(under_xs, under_ys, 'o', color='blue', markersize=0.75)
sinx = np.linspace(0,2*math.pi,512)
siny = np.sin(sinx)
plt.plot(sinx, siny)


plt.show()