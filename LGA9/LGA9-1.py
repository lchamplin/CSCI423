#!/usr/bin/env python3
import math
import sys

class Welford:
        def __init__(self) -> None:
                self.x = 0.0
                self.v = 0.0
                self.n = 0
                self.points = []
	
        def algorithm(self):
                n = 0
                xbar = 0.0
                v = 0.0
                i = 0
                while i<len(self.points):
                        x = self.points[i]
                        i+=1
                        n+=1
                        d = x - xbar
                        v = v + d * d * (n-1)/n
                        xbar = xbar + d/n
                s = math.sqrt(v/n)
                self.n = n
                self.x = xbar
                self.v = s

        def add_point(self, point: float):
                self.points.append(point)

        def get(self):
                self.algorithm()
                print("n:", self.n, "xbar:", self.x, "s:", self.v)


def main(filename):
        file = open(filename)
        w = Welford()
        for line in file:
                w.add_point(float(line.strip()))
        w.get()

main(sys.argv[1])