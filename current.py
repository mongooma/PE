from fundamentals.cores import Array, Dic, Cores, Structures, GraphTheory
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

def p55():
	"""
	How many Lychrel numbers are there below ten-thousand?
	(if not turn palindrome in 50 iters then announce it to be Lychrel)
	"""
	sol = 0
	for n in range(1, 10001):
		t = 1
		while t <= 50:
			# reverse, add
			n_ = str(n)[::-1]
			if len(str(int(n_))) == len(str(n)): # valid reverse?
				n += int(n_)
				if (str(n)[::-1] == str(n)) and (len(str(n)) != 1):
					sol += 1
					break
			else:
				break
			t += 1

	return sol  # error?
####pending
def p46():
	"""
	have a good storage plan for the computed

	use a generation method
	the smallest odd composite that cannot be written as the sum of a prime and twice a square
	"""

	MAX = 100000 # top MAX odd composite
	primes = Cores.primesBelowN(MAX)
	current_filled = np.nans(MAX)
	squares_add = []
	for n in range(1, MAX):
		squares_add.append([])
		last_add = squares_add
	pass


if __name__ == "__main__":
	p86()
	
