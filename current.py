from fundamentals.cores import Array, Dic, Cores, Structures, GraphTheory
import time
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import copy
from itertools import cycle
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

def p86():
	"""
	Cuboid route problem

	"""
	# get all the primitive Pythagorean triplets (a, b, c) using Euclid's formula
	# for M > m+n > sqrt(m^2+n^2)

	# gcd(m, n) = 1 and m+n=even (odd+even), n<m, then
	# a = m^2-n^2, b = 2*m*n, c = m^2+n^2 , a<b<c
	M_sqrt = 100
	primes = Cores().primesBelowN(M_sqrt)
	# print(primes)

	def sequence_gen(M):
		"""Generate the above seq. """
		# iterate order, (fixing m+n), (1, 2), | (1, 3), (2, 2), | (1, 4), (2, 3), | (1, 5), (2, 4), | (1, 6), (2, 5), (3, 4)
		res = []
		for k in range(3, M):
			for n in range(1, math.floor(k/2)):  # 
				m = k - n  # m > n
				if n == 1:
					if (m+n) % 2 == 1:
						res.append((n, m))
				else:
					m_p = list([p for (p, a, N) in Cores().primeFactorDecompose(m, primes)])
					n_p = list([p for (p, a, N) in Cores().primeFactorDecompose(n, primes)])
					if len(set(m_p).intersection(n_p)) == 0:
						res.append((n, m))

		return res

	primitive_triplets_M = sequence_gen(M_sqrt)
	print(len(primitive_triplets_M))

	max_primitive_triplet = max(primitive_triplets_M, key = lambda t:t[0]**2+t[1]**2)
	max_c = max_primitive_triplet[0]**2 + max_primitive_triplet[1]**2

	# fill the rest of non-primitive (n, m) pairs
	non_primitive_triplets_M = []
	for (n, m) in primitive_triplets_M:
		k = 2
		c = (k*m)**2 + (k*n)**2
		while c < max_c: # fill to the boundary of the primitive_M  # todo: is this the true boundary?
			non_primitive_triplets_M.append((k*n, k*m))
			k += 1
			c = (k*m)**2 + (k*n)**2


	print(len(primitive_triplets_M) + len(non_primitive_triplets_M))
	# assert(len(primitive_triplets_M) + len(non_primitive_triplets_M) > 10**6)
	# merge primitive_triplets and non-primitive ones,  sort by value c, and get the c for the 1,000,000th triplets
	triplets_M = sorted(primitive_triplets_M + non_primitive_triplets_M, key = lambda t:2*t[0]*t[1])
	

	return triplets_M[2000], triplets_M[2000-1], # todo: restrict to M*M*M
	# return triplets_M[10**6], triplets_M[10**6-1] 
	# ((690, 1451), (549, 1510))

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


def p88():
	"""
	sum-product
	solve the earlier factor decomposition related problems first
	"""
	pass


if __name__ == "__main__":
	print(p63())

