# o design an API or object that is initialized
# with ¯x = 0 and v0 = 0, permits data points to be added dynamically, and can return the values n = i, ¯xi and
# s =
# p
# vi/i using a standard interface.

from typing import Tuple


class Welford:
	def __init__(self) -> None:
                self.x = 0
                self.v = 0
                self.points = []
	
	def get_x(self) -> Tuple:
		"""
		return (i, x_i)
		"""
                i = len(self.points) - 1
                return (i, calc_x(i))

        def calc_x(self, i) -> float:
                if i == 0:
                        return 0
                else:
                        return self.calc_x(i-1) + (1/i)*(self.points[i] - self.calc_x(i-1))
	
	
	def get_s(self) -> float:
		"""
		return sqrt(v_i/i)
		"""


		return 0.0
	