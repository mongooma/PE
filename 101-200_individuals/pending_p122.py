import numpy as np
from math import ceil, log

def p122(N):
	"""
	(hypothesis:)

	The minimum mutiplication time for N:

	when N = 2^p, takes p times
	when N = 2^p * k + k, (2^p + 1) = N / k, takes 1 + (p + T(k)) times

		e.g.    15 = 5 + 2 * 5
		       /  \
		      5   10 = 2 * 5
		         /  \
                5    5

         T(5) -> 5 = 2^2 + 1, T(5) = 2 + 1 = 3
	when N cannot be represented as above forms, 
		if N is odd, it takes T(N//2) + 2 times
		if N is even, it takes T(N//2) + 1 times

	"""

	def gather(n):
		if sum([int(i) for i in bin(n)[2:]]) == 1: # full power of 2
			# print(n, "full power")
			return ceil(log(n)/log(2))
		else:
			s = 1
			p = 0
			min_res = n
			while 1:
				s *= 2
				p += 1
				if n % (s+1) == 0:
					k = n // (s+1)
					min_res = min(min_res, 1 + p + gather(k))
					# e.g. 15 = 12 + 3 = 10 + 5, multiple ways

				if s > n:
					break
			
			if min_res < n:
				return min_res

		# print(n, "other")
		if n % 2 == 0:
			return gather(n//2) + 1
		else:
			return gather(n//2) + 2

		return min_res

	print(gather(15))  # debug

	ms = 0
	for k in range(1, N+1):
		res = gather(k)
		print(k, res)
		ms += res

	return ms  # error

if __name__ == "__main__":
	print(p122(200))

