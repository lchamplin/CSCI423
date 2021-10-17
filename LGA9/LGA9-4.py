#!/usr/bin/env python3
import math
import sys
	
def mean(points):
        mean = 0.0
        for point in points:
                mean = mean + point
        return mean/len(points)

def two_pass(points, mean):
        total = 0.0
        for point in points:
                total = total + (mean - point)**2  
        return mean, math.sqrt(total/len(points))  


def one_pass(points):
        n = 0.0
        sum_xi_2 = 0.0
        sum_xi = 0.0
        i = 0
        while i<len(points):
                x = points[i]
                i+=1
                n+=1
                sum_xi = sum_xi + x
                sum_xi_2 = sum_xi_2 + x**2
        mean = sum_xi/n
        s = (sum_xi_2/n) - mean**2
        return mean, s
        

def main(filename):
        points = []
        file = open(filename)
        for line in file:
                points.append(float(line.strip()))
        print("one pass: ", one_pass(points))
        print("two pass: ", two_pass(points, mean(points)))

main(sys.argv[1])