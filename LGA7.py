#!/usr/bin/env python3
import random
import math
from matplotlib import scale
import matplotlib.pyplot as plt
import sys
import numpy as np


def generate():
        a = []
        r = []
        r_1 = random.uniform(0, 2)
        a.append(r_1)
        r.append(r_1)
        i = 2
        while(i<1001):
                r_i = random.uniform(0, 2)
                a_i = a[i-2] + r_i
                a.append(a_i)
                r.append(r_i)
                i+=1
        return a, r


(a1, r1) = generate()
(a2, r2) = generate()
(a3, r3) = generate()
(a4, r4) = generate()
(a5, r5) = generate()
(a6, r6) = generate()
(a7, r7) = generate()
(a8, r8) = generate()
(a9, r9) = generate()
(a10, r10) = generate()

a = np.concatenate((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
r = np.concatenate((r1, r2, r3, r4, r5, r6, r7, r8 ,r9, r10))

mean = np.mean(r)
sd = np.std(r)

print("mean: ", mean)
print("standard deviation: ", sd)

y = []
for i in range(1, 10001):
        y.append(i/10000)

a.sort()
plt.plot(a, y)
plt.show()

r.sort()
plt.plot(r, y)
plt.show()