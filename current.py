
import PE
from PE.cores import Array, Dic, Cores, Structures, GraphTheory
import time
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import copy
from itertools import cycle, chain, combinations
from functools import reduce
import scipy.special
from scipy.special import comb
## current

		
#### debug
def p92():
	"""
	debug..
	(EVERY starting number will eventually arrive at 1 or 89.)
	How many starting numbers below ten million will arrive at 89?
	"""
	
	sol = 0
	reached_1 = set()
	reached_89 = set() # early stop
	for n_ in range(2, 10**7):
		if n_ % 100000 == 0:
			print(n_)
		n = n_
		chain = [n_]
		while (n!=1) and (n!=89):
			if (n in reached_1) or (n in reached_89):
				break # early stop
			n = sum([int(s)**2 for s in str(n)])
			chain.append(n)
		
		if n == 1:
			for c in chain:
				reached_1.add(c)
		if n == 89:
			for c in chain:
				reached_89.add(c)


		if (n in reached_89) or (n == 89):
			sol += 1

	return sol# len(reached_89)


if __name__ == "__main__":
	print(p55())
	
