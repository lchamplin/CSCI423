#!/usr/bin/env python3

import sys
import random
import math
import numpy as np


def getTokens( inf ) :
    # word up!
    for lt in [ line.split() for line in inf ] :
        if not lt :
            continue
        for t in lt :
            yield t

def do_sim(N):
        n = 0
        xbar = 0.0
        v = 0.0

        c_i, c_n = 0., 0.
        i   = 0
        a_i, s_i, d_i = 0., 0., 0.
        d_sum, w_sum, s_sum = 0., 0., 0.

        data = open( sys.argv[1] if len(sys.argv) > 1 else "/dev/null" )
        tokens = iter(getTokens(data))


        try :
                while i<N :
                        #print(i)
                        #a_i, s_i = float(next(tokens)), float(next(tokens))
                        a_i = np.random.exponential(1)
                        s_i = np.random.uniform(0, 1)+0.5

                        i += 1

                        if  a_i < c_i :
                                d_i = c_i - a_i
                                d_sum += d_i
                        else :
                                d_i = 0

                        c_i = a_i + d_i + s_i

                        s_sum += s_i
                        w_sum += d_i + s_i

                        if i >= (N-1000):
                                w = d_i + s_i
                                n+=1    
                                d = w - xbar
                                v = v + d * d * (n-1)/n
                                xbar = xbar + d/n

        except StopIteration :
                pass
        except :
                raise

        if i :
                s = math.sqrt(v/n)
                # print( "jobs                 ", i )
                # print( "average interarrival ", a_i/i )
                # print( "average delay        ", d_sum/i )
                # print( "average wait         ", w_sum/i )
                # print( "average service      ", s_sum/i )
                # print( "c_n                  ", c_n)
                # print( "l-bar                ", (i*w_sum)/(c_n*1000))
                # print( "q-bar                ", (i*d_sum)/(c_n*1000))
                # print( "x-bar                ", (i*s_sum)/(c_n*1000))
                # print( "traffic intensity    ", (s_sum/i)/(a_i/i))
        #         def get_stats(array):
        # n = 0
        # xbar = 0.0
        # v = 0.0
        # i = 0
        # while i<len(array):
        #         x = array[i]
        #         i+=1
        #         n+=1
        #         d = x - xbar
        #         v = v + d * d * (n-1)/n
        #         xbar = xbar + d/n
        # s = math.sqrt(v/n)
        # return s
                return w_sum/i, i, s
        data.close()

N = 3000
w_bar, n, s = do_sim(N)
ci_upper = w_bar + 1.96 * (s/math.sqrt(n - 1))
ci_lower = w_bar - 1.96 * (s/math.sqrt(n - 1))
count = 0
for i in range(0, 100):
        w_bar, n, s = do_sim(N)
        if w_bar < ci_upper and w_bar > ci_lower:
              count += 1
print("w-bars (out of 100) in CI: ", count)

