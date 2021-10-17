#!/usr/bin/env python3
import math
import random
import matplotlib.pyplot as plt


def circle_sim(N):
        radius = 1
        circumference = 2*radius*math.pi
        total = 0
        count = 0
        for i in range(0, N):
                r1 = random.uniform(0, circumference)
                r2 = random.uniform(0, circumference)

                total += 1
                x1 = radius*math.cos(r1)
                y1 = radius*math.sin(r1)
                x2 = radius*math.cos(r2)
                y2 = radius*math.sin(r2)

                dist = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
                if dist > radius:
                        count += 1
        return count/total

def get_stats(array):
        n = 0
        xbar = 0.0
        v = 0.0
        i = 0
        while i<len(array):
                x = array[i]
                i+=1
                n+=1
                d = x - xbar
                v = v + d * d * (n-1)/n
                xbar = xbar + d/n
        s = math.sqrt(v/n)
        return s


N_arr = []
s_arr = []
for k in range (10, 2000, 100):
        for i in range(8, 1601, 16):
                points = []
                for j in range(k):
                        points.append(circle_sim(i))
                s = get_stats(points)
                N_arr.append(i)
                s_arr.append(s)
        plt.plot(N_arr, s_arr, 'o', color='black', markersize=0.5)
        plt.show()



                

