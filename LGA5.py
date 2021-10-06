#!/usr/bin/env python3
import random
import math
import matplotlib.pyplot as plot

# count = 0

# for i in range(1, 1001):
#         rand1 = random.uniform(0, 1)
#         rand2 = random.uniform(0, 1)
#         if rand1 < rand2:
#                 x=rand1
#                 y=rand2-rand1
#                 z=1-rand2
#         else:
#                 x=rand2
#                 y=rand1-rand2
#                 z=1-rand1
#         if x+y>z and x+z>y and y+z>x:
#                 count+=1

# print(count)

# c_count = 0 

# for i in range(1, 1001):
#         p1x = random.uniform(0, 1)
#         p1y = random.uniform(0, 1)
#         p2x = random.uniform(0, 1)
#         p2y = random.uniform(0, 1)

#         a = abs(p1x-p2x)
#         b = abs(p1y-p2y)
#         c = math.sqrt(a**2 + b**2)
#         c_count+=c

# print(c_count/1000)




arr = []

for a in range(1, 1001):
        count = 0
        for i in range(1, 10001):
                theta = random.uniform(0, 1)*2*math.pi
                radius = random.uniform(0, 1)*1000
                x = radius*math.cos(theta)
                y = radius*math.sin(theta)

                if math.hypot(x, y) < a:
                        count+=1
        arr.append(count/10000)
plot.plot(arr)
plot.show()

