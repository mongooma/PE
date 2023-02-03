from fundamentals.cores import Cores, Structures, GraphTheory, Array
import time
import sys
import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
import copy
from itertools import cycle, chain, combinations
from collections import Counter

def p101():
	"""
	Polynomial fitting problem but only on integer
	"""

	def f(n):
		return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

	def poly(p, x):
		n = len(p) - 1 # highest order
		res = 0
		for i, p_i in enumerate(p):
			res += p_i * x ** (n-i)
		return res

	def fit_poly_n(x, y, n):
		"""
		Given n (x, y), fit a n-th order polynomial
		"""
		p = np.polyfit(x, y, n) # simple linear algebra

		for p_i in p:
			assert(p_i == int(p_i))

		return p

	s = 0
	series = [f(n) for n in range(1, 12)]  # only have misfit for <= 9th order
	print("correct seq:", series)

	for i in range(1, len(series)): # fit till 10 numbers 
		p = np.polyfit(range(1, i+1), series[:i], deg=i-1)
		for j in range(1, i+1):
			fit_n = poly(p, j)
			assert(abs(fit_n - series[j-1]) < 0.1)
		BOP = poly(p, i+1)
		assert(abs(fit_n - series[i]) > 1)
		# print('\n')
		s += BOP

	return s

def p102():
	"""
	(The linear programming problem)
	(rotations of vectors -- Easy for Physics students) √
	
	Fact: Of an enclosed region, for every point X on the boundary B, there is an e_X point towards the "inside" of the region. From X going to X + d(X), the derivative vector being from v1 = (1, df(X)) to v2 = (1, df(X+d(X))), suppose v2 is rotated from v1 using the matrix R: v2 = R.dot(V1), then e_X+d(X) = e_X.dot(R) 

	------------------------

	Suppose the data is given as A(X_A, Y_A), B(X_B, Y_B), C(X_C, Y_C), go through the edges as A->B->C. No matter if the going-through is clockwise or counter-clockwise, first get e1 for AB, e1 is chosen as either of the two possible normal vectors:

	(-1, (B[0] - A[0])/B([1]-A[1])), (1, -(B[0] - A[0])/B[1]-A[1]))

	calculate R_AB_BC = [[cos(theta), -sin(theta)], 
					  [sin(theta), cos(theta)]]
				   = R_BC_I X (R_AB_I)^{-1} 
				   = [[AB[0]*BC[0]+AB[1]*BC[1], AB[1]*BC[0]-AB[0]*BC[1]], 
					  [AB[0]*BC[1]-AB[1]*BC[0], AB[0]*BC[0]+AB[1]*BC[1]]]

	# first rotate AB back to (x, 0) then rotate from (x, 0) to BC
	Notice the columns are exactly the image of the vectors. 

	Similarly compute the rotation matrix R_BC_CA. 

	R_BC_CA = [[BC[0]*CA[0]+BC[1]*CA[1], BC[1]*CA[0]-BC[0]*CA[1]], 
			   [BC[0]*CA[1]-BC[1]*CA[0], BC[0]*CA[0]+BC[1]*CA[1]]]

	Then e2 = R_AB_BC.dot(e1), e3 = R_BC_CA.dot(e2).
	
	* Refer to https://math.stackexchange.com/questions/3563901/how-to-find-2d-rotation-matrix-that-rotates-vector-mathbfa-to-mathbfb
	about this part. 

	Then calculate sign(<e1, e1*>), sign(<e2, e2*>) and sign(<e3, e3*>) where e* is the normal vector pointed towards origin (0, 0) of respect edge vectors. But sign(<e, e*>) = sign(<e, p>), where p is (-x, -y) with arbitrary (x, y) on the edge. Therefore calculate s1 = sign(<e1, A>), s2 = sign(<e2, B>) and s3 = sign(<e3, C>). 

	If s1, s2, s3 all >=0 or <=0. Then the origin point is in the closed area.
		This will also fit for some node on the origin, or some edge on the origin.


	-----------------------------


	"""

	def sign(n):
		if n > 0:
			return 1
		elif n < 0:
			return -1
		else:
			# print("sign: not applicable")
			return 0

	def check(A, B, C):
		A = np.array(A)
		B = np.array(B)
		C = np.array(C)
		AB = B-A
		BC = C-B
		CA = A-C
		e1 = np.array([-(B[1]-A[1]), B[0]-A[0]])

		R_AB_BC = np.array([[AB[0]*BC[0]+AB[1]*BC[1], AB[1]*BC[0]-AB[0]*BC[1]], 
				   [AB[0]*BC[1]-AB[1]*BC[0], AB[0]*BC[0]+AB[1]*BC[1]]])
		R_BC_CA = np.array([[BC[0]*CA[0]+BC[1]*CA[1], BC[1]*CA[0]-BC[0]*CA[1]], 
			       [BC[0]*CA[1]-BC[1]*CA[0], BC[0]*CA[0]+BC[1]*CA[1]]])
		e2 = R_AB_BC.dot(e1)
		e3 = R_BC_CA.dot(e2)

		s1 = sign(e1.dot(A))
		s2 = sign(e2.dot(B))
		s3 = sign(e3.dot(C))

		if all(np.array([s1, s2, s3]) >= 0) or all(np.array([s1, s2, s3]) <= 0):
			return 1
		else:
			return 0

	corrs = ''''''
	cnt = 0
	for corr in corrs.split('\n'):
		l = [float(i) for i in corr.split(',')]
		A, B, C = l[:2], l[2:4], l[4:]
		cnt += check(A, B, C)


	# A, B, C = [-340,495], [-153,-910], [835,-947] #A(-340,495), B(-153,-910), C(835,-947)
	# A, B, C = [-175,41], [-421,-714], [574,-645]
	# A, B, C = [0.5, -1], [1, 0], [0, 1]
	# A, B, C = [3, 2], [-2, 3], [-2, 2]
	# print(check(A, B, C))


	return cnt



