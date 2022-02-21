from fundamentals.cores import Array, Dic, Cores, Structures, GraphTheory
import time
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import copy
from itertools import cycle



def p67():
	"""
	larger scale version of p18
	"""
	triangle = \
	[[int(n) for n in l.split(' ')] for l in """""".split('\n')]
	
	# i-th at n-th row, could only move to i and i+1 at n+1-th row
	# use DP; table

	maximal_L_path = [[0 for i in l] for l in triangle]
	for row_n in range(len(triangle)):
		if row_n == 0:
			maximal_L_path[row_n][0] = triangle[row_n][0]
		else:
			for pos_i in range(len(triangle[row_n])):
				if 0 < pos_i < row_n:
					maximal_L_path[row_n][pos_i] = triangle[row_n][pos_i] + \
							max(maximal_L_path[row_n-1][pos_i],
								maximal_L_path[row_n-1][pos_i-1])
				elif pos_i == row_n:
					maximal_L_path[row_n][pos_i] = triangle[row_n][pos_i] + \
							maximal_L_path[row_n-1][pos_i-1]
				elif pos_i == 0:
					maximal_L_path[row_n][pos_i] = triangle[row_n][pos_i] + \
							maximal_L_path[row_n-1][pos_i]

	return max(maximal_L_path[-1])

def p86():
	"""
	Cuboid route problem

	(search -- solve earlier problems to find a better way than brute-force (?))
	"""
	pass

def p88():
	"""
	sum-product
	solve the earlier factor decomposition related problems first
	"""
	pass


if __name__ == "__main__":
	print(p30())

