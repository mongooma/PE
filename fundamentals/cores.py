# python 3

import math
import copy
import time
from itertools import cycle
import matplotlib.pyplot as plt
import numpy as np

class Array:
	def __init__(self):
		pass

	def safeSetValue(self, arr, i, val):
		"""
		set arr[i] = val
		if index error, padding 0s first
		"""
		if -len(arr)-1 < i < len(arr):
			arr[i] = val
		else:
			if i > 0:
				padding = abs(i) - (len(arr)-1)
			else:
				padding = abs(i) - len(arr)
			arr = np.append(arr, [0 for j in range(padding)])  # new var.
			arr[i] = val

		return arr

class Dic:
	def __init__(self):
		pass

	def dic_reverse(self, dic):
		"""
		reverse the dic s:t to t:s
		in s:t and t:s one-to-one is not required
		"""

		reversed_dic = dict()
		for s, t_l in dic.items():
			for t in t_l:
				reversed_dic[t] = reversed_dic.setdefault(t, [])
				reversed_dic[t].append(s)

		return reversed_dic

class Cores:
	"""
	Useful knowledge:
	* every prime > 3 could be represented as 6k+/-1:  
		consider mod 6 = (0, 1, 2, 3, 4, 5), then (0), (2), (4) mod 2=0, (3) mod 3=0, 
		if (5)(1) contains non-prime, that is (0) and (1) adjacent yet both non-prime, which will not exist
		therefore (5)(1) must be prime, thus all prime > 3 could be represented as 6k+/-1
	*  Prime number theorem: the number of primes under Pi(x) := x/ln(x), estimated by Gauss and Legendre, proved in 1896

	"""

	def __init__(self):
		pass

	# divisors

	def divisors(self, N):
		"""return the divisors of N"""
		divisors = set()
		for i in range(1, math.floor(math.sqrt(N))+1):
			if N % i == 0:
				divisors.add(i)
				divisors.add(N // i)

		return sorted(list(divisors))


	# primes
	def __primeCheck_recur(self, N):
		"""
		:return True if n is a prime, False otherwise
		will also generate the smallest prime factor
		
		-- fancy recursive, most should be as efficient as primeCheck --

		"""
		# floor(2/n) is the largest factor there is [if N is composite]
		# if !2|n, floor(n/2**(n_2)) is the largest possible factor when 3 is unchecked
		# if !3|n, floor(n/3**(n_3)) is the largest possible factor when 5 is unchecked


		curr_max_candid = math.floor(N/2)
		curr_min_candid = 2
		while curr_min_candid <= curr_max_candid: # limit the prime factor check below curr_max_candida
			if self.primeCheck(curr_min_candid): # if the current candid is prime
			# we are using recursive here, but we suppose the func is written already
				if n % curr_min_candid != 0: # !cur|n
					# move to the next prime 
					curr_min_candid += 1
					while not self.primeCheck(curr_min_candid):
						curr_min_candid += 1
					curr_max_candid = math.floor(n/curr_min_candid)  # update the candidates
				else:
					# print('fin;composite')
					return 0  # composite
		return 1 # if prime

	def primeNext(self, curr_primes, curr_to_check=-1):
		"""
		:param curr_primes: []
		:param current_to_check: if -1 then go to max(curr_primes)+1
		get the next prime
		"""
		if curr_to_check == -1:
			curr_to_check = max(curr_primes) + 1

		is_prime = 0
		while not is_prime:
			is_prime = 1
			# print("curr_to_check", curr_to_check)
			for p in curr_primes:
				if curr_to_check % p == 0:
					curr_to_check += 1
					is_prime = 0

					break

		next_p = curr_to_check
		return next_p

	def primeGenerator(self):
		"""
		:param N: int
		:return a infinite generator of primes below or equal to N in ascending order
		"""
		res = []
		p = 2
		is_prime = 1
		while 1:
			for p_i in res:
				if p % p_i == 0:
					is_prime = 0
					break
			if is_prime == 1:
				res.append(p)
				yield p
			p += 1
			is_prime = 1

	def primeCheck(self, N, prime_factor_candidates = []):
		# possible divisor (if multiple, the smallest) --> 2 to square root 

		candidate_max = int(math.sqrt(N))+1
		if (len(prime_factor_candidates) == 0) or (N > prime_factor_candidates[-1]**2): 
			prime_factor_candidates = self.primesBelowN(candidate_max)

		for next_prime in prime_factor_candidates:
			if next_prime < candidate_max:
				if N % next_prime == 0:
					return 0

		return 1

	def primeFactorDecompose(self, N, prime_factor_candidates=[]):
		"""
		a generator
		"""

		if len(prime_factor_candidates) == 0:
			prime_factor_candidates = self.primesBelowN(N) # more efficient than using primeGenerator
		
		while N > 1:
			for next_prime_factor in prime_factor_candidates:
				if N % next_prime_factor == 0:
					break 
	
			n = 0 
			while N % next_prime_factor == 0:
				N = N // next_prime_factor
				n += 1

			yield [next_prime_factor, n, N]

	def primesBelowN(self, N):
		"""
		Get all the primes below N, return a list
		# use space to save time

		Similar to the "sieve's algorithm" but more efficient

		"""

		if N in [0, 1]:
			return []
		if N < 0:
			return -1

		unchecked = [0] * (N+1)
		largest_unchecked = N
		curr_checked = [1]
		unchecked[1] = 1
		
		p = 2
		curr_primes = [2]
		unchecked[2] = 1

		while p < largest_unchecked: # when this time's prime is left to the largest unchecked non-prime 
			
			# update the current checked numbers
			curr_checked_p = []

			i = 1
			while i < N:
				if unchecked[i] == 1:
					curr = i
					new_curr = curr * p # *p^0
					cnt_i = 1	
					while new_curr <= largest_unchecked:
						curr_checked_p.append(new_curr) #*p^1, *p^2, ...
						new_curr *= p
						cnt_i += 1
					if cnt_i == 1:
						break  # no need to accumulate on larger numbers
				i += 1

			for c in curr_checked_p:
				unchecked[c] = 1  # all the non-primes with prime factors (P, p)
			curr_checked.extend(curr_checked_p)

			# update the largest-unchecked non-prime
			while unchecked[largest_unchecked] == 1:
				largest_unchecked -= 1  # update to the right-most interval between checked-non-primes

			# update the smallest_unchecked non-prime
			smallest_unchecked = p
			while unchecked[smallest_unchecked] == 1:  # might be the most efficient possible... # will set() optimize this?
				smallest_unchecked += 1

			# get the next prime
			
			p = smallest_unchecked
			curr_primes.append(p)
			
		return curr_primes
	
	# ^n Number
	def powerNumberCheck(self, N, n, prime_factor_candidates=[]):
		"""
		1. get the prime factor decomposition
		2. for each prime factor p_i, check if the power alpha_i is divisible by n
		"""
		prime_factor_decomposition = self.primeFactorDecompose(N, prime_factor_candidates)

		for p, alpha in prime_factor_decomposition:
			if not alpha % n == 0:
				return 0

		return 1  

	# irrationals (e.g. sqrt(), e) expansion
	
	######
	#   define some generators here, for: periodic, e, 
	######

	def fractionToMinimumFraction(self, n, m_1, m_2):
		"""
		return the minimum fraction format for n + m_1/m_2 (numerator/denominator)
		"""

		num = n * m_2 + m_1
		den = m_2

		num_facs = dict([(p, n) for p, n, _ in list(self.primeFactorDecompose(num))])  # generator -> list
		den_facs = dict([(p, n) for p, n, _ in list(self.primeFactorDecompose(den))])

		if len(num_facs) > len(den_facs):
			for p in den_facs.keys():
				if p in num_facs.keys():
					num_facs[p] -= min(num_facs[p], den_facs[p])
					den_facs[p] -= min(num_facs[p], den_facs[p])
		else:
			for p in num_facs.keys():
				if p in den_facs.keys():
					num_facs[p] -= min(num_facs[p], den_facs[p])
					den_facs[p] -= min(num_facs[p], den_facs[p])

		num = 1
		for p, n in num_facs.items():
			num *= p**n
		den = 1
		for p, n in den_facs.items():
			den *= p**n

		return num, den


	def __floatToFraction(self, f):
		"""
		(...pending, might be useless)
		Given a float, output the minimal fraction
		"""
		# get the format to xxxxx/10^n
		# numerator:
		num = ''.join(str(f).split('.'))  # notice the leading 0, if exist, is kept, '0.123'->'0123'
		L = len(num)
		num = int(num)
		# denominator:
		denom = 10**(L-1)
		# pending... cancel all the 2 and 5 in num
		pass


	def infiniteContinuedFraction(self, seq):
		"""
		a generator, 
		# https://en.wikipedia.org/wiki/Continued_fraction#:~:text=An%20infinite%20continued%20fraction%20representation,convergents%20of%20the%20continued%20fraction.
		
		"""

		h = 1
		h_pre = 0
		k = 0
		k_pre = 1

		while 1:
			a = seq.__next__()
			h_old = h
			h = a * h + h_pre
			h_pre = h_old
			k_old = k
			k = a * k + k_pre
			k_pre = k_old

			num = h
			den = k

			yield num, den

		return 0 # never reach here

	def infiniteContinuedFraction_m(self, seq, m):
		"""
		(by def)
		up to the m-th element in seq
		e.g. for e
		seq = generator which output [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14, 
		1, 1, 16, 1, 1, 18, 1, 1, 20, 1, 1, 22, 1, 1, 24, 1, 1, 26, 1, 1, 28, 1, 1, 
		30, 1, 1, 32, 1, 1, 34, 1, 1, 36, 1, 1, 38, 1, 1, 40, 1, 1, 42, 1, 1, 44, 
		1, 1, 46, 1, 1, 48, 1, 1, ...]
		"""

		dens = [seq.__next__() for i in range(m)]
		dens = dens[::-1]

		den_pre = dens[0]
		num_pre = 1
		for den in dens[1:]:
			den_pre, num_pre = den_pre * den + num_pre, den_pre
			# den_pre, num_pre = self.fractionToMinimumFraction(den, num_pre, den_pre)
			# print(den_pre, num_pre)
		# num, den = self.fractionToMinimumFraction(0, den_pre, num_pre)
		den1, num1 = den_pre, num_pre

		# den_pre = 1
		# num_pre = dens[0]
		# for den in dens[1:]:
		# 	den_pre, num_pre = den_pre * den + num_pre, den_pre
		# 	# den_pre, num_pre = self.fractionToMinimumFraction(den, num_pre, den_pre)
		# 	# print(den_pre, num_pre)
		# # num, den = self.fractionToMinimumFraction(0, den_pre, num_pre)
		# den2, num2 = den_pre, num_pre

		# assert(num1/den1 > num2/den2)  # assertion wrong

		return num1, den1 #num2, den2
		# num2/den2 < N < num1/den1 

	def sqrtExpansion(self, N):
		"""
		Expand sqrt(m) to its infinite convergent expansion
		See notability "maths-topics-irrationals"
		return int_part, [cycle]
		"""
		# generate a0, a1, a2, ... in the infinite continued fraction

		if N == 0:
			return 0, []
		if N < 0:
			print("invalid sqrt")
			return 
		a = 1
		while a * a < N:
			a += 1
		if a * a == N:  # square number
			# print(a, [])
			return a, []
		a -= 1  # larges a0 --> a0^2 < N
		
		a0 = a
		b = 1
		c = 1
		d = a

		tocheck = 0
		expansion_part = []
		earlier_res = set()
		earlier_res.add((a, c, d))
		while 1:
			b = c
			c = N - d**2
			assert(c % b == 0) #
			c = c//b
			b = 1
			d_new = a0
			while (d + d_new) % c != 0:
				d_new -= 1 
			
			assert(d_new > 0) # 

			a = (d + d_new)//c 
			d = d_new
			# print(a)

			if (a, c, d) in earlier_res:  # cycle detected
				# print(a0, expansion_part)
				return a0, expansion_part
			expansion_part.append(a)
			earlier_res.add((a, c, d))

		return -1  # should never reach here


	def eExpansion(self, m):
		"""
		Expand e up to the m-th decimal, use the infinite continued fraction

		e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14, 
		1, 1, 16, 1, 1, 18, 1, 1, 20, 1, 1, 22, 1, 1, 24, 1, 1, 26, 1, 1, 28, 1, 1, 
		30, 1, 1, 32, 1, 1, 34, 1, 1, 36, 1, 1, 38, 1, 1, 40, 1, 1, 42, 1, 1, 44, 
		1, 1, 46, 1, 1, 48, 1, 1, 50, 1, 1, 52, 1, 1, 54, 1, 1, 56, 1, 1, 58, 1, 1, 
		60, 1, 1, 62, 1, 1, 64, 1, 1, 66...]
		* 2 '1's between each 2(k-1) and 2(k) except for the first '1'
		"""

		def e_infinite_fraction_gen():
			yield 2
			yield 1
			cnt = 1
			while 1:
				yield cnt * 2
				yield 1
				yield 1
				cnt += 1
			return  # never reach here
		
		num, print(Cores().infiniteContinuedFraction_m(e_infinite_fraction_gen(),m))

	def squareNumberGen(self, N_1, N_2):
		"""
		Generate all square numbers within N_1 and N_2
		"""

		res = []
		floor_n = math.ceil(math.sqrt(N_1))
		n = floor_n
		while n*n < N_2:
			res.append(n*n)
			n+=1
		return res

	# print(Cores().fractionToMinimumFraction(0, 1, 1))

class Structures:
	def __init__(self):
		pass
	#####sorting

	# order func
	def alphabetical_order(self, s1, s2):
		"""return 1 if s1 <= s2, 0 otherwise 
		if all matched, place the short one before the longer one"""
		for i, j in zip(s1, s2):  # compare to the shortest one
			if i == j:
				continue
			else:
				if ord(i.lower()) < ord(j.lower()):
					return 1
				elif ord(i.lower()) > ord(j.lower()):
					return 0

		# if all matched for the comparable part
		if len(s1) < len(s2):
			return 1 
		else:
			return 0

	# sorting algos
	def insert_sort(self, sort_l, n, order):
		"""
		insert n into a sorted list sort_l based on order func
		"""
		for i, m in enumerate(sort_l):
			if order(n, m):
				sort_l = sort_l[:i] + [n] + sort_l[i:]
				return sort_l

		sort_l = sort_l + [n]
		return sort_l



	##
	def permutations(self, candidates, N=-1):
		"""
		A base func
		Generate all permutations of N of the candidates
		"""

		# 

		def __permute(candidates, curr=[], res=[], N=-1, cnt=0):
			"""
			
			"""
			if (len(candidates) == 0) | (cnt >= N):  # candidates exhausted, or max depth reached
				res.append(curr)
				return  # return from leaves

			for c in candidates:
				candidates_copy = [i for i in candidates]
				candidates_copy.pop(candidates.index(c))  
				__permute(candidates_copy, curr=curr+[c], res=res, N=N, cnt=cnt+1)

			return res  # return from root

		return __permute(candidates, N=N)

	def combinations(self, candidates, N=-1):
		"""
		choose N from candidates
		"""
		def __combine(candidates, N=-1, ind=0, curr=[], res=[], cnt=0):
			if (ind>len(candidates)-1) | (cnt >= N):  # candidates exhausted, or max depth reached
				if cnt == N:
					res.append(curr)
				return  # return from leaves

			for candidates_ind in range(ind, len(candidates)):
				c = candidates[candidates_ind]
				__combine(candidates, N=N, ind=candidates_ind+1, curr=curr+[c], res=res, cnt=cnt+1)  
				# not necessarily run faster than the unfolding iterative one

			return res  # return from root

		return __combine(candidates, N=N)

class GraphTheory:
	def __init__(self):
		pass

	## data structure ##############################
	def get_adjacency_list(self, N:list, E:list, directed:int=1):
		"""
		list of sets (in Adjacency list, the order of nbrs do not matter)
		"""
		A = [set() for n in N]  # including the 0-degree nodes
		A_ind = dict([(n, i) for i, n in enumerate(N)])
		for e in E:
			A[A_ind[e[0]]].add(A_ind[e[1]])
			if not directed:
				A[A_ind[e[1]]].add(A_ind[e[0]])
		return A, A_ind
		
	## traversing ##############################
	def BFS(self, A:list, src:int):
		"""
		# A: adjacency list
		
		test case:
		A = [[1,2,3], [2,3,5], [4]]
		BFS(A, 0)
		"""
		to_visit = [src]  # use one queue only 
		visited = set()
		while to_visit:
			n_i = to_visit[0]
			visited.add(n_i)
			for n_j in A[n_i]:
				if n_j not in visited:
					to_visit.append(n_j)  # add to the end of the queue
					
			to_visit.pop(0) # pop the head of the queue
		return visited

	def DFS(self, A:list, src:int):
		"""
		# A: adjacency list
		
		test case:
		A = [[1,2,3], [2,3,5], [4]]
		DFS(A, 0)
		"""

		N_pre_post = [[-1, -1] for i in range(len(A))]

		def _DFS(A:list, src:int, N_pre_post:list, cnt=0):
			"""
			:param N_pre_post: global; will be changed; no collison happen
			"""
			# arrive
			N_pre_post[src][0] = cnt

			# leave
			cnt += 1
			N_pre_post[src][1] = cnt

			for nbr in A[src]:
				cnt = _DFS(A, nbr, N_pre_post, cnt)

			# leave again
			N_pre_post[src][1] = cnt
			cnt += 1
			return cnt

		_DFS(A, src, N_pre_post, 0)

		return N_pre_post

	## MST ##############################
	def Prim(self, nodes, weighted_edges):
		"""
		expand the current tree by adding in the least weighted edges connecting to the nodes outside
		"""
		# create a adj list based on weighted_edges
		Adj = dict([(n, []) for n in nodes])
		for u,v,w in weighted_edges: # undirected
			Adj[u].append(v)
			Adj[v].append(u)
		weighted_edges = dict([((u, v), w) for u, v, w in weighted_edges] + 
								[((v, u), w) for u, v, w in weighted_edges])


		current_tree_nodes = {nodes[0]}
		MST_edges = [] 
		# outside_nodes = set(nodes[1:])

		while len(current_tree_nodes) < len(nodes):
			min_edge = -1
			min_weight = math.inf
			for n in current_tree_nodes:
				for m in Adj[n]:
					if m not in current_tree_nodes:
						if weighted_edges[(n, m)] < min_weight:
							min_edge = (n, m, weighted_edges[(n, m)])
							min_weight = weighted_edges[(n, m)]
			MST_edges.append(min_edge)
			current_tree_nodes.add(min_edge[1])

		return MST_edges

	def Kruskal(self, nodes, weighted_edges):
		"""
		merging subtrees by adding edges in the order of ascending weight and avoid loop
		:param weighted_edges, [(u, v, w), ...]
		:param nodes, [u1, u2, u3, ...]
		"""
		weighted_edges = sorted(weighted_edges, key = lambda t:t[-1])
		current_subtrees = [{n} for n in nodes]
		MST_edges = []

		while len(current_subtrees) > 1:
			for u, v, w in weighted_edges:
				sub_tree_1 = -1
				for i, sub_tree in enumerate(current_subtrees):
					if u in sub_tree:
						sub_tree_1 = i
						break
				sub_tree_2 = -1
				for i, sub_tree in enumerate(current_subtrees):
					if v in sub_tree:
						sub_tree_2 = i
						break

				if sub_tree_1 != sub_tree_2:
					current_subtrees[sub_tree_1] = current_subtrees[sub_tree_1].union(current_subtrees[sub_tree_2])
					current_subtrees.pop(sub_tree_2)
					MST_edges.append((u, v, w))

		return MST_edges


	## SCC ##############################
	def undirected_get_components(self, A:list):
		"""
		For undirected, get connected components
		A: adjacency list
		"""
		components = []
		unchecked = range(len(N))   #pending, Adj might missed some 0-degree nodes
		while unchecked:
			src = unchecked[0]
			visited = GraphTheory().BFS(A, src)  # set
			components.append(visited)
			for n in visited:
				unchecked.pop(unchecked.index(n))	

		return components

	def get_k_clique(self, A:list, src:int, k:int):
		"""
		For undirected, get the k-clique where the src is in, if exist
		A: adjancency list
		"""

		def _next_clique(N, curr_clique):
			if len(curr_clique) >= k:
				res.append(curr_clique)
				return 
			for n in set(N) - set(curr_clique):
				add_in = 1
				for n_c in curr_clique:
					if n not in A[n_c]:
						add_in = 0
						break
				if add_in == 1:
					new_clique = copy.copy(curr_clique)
					new_clique.add(n)
					_next_clique(N, new_clique)

		res = []
		N = copy.copy(A[src])
		N.add(src)
		curr_clique = set([src])
		_next_clique(N, curr_clique)

		return res

if __name__ == "__main__":
	# the main function here is for unit test
	candidates = [1, 2, 3, 4]
	print(Structures().combinations(candidates, 2))




