# import fundamentals
# from fundamentals.cores import Array, Dic, Cores, Structures, GraphTheory
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

def p86_euclid_1():
	"""
	(construct the possible (a, b, c) from euclid, will have repetitive computations with incorrect heuristics, and will need heuristic to choose the search region so that it's most cost-effective to reach M)
	
	Consider a^2 + b^2 = c^2
	According to Euclid's formula https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

	The primitive (a, b, c) (i.e. could be used to generate other (ka, kb, kc)) is to represented as
	a = m^2 - n^2
	b = 2*m*n
	c = m^2 + n^2
	where m, n are co-primes and one of them is even. (if m, n both odd, then a, b, c are all even then not primitive)
	e.g. (3, 4, 5) -> m = 2, n = 1


	Therefore we first generate the valid (a, b, c) for (m_max, n_max), 
	notice that a >= b, and a > c, the ordering of (b, c) is undetermined

	Same as in p86_bruteforce, store the valids in the matrix Mat:M*M*M
	Use heuristics to choose m_max, n_max until the sum(Mat) >= _required_

	"""

	MAXINT = 2000 #10000 
	required = 10**6

	# valid = np.zeros((MAXINT, MAXINT, MAXINT)) # costly, use set instead (Python has good optimization for set)
	valid = [0 for M in range(1, MAXINT+2)] 
	# valid = [set() for M in range(1, MAXINT+2)]

	def gcd(*numbers):
		d = reduce(lambda x,y: math.gcd(x,y), numbers)
		return d

	for n in range(1, MAXINT+1): # n > 1, 2*n*1 <= 2*MAXINT
		###########
		#debug
		# if n == 1:
		# 	print(1)
		#debug
		###########
		for m in range(n+1, min((2*MAXINT)//(2*n), math.ceil(math.sqrt(n**2 + 2*MAXINT)))+1): # m > n; {m**2 - n**2, 2*m*n} <= 2*MAXINT
			if (gcd(n, m) > 1) or (n%2 != 0 and m%2 != 0): # only keep primitive
				continue

			###########
			#debug
			# if m == 2 and n == 1:
			# 	print("m, n:", m, n)
			#debug
			###########
			a, b, c = [m**2-n**2, 2*m*n, m**2+n**2] # a != b
			###########
			#debug
			if m == 2 and n == 1:
				print("a, b, c:", a, b, c)
			#debug
			###########

			assert(a != b)
			# a, b, c are co-primes

			# 1. k*a=A, k*b=B+C: A**2 + B**2 + C**2 + 2*B*C
			# check if other combination for (A, B, C) yields shorter path length
			# that is 
			#  (A+B, C): A**2 + B**2 + C**2 + 2*A*B
			#  (A+C, B): A**2 + B**2 + C**2 + 2*A*C
			# So the possible (A, B, C) requires that A >= C, and A >= B
			#
			# Therefore all the inequalities:
			# A >= B (*) 
			# A >= C: k*b-B <= A, B >= k*b-A > 0 (***); A<k*b, k*a<k*b, a<b (**)
			# let B >= C; (****)
			# ka < MAXINT, kb < 2*MAXINT (*****)
			for k in range(1, min(MAXINT//(a), 2*MAXINT//(b))+1):  #
				###########
				#debug
				# if m == 2 and n == 1:
				# 	print("A:", k*a)
				#debug
				###########
				A = k*a
				for C in range(max(1, k*b-A), min(A, (k*b)//2)+1): 
					B = k*b - C  # >= A
					###########
					#debug
					# if m == 2 and n == 1:
					# 	print("a=A, b=B+C, FOUND:", A, B, C)
					#debug
					###########
					valid[A] += 1
					# valid[A].add((A, B, C))
					"""
					From one (a1, b1, c1) -> (k1*a1, k1*b1, k1*c1)
					will not exist another (a2, b2, c2) -> (k2*a2, k2*b2, k2*c2) == (k1*a1, k1*b1, k1*c1)
					"""
			# 2. k*a=B+C, k*b=A
			for k in range(1, min(2*MAXINT//(a), MAXINT//(b))+1):
				###########
				#debug
				# if m == 2 and n == 1:
				# 	print("A:", k*b)
				#debug
				###########
				A = k*b
				for C in range(max(1, k*a-A), min(A, (k*a)//2)+1):
					B = k*a - C
					###########
					#debug
					# if m == 2 and n == 1:
					# 	print("a=B+C, b=A, FOUND:", A, B, C)
					#debug
					###########
					valid[A] += 1
					# assert(A >= C and A >= B)
					# valid[A].add((A, B, C))

		print(sum(valid))
		# print(sum([len(s) for s in valid]))


	print("fill finished")
	valid_cnt = valid 
	# valid_cnt = [len(s) for s in valid]
	M_valid_cnt = [sum(valid_cnt[:m]) for m in range(1, len(valid_cnt)+1)]

	
	for i, M_cnt in enumerate(M_valid_cnt):
		if M_cnt >= required:
			print(i)
			break
	if i == len(M_valid_cnt) - 1:
		print("increase t_max")

	return valid  # debug, compare with bruteforce to see which ones are missing
	# return


def p86_bruteforce():
	"""
	(Find the least value of M such that the number of solutions first exceeds one million 
	1, 000, 000 = 10 ** 6 = (10**2)**3.-- M > 100)
	Try a simple brute-force, 
	If we have chosen M, then choose (a, b, c) from M*M*M (let a >= b >= c), the 3 routes have length 
	sqrt(a**2 + (b+c)**2), 
	sqrt(b**2 + (a+c)**2), 
	sqrt(c**2 + (a+b)**2).
	
	Now the number of solutions has not exceed the required, check for M+1, the new triples will be
	For the triple (M, M, M)  -> (M+1, M+1, M+1), (M+1, M+1, M), (M+1, M, M) # has three values
	For the triple (M, M, *<M)  -> (M+1, M+1, *), (M+1, M, *) # * has 2 * (M-1) values, [1, ..., M-1]
	For the triple (M, *<M, *<M) -> (M+1, *, *),  # (*, *) has (M-1) + (M-2) + ... + 1 = M(M-1)/2 values

	Therefore, the computation complexity for M+1 is
	C(M+1) = C(M) + (3 + 2*(M-1) + M(M-1)/2) = C(M) + O(M^2)
	C(1) = 1
	Therefore, C(M) < 1 + (1 + 1^2) + (1 + 1^2 + 2^2) + ... + (1 + 1^2 + 2^2 + 3^2 + ... + (M-1)^2)
				    < sum(O(n^3))
				    < O(n^4) 
	
	"""
	MAXINT = 101 #10000  #
	valid = np.zeros((MAXINT, MAXINT, MAXINT))

	required = 2000 #10**6

	def gcd(numbers):
		d = reduce(lambda x,y: math.gcd(x,y), numbers)
		return d

	def check(a, b, c):
		s1 = math.sqrt(a**2 + (b+c)**2) 
		s2 = math.sqrt(b**2 + (a+c)**2) 
		s3 = math.sqrt(c**2 + (a+b)**2)

		l = [s1, s2, s3]
		if min(l) % 1 == 0:
			return 1
		else:
			return 0

	
	# get initial triplets
	T = [[1, 1, 1]]
	cnt = 0  # first triple yields sqrt(5)

	for M in range(2, MAXINT):
		if M % 50 == 0:
			print(M, cnt)
		new_test = []
		for t in T:
			a, b, c = t
			if a == b == c == M-1:
				new_test.extend([(a+1, b+1, c+1), (a+1, b+1, c), (a+1, b, c)])
			elif a == b == M-1:
				new_test.extend([(a+1, b+1, c), (a+1, b, c)])
			elif a == M-1:
				new_test.extend([(a+1, b, c)])
		T.extend(new_test)

		# print(new_test)

		for t in new_test:
			# only check when gcd(a, b, c) > 1
			GCD = gcd(t)
			if GCD > 1:
				if valid[t[0] // GCD, t[1] // GCD, t[2] // GCD]:
					cnt += 1 # use stored result
			else: # 
				c = check(t[0], t[1], t[2])
				cnt += c
				if c:
					valid[t[0], t[1], t[2]] = 1
					# print(t)

		if cnt >= required:
			# print(M)
			break

	# assert([a >= b >= c for a, b, c in valid])
	# print(len(set([tuple(t) for t in valid])))
	return np.nonzero(valid)
	# return # will not compute beyond M=300


if __name__ == "__main__":
	p86_euclid_1()
	# M = 100
	# res_1 = p86_euclid_1()
	# res_2 = p86_bruteforce()

	# l1 = []
	# for s in res_1:
	# 	for t in s:
	# 		l1.append(t)

	# l2 = []  # gt
	# for t in zip(*res_2):
	# 	for n in range(1, M):
	# 		if n * t[0] < M:
	# 			l2.append((n*t[0], n*t[1], n*t[2]))
	# 		else:
	# 			break

	# print(set(l2) - set(l1), set(l1) - set(l2)) # missing