def p103():
	"""
	NOTE: the problem specifies for subset pairs to be "disjoint", so the check could be easier done

	correct answer: 
	  20, 31, 38, 39, 40, 42, 45

	CP: constraint programming
	(A hardcore problem about find a search path to the optimum)
	https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p103.py
	# keypoints:
	# find possible sum 
	# use Knapsack as a sub-routine
	# binary search (determine a maxval and a minval)
	"""

	"""
	This problem has several key components:
	1. Limit the search. 
		According to the traditional way of solving EP problems, we have to search in the solution space. Infinite and heuristically growing the solution will not lead to meaningful comparison. 
		There is no explanation to why the lowest n of S_k should be in the middle of the previous S_k-1. So suppose we search the 7 numbers within the interval [1, MAXINT]

	
	2. Construct the ordering:
		2.1 Efficiently compare the subsets in the power set. Find an ordering of these comparisons.

		2.2 Find the growth/deduction function between finding S_k-1 and S_k. Since clearly a successful S_k indicates a successful S_k-1, so every successful S_k is constructed from a successful S_k-1. 


	Now we separately target the components:
		
	1. (1) Suppose we have found a S_k = 7 * En, then we could stop searching for the min_n = E_n.
	   (2) According to 2.2 (1), we order the search branches from the lowest possible n_k to the highest. However, when we have found a S_k from an earlier path, we should not stop the further searches. Since such occasion might exist:

	   		n_11, n_12, n_13, ...,          n_1k
	   		n_21, n_22,      n_23, ..., n_2k   * better solution
	
	2. 	
		2.1 If every m-set having sum larger than all m-1-set, then every m-set will have sum larger than l-set, 0<l<=m-1; and also every p-set will have sum larger than all m-1-set, k>=p>=m.
		Therefore, for a k-set, we only need to guarentee every m-set having sum larger than all m-1-set, m=2, 3, 4, ..., k. 
			That is, min(m-set) > max(m-1-set). 
				(1) That is, {n_1, n_2, ..., n_m} > {n_k-(m-2), ..., n_k-1, n_k}

		2.2 Without loss of generality, let's grow S_k from the right of S_k-1. (But notice we will not necessary grow S*_k from S*_k-1 this way) Suppose we have S_k-1:

			n_1, n_2, ..., n_k-1

		And we need to have
			n_k-2 + n_k-1 > n_k
		But a better limit would be
			n_1 + n_2 > n_k

		(1) So we search between [n_k-1 + 1, n_1 + n_2 - 1] for n_k. Ordering the next searches from the lowest to the highest in possible n_k. 
		n_k has to be larger than n_k-1 because if we have a S_k = {n_1, n_2, ..., n*_k, n_k-1} then we have messed up the ordering of the search. That is, this search result should be on a different branch.

		(2) Therefore, by keep growing S_k from S_k-1 in this way, we will have disjoint search branches with no redundancie. 

			2.2.1 Find a possible construction for S_3:
			Since every 2-set will have sum larger than the 1-set, we have a possible S_3:
				n, n+1, 2n+2 for k = 3 (when n=1, optimal)
			(1) Actually, the general construction for S_3 is
				* n, n+m, [max(m, n+m+1)=n+m+1, 2n+m] for arbitrary n, m
			where we start the searches from. 

	"""
	# subset check
	def check(S, k):
		# (ii) if |S(B)| > |S(C)| then sum(S(B)) > sum(S(C)) 
		for m in range(2, k):
			if sum(S[:m]) <= sum(S[-(m-1):]):
				# print(S, 'fail', S[:m], S[-(m-1):])
				return 0

		# (i) unique subset sums
		# given condition (ii) fulfilled, check for equal size subsets
		# this step could be optimized (see nayuki's solution; and another way is according to p106)
		# yet test for brute-force complexity first (take 10 min)

		for s in range(2, k):
			subset_sums = [sum(l) for l in list(combinations(S, s))]
			if len(np.unique(subset_sums)) < len(subset_sums):
				# print(S, 'fail subset for', s)
				return 0

		# print(S, "passed")
		return 1

	# def _check(S, k):

	# 	def powerset(iterable):
	# 	    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
	# 	    s = list(iterable)
	# 	    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
	# 	ps = list(powerset(S))

	# 	# (i)
	# 	subset_sums = [sum(l) for l in ps]
	# 	if len(np.unique(subset_sums)) < len(subset_sums):
	# 		print('violate (i)', Counter(subset_sums),
	# 			sorted(zip(ps, subset_sums), key=lambda t:t[1]))
	# 		return 0

	# 	# (ii)
	# 	subset_pair = [sp for sp in combinations(ps, 2)]
	# 	for s1, s2 in subset_pair:
	# 		if len(s1) > len(s2):
	# 			if sum(s1) < sum(s2):
	# 				print(s1, s2, 'violate (ii)')
	# 				return 0
	# 		elif len(s1) < len(s2):
	# 			if sum(s1) > sum(s2):
	# 				print(s1, s2, 'violate (ii)')
	# 				return 0

	# 	print("passed")



	# recursion
	def explore(S, k, k_max):

		for next_n in range(S[k-1]+1, S[0]+S[1]):
			success = check(S+[next_n], k+1)
			if success:
				# print(S+[next_n], k+1)
				if (k+1) < k_max:
					S, SIGSTOP = explore(S+[next_n], k+1, k_max)
					if SIGSTOP: # found solution, stop future computations
						continue
						# return S, SIGSTOP # send S_k and stop signal to the parent node
				else: # send stop signal upwards to the root and stop any computation going on in the sub-branches
					print("FOUND", S+[next_n], sum(S+[next_n]))
					return S+[next_n], 1
		
		return S[:-1], 0  # unable to find from this node, go back to the parent node and continue search from its previous state

	# search main
	def search(n, k_max):

		for m in range(1, MAXINT):
			for i in range(n+m+1, 2*n+m+1):
				S_0 = [n, n+m, i]
				# print('base', S_0)
				S, SIGSTOP = explore(S_0, 3, k_max)
				if SIGSTOP:  # if found
					return S, sum(S) # return the first success

		return None, None


	
	MAXINT = 100
	MAXMIN_N = 25 # heuristic
	# min_S = []

	# n = 1: {1}
	# n = 2: {1, 2}
	# n = 3: {2, 3, 4}
	# n = 4: {3, 5, 6, 7}
	# n = 5: {6, 9, 11, 12, 13}
	# n = 6: {11,   18, 19, 20, 22, 25} not {11, 17, 20, 22, 23, 24},     [11, 17,     20, 21, 23, 25]

	k_max = 7
	for n in range(19, MAXMIN_N):
		# print('start at', n)
		print(n)
		# search a S_7 start from n
		S, _ = search(n, k_max)
		# if min_sum_ < min_sum:
		# 	min_sum = min_sum_
		# 	min_S = S 
		if S:
			return S

	# check([19, 30, 37, 38, 39, 41, 44], 7)

