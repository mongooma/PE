import numpy as np
from math import factorial



def p158():
	"""
	
	"Exploring strings for which only one character comes 
		lexicographically after its neighbour to the left"

	"exactly one character comes lexicographically after its neighbour to the left."

	h a t  <- only t comes after its neighbour to the left (a, t)

	only one "wriggle""

	*
	  *     *
	    *      *
	      *       *
  
	choose i out of n, comb(n, i)
	- 1, => (5,4,3) (2, 1) all left larger than the right

	return max(p(n)), n = 2, 3, 4, ..., 26
	"""

	def comb(n, k):
		return factorial(n) / (factorial(k) * factorial(n-k))

	ans = max([comb(26, n) * sum([(comb(n, i)-1) for i in range(1, n)]) for n in range(2, 26+1)]) 
	
	print(comb(26, 3) * sum([(comb(3, i)-1) for i in range(1, 3)]))
	return ans

if __name__ == "__main__":
	print(p158())




