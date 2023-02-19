import numpy as np


def p169(N):
	"""
	- "binary tree single side expansion with conflicts"

		e.g. 10  = 2 + 8

		expanding configurations:
		8: 8 8 4 4 2 1 (1) 
		2: 2 1 2 1 1 2 (1)
		(1, 1 not valid) 

			  8           
			/   \
		   4     4     
		 /   \     	
		2     2		  2    <-  conflict; keep expanding
	   / \           /  \
	  1   1         1    1  <- conflict

	  
	-- at every level only choose to expand once
		since if expand >= 2, will cause the downward levels not resolvable


	Numerical example:

	100001000100100
	i    j   k  l


	0. expand: 1  -> +011111...12
	1. the stoppable positions are '0's
	

	2. enumerate:
		i -> expand to end at [i+1, j-1]  -> j, k, l keep expanding
							e.g. 01120 | 1000100100
							  [j+1, k-1]  -> k, l keep expanding 
							  			(any pos before the stopped pos 
							  				has already been expanded once, so cannot be reused)
							  [k+1, l-1]  -> l keep expanding
							  [l+1, ...]

	3. separate the bin into intervals, indexed by the pos of '1's:
			10000 |1000 |100  |100
			i      j     k     l
	   From every '1', choose to 1. not expand, 2. expand to this interval, and 3. expand to some later interval

	   Suppose fixing i to choose to expand within ith interval, has 4 stop positions
			01112 |1000 |100  |100
			i      j     k     l	
	   Then if choose j to expand to jth, calculate until j for 4 * (1+3), 1 for not expanding j

	   if choose j to expand to k > j, calculate until j for 4 * (num_of_zeros_in_kth=2), because that's where
	   j could stop 

	   after finishing for j, suppose it has expanded to k, do the next expanding from l > k
	

	"""
	rep = bin(N)[2:]
	# x.....x......x
	end_pos = [i for i, r in enumerate(rep) if r == '1']
	# valid expansion stop positions
	# [n1, n2, n3, n4]
	l = [] # L = len(end_pos)
	for i in range(len(end_pos)-1):
		l.append(sum([1 for s in rep[end_pos[i]:end_pos[i+1]] if s=='0']))
	l.append(sum([1 for s in rep[end_pos[-1]:] if s=='0']))

	print("intervals:", l)

	total_cnt = [0]

	def segment(i, curr_cnt):
		if i == len(l)-1:
			total_cnt[0] += curr_cnt
			return

		for next_i in range(i+1, len(l)):
			if next_i > i+1:
				segment(next_i, curr_cnt * (l[next_i]))
			else:
				segment(next_i, curr_cnt * (1+l[next_i])) # could choose not expanding

	segment(-1, 1)

	return total_cnt[0]


if __name__ == "__main__":
	print(p169(10**25))







	