def p105():
	"""
	related to p103, identify the S set
	"""

	# from p103; subset check
	def check(S, k):
		S = sorted(S)
		# (ii) if |S(B)| > |S(C)| then sum(S(B)) > sum(S(C)) 
		for m in range(2, k):
			if sum(S[:m]) <= sum(S[-(m-1):]):
				# print(S, 'fail', S[:m], S[-(m-1):])
				return 0

		# (i) unique subset sums
		# given condition (ii) fulfilled, check for equal size subsets
		# this step could be optimized (see nayuki's solution)
		# yet test for brute-force complexity first (take 10 min)

		for s in range(2, k):
			subset_sums = [sum(l) for l in list(combinations(S, s))]
			if len(np.unique(subset_sums)) < len(subset_sums):
				# print(S, 'fail subset for', s)
				return 0

		# print(S, "passed")
		return 1

	candids = ''''''

	candids = [[int(n) for n in l.split(',')] 
				for l in candids.split('\n')]

	res = 0
	for candid in candids:
		if check(candid, len(candid)):
			res += sum(candid)

	return res

def p106():
	"""
	from p103, 
	the check for (i) could be optimized
	there are some subset-pairs not need to go through (i) checking

	that is 
	(0) if |B| == |C|, then need to check for (i)
	(1.1) if B={b1, b2, ..., bm} and C={c1, c2, ..., cl}
	and bm < c1 or cl < b1, then the checking for (i) is not needed for (B, C)
	(1.2) check for situations like
		-*--*----*---  B
		---*---*---*-  C

		if c1 > b1, then c2 > b2, ...

	(1) -- take out b1 and cl, then b2 and cl-1, ..., until the extremes are all B or all C
		(... a simpler way is to sequentially compare c1-b1, c2-b2, ...)

	-------------
	Use bit-mask checking to get disjoint subset-pairs
	"""

	# from p103: subset check
	def check(S, k):
		# (ii) if |S(B)| > |S(C)| then sum(S(B)) > sum(S(C)) 
		for m in range(2, k):
			if sum(S[:m]) <= sum(S[-(m-1):]):
				# print(S, 'fail', S[:m], S[-(m-1):])
				return 0

		# (i) unique subset sums
		# given condition (ii) fulfilled, check for equal size subsets -- exactly what p106 asked.


		# this step could be optimized (see nayuki's solution)
		# yet test for brute-force complexity first (take 10 min)

		for s in range(2, k):
			subset_sums = [sum(l) for l in list(combinations(S, s))]
			if len(np.unique(subset_sums)) < len(subset_sums):
				# print(S, 'fail subset for', s)
				return 0

		# print(S, "passed")
		return 1

	def check_1_unneeded(n):
		"""
		n = 4, only 1 of these pairs need to be tested for equality (first rule). 
		Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.
		For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?
		"""

		powerset_ind = range(1, 2**n-1)  # e.g. bin(2**3-1)='0b111'

		def get_bin_digits(n):
			i = 0
			pos = []
			while n // 2 or n == 1:
				if n % 2:
					pos.append(i)
				i += 1
				n = (n-n%2) // 2
			
			return pos


		cnt = 0
		for i, ind1 in enumerate(powerset_ind):
			for _, ind2 in enumerate(powerset_ind[i+1:]):
				if ind1 & ind2 == 0:  # disjoint set
					ind1_bin = get_bin_digits(ind1)
					ind2_bin = get_bin_digits(ind2)
					if len(ind1_bin) == len(ind2_bin):
						#### check if satisfy
						####
						#   *--*--*--
						#    -*--*--*--
						####
						ck = sum([(ind1_bin[i] < ind2_bin[i]) for i in range(len(ind1_bin))])
						if (ck != 0) and (len(ind1_bin)-ck != 0):
							cnt += 1
							# print(bin(ind1), bin(ind2), ck, ind1_bin, ind2_bin)

		
		print(cnt)


		# print(get_bin_digits(n), bin(n))

	for n in [4, 7, 12]:
		check_1_unneeded(n)

def p107():
	"""
	MST problem
	"""
	mat_raw = ''''''

	weighted_edges = []
	nodes = []
	for i, l in enumerate(mat_raw.split('\n')):
		for j, w in enumerate(l.split(',')):
			if w != '-':
				weighted_edges.append((i, j, int(w)))
				nodes.extend([i, j])

	nodes = list(set(nodes))

	MST_edges = GraphTheory().Prim(nodes, weighted_edges)
	max_saving = sum([w for u, v, w in weighted_edges])/2 - \
				sum([w for u, v, w in MST_edges])

	return max_saving



if __name__ == "__main__":
	print(p102())