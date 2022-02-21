from fundamentals.cores import Cores, Structures, GraphTheory, Array
import time
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import copy
from itertools import cycle

def p2():
	"""
	https://projecteuler.net/problem=2
		
	Even Fibonacci numbers
	: result sum_i F(i), F(i) < 4 * 10^6
	
	(code the iterative fib, or explicitly use the formula)
	"""

	def fib_sum(MAX_fib):
		def fib_next(pre_fib, pre_pre_fib):
			return pre_pre_fib + pre_fib

		sum_res = 0
		fib_curr_0 = 0
		fib_curr_1 = 1

		sum_res += fib_curr_0
		while fib_curr_1 <= MAX_fib:
			if fib_curr_1 % 2 == 0:
				sum_res += fib_curr_1
			
			fib_curr_1_ = fib_next(fib_curr_1, fib_curr_0) # new
			fib_curr_0 = fib_curr_1
			fib_curr_1 = fib_curr_1_  
		
		return sum_res


	return fib_sum(4*(10**6))

def p3():
	factors = Cores().primeFactorDecompose(600851475143)
	while factors:
		print(factors.next())

def p4():
	"""
	Largest palindrome e.g. "10001" made from the product of two 3 digit numbers 
	"""
	largest_palindrome = 101
	for i in range(100, 1000):
		for j in range(100, 1000):
			n = i * j
			n_l = str(n)
			p1 = 0
			p2 = len(n_l)-1
			is_pan = 1
			while p1 <= p2:
				if n_l[p1] != n_l[p2]:
					is_pan = 0
					break
				p1 += 1
				p2 -= 1
			if is_pan:
				if largest_palindrome < n:
					largest_palindrome = n
	return largest_palindrome

def p6():
	"""
	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
	"""
	s1 = sum([i**2 for i in range(1, 101)])
	s2 = sum([i for i in range(1, 101)]) ** 2

	return s2 - s1

def p7():
	N = 10001
	i = 0
	primes = Cores().primeGenerator()
	while i < 10001:
		p = primes.next()
		i += 1
	return p

def p8():
	"""
	Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
	"""
	l = ''.join("""73167176531330624919225119674426574742355349194934
				96983520312774506326239578318016984801869478851843
				85861560789112949495459501737958331952853208805511
				12540698747158523863050715693290963295227443043557
				66896648950445244523161731856403098711121722383113
				62229893423380308135336276614282806444486645238749
				30358907296290491560440772390713810515859307960866
				70172427121883998797908792274921901699720888093776
				65727333001053367881220235421809751254540594752243
				52584907711670556013604839586446706324415722155397
				53697817977846174064955149290862569321978468622482
				83972241375657056057490261407972968652414535100474
				82166370484403199890008895243450658541227588666881
				16427171479924442928230863465674813919123162824586
				17866458359124566529476545682848912883142607690042
				24219022671055626321111109370544217506941658960408
				07198403850962455444362981230987879927244284909188
				84580156166097919133875499200524063689912560717606
				05886116467109405077541002256983155200055935729725
				71636269561882670428252483600823257530420752963450""".split('\n'))
	print(l)

	def product_n(l):
		res = 1
		for i in l:
			res *= i
		return res

	max_product = -1
	adjacent_digits = ''
	for i in range(0, 1001-13):
		ints = [int(j) for j in l[i:i+13]]
		product = product_n(ints)
		if product > max_product:
			max_product = product
			adjacent_digits = l[i:i+13]

	return max_product

def p9():
	"""
	There exists exactly one Pythagorean triplet (a^2 + b^2  = c^2) for which a + b + c = 1000.
	Find the product abc.
	"""

	for a in range(0, 1000):
		for b in range(0, 1000-a):
			c = 1000-a-b
			if (a**2 + b**2 == c**2):
				print(a, b, c)

	return

def p10():
	"""Find the sum of all the primes below two million."""

	return sum(Cores().primesBelowN(2 * (10 ** 6)))

def p11():
	"""
	largest product of 4 adjacent digits in the 20 * 20 grid

	"""

	g = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
			49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
			81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
			52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
			22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
			24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
			32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
			67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
			24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
			21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
			78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
			16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
			86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
			19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
			04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
			88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
			04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
			20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
			20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
			01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

	grid = [[int(i) for i in l.split(' ')] for l in g.split('\n')]

	grid = np.array(grid)

	def product_n(l):
		res = 1
		for i in l:
			res *= i
		return res

	max_product = -1
	# check horizonal

	for i in range(20): # row
		for j in range(0, 20-4):
			product = product_n(grid[i, j:j+4]) 
			if product > max_product:
				max_product = product
	# check vertical
	for j in range(20): # column
		for i in range(0, 20-4):
			product = product_n(grid[i:i+4, j]) 
			if product > max_product:
				max_product = product
	# check diagonal
	for i in range(20-3): # row
		for j in range(20-3): # column
			product = product_n(grid[[i, i+1, i+2, i+3], [j, j+1, j+2, j+3]])
			if product > max_product:
				max_product = product
	# check off-diagonal
	for i in range(20-3): # row
		for j in range(20-1, 3-1, -1): # column
			product = product_n(grid[[i, i+1, i+2, i+3], [j, j-1, j-2, j-3]])
			if product > max_product:
				max_product = product

	print(max_product)

def p12():

	n = 1 # tri_num = n(n+1)/2
	while 1:
		if n % 2 == 0:
			no_factors_1 = 0  # n // 2
			for i in range(1, math.floor(math.sqrt(n//2))):
				if (n//2) % i == 0:
					no_factors_1 += 2 # a pair
			no_factors_2 = 0 # n+1
			for i in range(1, math.floor(math.sqrt(n+1))):
				if (n+1) % i == 0:
					no_factors_2 += 2

			if no_factors_1 * no_factors_2 - 1 > 500:
				return n*(n+1)//2 
		
		else:
			no_factors_1 = 0  # n
			for i in range(1, math.floor(math.sqrt(n))):
				if n % i == 0:
					no_factors_1 += 2
			no_factors_2 = 0 # n+1 // 2
			for i in range(1, math.floor(math.sqrt((n+1)//2))):
				if ((n+1)//2) % i == 0:
					no_factors_2 += 2

			if no_factors_1 * no_factors_2 - 1 > 500:
				return n*(n+1)//2 

		n += 1


	return 0 # never reach here

def p13():
	"""the first 10 digits of the sum of the 100 50-digit numbers"""

	number_D = np.array([[int(d) for d in n] for n in """""".split('\n')])  # np.array 

	number_D = number_D[:, ::-1]  # revert row, set the lowest to the top 
	
	res = np.zeros(number_D.shape[1])  # init

	def fix_overflow(res, loc):
		while res[loc] > 9:  # overflow detected at loc
			res[loc] -= 10
			try:
				res[loc+1] += 1
			except IndexError:  # overflow digit spaces
				res = Array().safeSetValue(res, loc+1, 1)
			loc += 1
		return res

	for col in range(number_D.shape[1]):
		col_sum = np.sum(number_D[:, col])
		d_add_loc = col # adding ds in col_sum "xxxx" from the curr col
		while col_sum > 0:
			curr_d = col_sum % 10

			try:
				res[d_add_loc] += curr_d
			except IndexError:
				res = Array().safeSetValue(res, d_add_loc, curr_d)
			# check & fix the overflow result from the +
			res = fix_overflow(res, d_add_loc)
			
			d_add_loc += 1
			col_sum -= curr_d
			col_sum //= 10

	return res[-10:][::-1]

def p14():
	"""
	Longest Collatz sequence (hypo: all chain finishes at 1)
	
	Which starting number < 10**7, produce the longest chain?
	
	even n -> n/2 reduce
	odd n -> 3n + 1 even; (expand)

	Once the chain starts the terms are allowed to go above one million.
	"""
	# simple brute-force, don't need optimize for now
	max_l = -1
	max_l_n = -1
	for i in range(2, 10**6+1):
		L = 0
		n = i
		while n != 1:
			if n % 2 == 0:
				n = n // 2
			else:
				n = 3*n+1
			L += 1
		if L > max_l:
			max_l_n = i
			max_l = L

		if i % 10000 == 0:
			print(i)

	return max_l_n

def p15():
	"""
	Lattice paths:
	right, down

	how many such paths in a 20*20 grid?
	"""

	# arranging 20 rights in 40 places

	return math.factorial(40)/(math.factorial(20))**2

def p16():
	"""
	the sum of the digits of the number 2^1000

	* for different languages the data type need to be chosen first
	"""

	return sum([int(i) for i in str(2**1000)[:]])

def p17():
	"""
	If the numbers 1 to 5 are written out in words: 
	one, two, three, four, five, 
	then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

	If all the numbers from 1 to 1000 (one thousand) 
	inclusive were written out in words, 
	how many letters would be used?
	
	e.g.
	342 (three hundred and forty-two) 
	contains 23 letters 

	"""
	dic = dict({1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
				6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
				11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 
				15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 
				19:"nineteen", 20:"twenty", 
				30:"thirty", 40:"forty", 
				50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",
				100:"hundred", 1000:"thousand"})


	L = 0
	for N in range(1, 1001):
		s = ''
		xx = N % 100
		if xx > 0:
			if xx <= 20:
				s += dic[xx]
			else:
				s += dic[xx-xx%10]  # '-ty'
				if xx%10 != 0:
					s += dic[xx%10]  # x

		if (N!=1000) and (N // 100 != 0): # xxx
			s += dic[100]  # "hundred"
			if (N//100)%10 != 0:
				s += dic[(N//100)%10]  # xx hundred
			
			if xx != 0:
				s += 'and' # and

		if N == 1000:
			s += "one" + dic[1000]

		L += len(s)

	return L

def p18():
	"""
	"""
	triangle = \
	[[int(n) for n in l.split(' ')] for l in 
	"""""".split('\n')]

	# i-th at n-th row, could only move to i and i+1 at n+1-th row
	# use DP
	# set up the table, and update in the order top-bottom

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

def p19():
	"""
	How many Sundays fell on the first of the month 
	during the twentieth century (1 Jan 1901 to 31 Dec 2000)"""

	years = range(1900, 2001)
	months = cycle(range(1, 13))
	days = 0
	month_1st_Sun = 0 

	for year in years:
		for i in range(12):
			# the current month
			if year > 1900 and (days + 1) % 7 == 0:
				month_1st_Sun += 1
			
			month = months.__next__()
			if month in [1, 3, 5, 7, 8, 10, 12]:
				days += 31
			elif month in [4, 6, 9, 11]:
				days += 30
			else:
				if year % 4 == 0:
					if year % 100 == 0:
						if year % 400 == 0:
							days += 29
					else:
						days += 29
				else:
					days += 28

	return month_1st_Sun

def p20():
	"""
	"""

	return sum([int(i) for i in str(math.factorial(100))])

def p21():
	"""
	Evaluate the sum of all the amicable numbers under 10000
	"""

	amicable_numbers = set()

	def div_sum(n):
		n_div = [i for i in range(1, n) if n % i == 0]
		n_div_sum = sum(n_div)
		return n_div_sum

	for n in range(2, 10001):
		n_div_sum = div_sum(n)
		n_ = div_sum(n_div_sum)
		# print(n, n_div_sum, n_)
		if n == n_:
			if n < n_div_sum:
				amicable_numbers.add((n, n_div_sum))
			elif n > n_div_sum:
				amicable_numbers.add((n_div_sum, n))
			else:
				pass

	return sum([sum(t) for t in list(amicable_numbers)])

def p22():
	"""
	sorting - insert sorting

	alphabetical ordering
	"""

	name_list = [str(n.strip('''"''')) for n in open("name.txt").readline().strip('\n').split(',')]   # read-in 
	# print(name_list)
	sort_list = []

	for name in name_list:
		if len(sort_list) == 0:
			sort_list.append(name)
		else:
			sort_list = Structures().insert_sort(sort_list, name, Structures().alphabetical_order)

	name_score = sum([sum([ord(s)-96 for s in name.lower()]) * (i+1) 
						for i, name in enumerate(sort_list)])

	return name_score

def p23():
	"""
	Find the sum of all the positive integers which 
	cannot be written as the sum of two abundant numbers.
	"""

	# get all the abundant numbers below 28123

	abundant_n = []
	for n in range(1, 28124):
		n_div_sum = sum(Cores().divisors(n)) - n  # proper
		if n_div_sum > n:
			abundant_n.append(n)

	sum_res = []

	for i, n1 in enumerate(abundant_n):
		for j, n2 in enumerate(abundant_n[i:]):
			if n1+n2 < 28124:
				sum_res.append(n1+n2)

	return sum(list(set(range(1, 28124)) - set(sum_res)))

def p24():
	"""
	the millionth lexicographic permutation of the digits 
	0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
	"""

	res = []
	def lexicographic_permutation(curr, candid_remain):
		if len(candid_remain) == 0:
			res.append(curr)
			return

		for c in sorted(candid_remain):
			tmp = copy.copy(candid_remain)
			tmp.pop(tmp.index(c))
			lexicographic_permutation(curr+[c], tmp)
	
	lexicographic_permutation([], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	return ''.join([str(i) for i in res[10**6-1]])

def p25():
	"""
	the index of the first term 
	in the Fibonacci sequence to contain 1000 digits
	"""
	f_1 = 1
	f_2 = 1
	ind = 2
	while len(str(f_2)) < 1000:
		f_2_old = f_2
		f_2 = f_1 + f_2
		f_1 = f_2_old
		ind += 1

	return ind

def p26():
	"""
	Find the value of d < 1000 for which 
	1/d contains the longest recurring cycle 
	in its decimal fraction part.
	"""

	def decimal_fraction(d):
		""""""
		visited_num = set()
		num = 10
		decimal_part = []
		while num not in visited_num:
			visited_num.add(num)
			decimal_part.append(num // d)
			num = (num % d) * 10

		return decimal_part

	max_L = -1
	max_L_d = -1
	for d in range(2, 1000):
		L = len(decimal_fraction(d))
		if L > max_L:
			max_L = L
			max_L_d = d

	return max_L_d

def p27():
	"""
	For F(n) = n^2 + a*n + b, |a|<1000, |b|<=1000, 
	get a * b which F(n) produces the longest consecutive primes from n=0 to L(a, b)

	Consider:
	1, F(b) non-prime, F(-b) non-prime, F(b-a) non-prime
	   thus if a<0, then the upper bound L(a, b) = b-1 < b, else the upper bound is b-a-1 < b-1 < b, 
	   there for set a<0
	2. for if F(n) prime then F(n+1) prime, F(n+1)-F(n) = (2*n + 1) + a, then a must be odd
	
	Then iterate through these candidates:
	a<0, |a| = {1, 3, 5, 7, ..., 999}
	|b| = {2, 3, 5, 7, 11, ...}
	"""

	b_candidates = Cores().primesBelowN(1000)
	b_candidates += [-b for b in b_candidates]
	a_candidates = [-(2*i+1) for i in range(499)] + [(2*i+1) for i in range(499)]
	all_possible_primes = set(Cores().primesBelowN(1000**2 - 1*1000 + 1000))

	def F(n, a, b):
		return n**2 + a*n + b

	curr_longest = -1
	curr_a_b = (0, 0)

	cnt = 0
	for a in a_candidates:
		for b in b_candidates:
			i = 0
			is_prime = 1
			while is_prime & (i < abs(b)):
				if F(i, a, b) not in all_possible_primes:
					is_prime = 0
				i += 1

			if curr_longest < i:
				curr_longest = i
				curr_a_b = (a, b)
				# print(curr_a_b, curr_longest)

			cnt += 1
			if cnt % 100 == 0:
				print(cnt, '/', len(b_candidates)*len(a_candidates))
				print(curr_a_b, curr_longest)

	return curr_a_b[0] * curr_a_b[1]

def p28():
	"""
	the sum of the numbers on the diagonals in a 1001 by 1001 spiral
	"""

	res = 1
	pre = 1
	for level in range(1, 501): # to the 1001
		res += 4*pre + 2*level*(1+2+3+4)
		pre += 2*level*4

	return res

def p29():
	"""
	How many distinct terms are in the sequence 
	generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
	"""

	return len(set([a**b for a in range(2, 101) 
						for b in range(2, 101)]))

def p30():
	"""
	Find the sum of *all* the numbers that can be 
	written as the sum of fifth powers of their digits.

	(browse within <6-digits; see note)
	"""

	res = []
	for n in range(2, 1000000):
		digits = [int(i) for i in list(str(n))]
		if n == sum([d**5 for d in digits]): 
			res.append(n) 

	return sum(res)


def p35():
	"""
	The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

	There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

	How many circular primes are there below one million?
	"""

	N = 1 * (10 ** 6)
	primes = set(Cores().primesBelowN(N))
	print("generation finish")

	is_circular = 1
	cnt = 0
	for p in primes:
		# see if need optimizing (no
		p_l = str(p)
		# print(p)
		for i in range(1, len(p_l)):
			p_rot = int(str(p_l[i:]) + str(p_l[:i]))
			# print(p_rot)
			if p_rot not in primes:
				is_circular = 0
				break
		if is_circular == 1:
			cnt += 1
		is_circular = 1
	
	print("cnt", cnt)

	return 

def p37():
	"""
	Find the sum of *the only eleven primes* that are both truncatable from left to right and right to left.
	"""

	# use recursive

	def truncablePrimeCheck(p, candidate_primes):
		"""
		return: is_prime, is_truncable
		"""

		p_l = str(p)

		is_prime = 1
		is_truncable = 1

		# p>>>
		if len(p_l)-1 == 2:
			i_l = [2]
		else:
			i_l = range(2, len(p_l)-1) 
		for i in i_l:
			if sum([int(j) for j in p_l[:i]]) % 3 == 0:
				is_truncable = 0
				break
			# elif not Cores().primeCheck(int(p_l[:i])):
			elif int(p_l[:i]) not in candidate_primes:
				is_truncable = 0
				break

		# p<<<
		for i in range(1, len(p_l)-1):
			if sum([int(j) for j in p_l[i:]]) % 3 == 0:
				is_truncable = 0
				break
			# elif not Cores().primeCheck(int(p_l[i:])):
			elif int(p_l[i:]) not in candidate_primes:
				is_truncable = 0
				break

		# finally check for p as prime
		if len(p_l) > 1:
			if sum([int(i) for i in str(p)]) % 3 == 0:
				is_prime = 0  # shortcut
			# elif not Cores().primeCheck(p):  
			elif p not in candidate_primes:
				is_prime = 0

		return is_prime, is_truncable

	def select_next_digit(N):
		"""
		not so much restrictions for the middle numbers
		"""
		candidates = [1, 3, 7, 9]

		return candidates # some candidates meet all the restrictions above


	def get_next_candidate(n_pre, n_digit, candidate_primes):

		if n_digit == 0:
			next_digits = [2, 3, 5, 7]
		else:
			next_digits = select_next_digit(n_pre)

		for d in next_digits:  # left-most
			# d>>>
			n = n_pre * 10 + d
			# print("checking", n)
			is_prime, is_truncable = truncablePrimeCheck(n, candidate_primes)
			if is_prime and is_truncable:
				# cnt += 1  # global
				if d in [1, 9]:
					get_next_candidate(n, n_digit + 1, candidate_primes)
				else:
					print(n) #cnt)
					get_next_candidate(n, n_digit + 1, candidate_primes)
			else:
				if is_prime:
					get_next_candidate(n, n_digit + 1, candidate_primes) # keep branching down
				else:
					continue # stop branching, go for the next d in for-loop

		return 
		# if the for-loop exhausted, go back to the parent node, continue the pre-parent for-loop, if any

	candidate_primes = set(Cores().primesBelowN(10**6))   # proof by hand..

	get_next_candidate(0, 0, candidate_primes)
	# sum([]) = 388317

	# print(truncablePrimeCheck(397, candidate_primes))
	# print(select_next_digit(73373))
	return 

def p41():
	"""
	Largest n-digit pan-digital (\pi(1, 2, 3, ..., n)) prime that exists

	rules:
	12  sum=3 x
	123 sum=6 x
	1234 sum=10
	12345 sum=15 x
	123456 sum=21 x
	1234567 sum=28 
	12345678 sum=36 x
	123456789 (10**8) sum=45 x  

	"1234567" 10**7
	--> 2, 4, 5, 6, 8 not on the lowest (1, 3, 7, 9 on the lowest), 
	"""

	# see if optimization needed
	
	def generate_pandigital(n, prime_candidates, rest_digits=[], res=[]):
		"""all the permutations of 1, 2, ..., 7"""

		if (n == 0) & (len(rest_digits)==0):
			for i in [1, 3, 7]:
				n = i
				if i == 1:
					generate_pandigital(n, prime_candidates, rest_digits=[3, 7] + [2, 4, 5, 6], res=res)
				elif i == 3:
					generate_pandigital(n, prime_candidates, rest_digits=[1, 7] + [2, 4, 5, 6], res=res)
				else:
					generate_pandigital(n, prime_candidates, rest_digits=[1, 3] + [2, 4, 5, 6], res=res)
		elif (n != 0) & (len(rest_digits)!=0):
			for i in rest_digits:
				rest_digits_copy = [j for j in rest_digits]
				n_ = n + i*(10**(7 - len(rest_digits)))
				rest_digits_copy.pop(rest_digits.index(i))
				generate_pandigital(n_, prime_candidates, rest_digits=rest_digits_copy, res=res)
		elif (n != 0) & (len(rest_digits)==0):
			if n in prime_candidates:
				res.append(n)

		return res

	prime_candidates = set(Cores().primesBelowN(7654321))
	print(max(generate_pandigital(0, prime_candidates)))

def p47():
	"""
	Find the first four consecutive integers to have four distinct prime factors each
	"""

	cnt = 0
	N = 2
	restart = 0
	res = []
	prime_factor_candidates = Cores().primesBelowN(10**6)
	while cnt < 4:
		factors = Cores().primeFactorDecompose(N, prime_factor_candidates)  # a generator
		try:
			for i in range(4):
				factors.__next__()
		except StopIteration:
			restart = 1 # less than 4 prime factors

		try: 
			factors.__next__()
			restart = 1  # more than 4 prime factors
		except StopIteration:
			pass
		
		if restart == 1:
			cnt = 0
			restart = 0
			res = []
		else:
			cnt += 1
			res.append(N)

		N += 1
		print(res)

	return res

def p49():
	"""
	3 4-digit primes as a arithmetic sequence N1=n, N2=n+a, N3=n+2a, 
	each N_i is a prime, N_i is a permutation of N_j
	only one other than 1487, 4817, 8147 a=3330
	"""

	prime_candidates = set(Cores().primesBelowN(9999))
	digit4s = Structures().permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 
										 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 
										 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 
										 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], N=4)  # all 4-digits, 10**4
	digit4s = ["%s%s%s%s"%(i, j, k, l) for i, j, k, l in digit4s] # strs
	prime_candidates = [str(i) if i//1000>0 else "0"+str(i) for i in prime_candidates]  # strs
	prime_digit4s = set(digit4s).intersection(prime_candidates)  # strs

	for digit4 in prime_digit4s: # str
		# get all the permutations of digit4 in prime_digit4
		permutes = [1000*i+100*j+10*k+l for i, j, k, l in Structures().permutations([int(i) for i in str(digit4)], N=4)]  # ints
		prime_permutes = list(set([int(i) for i in prime_digit4s]).intersection(set(permutes))) # ints

		triplets = Structures().permutations(prime_permutes, N=3) # ints
		# print(triplets)
		for triplet in triplets:
			if len(triplet) > 2:
				triplet = sorted(triplet)
				if triplet[0]+triplet[2] == 2 * triplet[1]:
					if triplet[0]//1000 > 0:
						print(triplet)  # should output 2 triplets

		for prime_permute in prime_permutes: 
			prime_permutes.pop(prime_permutes.index(prime_permute))

def p50():
	"""Which prime, below one-million, can be written as the sum of the most consecutive primes?"""

	prime_candidates = Cores().primesBelowN(10**6)
	prime_candidates_set = set(prime_candidates)

	max_len = 0
	max_len_prime = 0
	for i, p in enumerate(prime_candidates):  # head
		s = 0
		cnt = 0
		for _, p_t in enumerate(prime_candidates[i+1:]):
			s += p_t
			cnt += 1
			if s in prime_candidates_set:  # the sum is prime and < 10**6
				if max_len < cnt:
					max_len = cnt
					max_len_prime = s
			if s > 10**6:
				break
		if i % 1000 == 0:
			print(i, max_len, max_len_prime)

	return max_len_prime  # actually, the one receives at the lower head is the optimal (as when head increases, the len decreases)

def p51():
	"""
	(combinatorics)

	Find the *smallest* prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, 
	is part of an eight prime value family.

	(assume that these primes < 10**6) get all the primes < 10**6 and have same digits

	(generating graphs, find connected components, etc. is not efficient for this problem, basically because generating edges requires
	compare each pair of nodes, and the connection rules are not universal.)
	"""

	prime_nodes = Cores().primesBelowN(10**6)
	for L in range(5, 7):
		print("L", L)
		prime_candidates = set([p for p in prime_nodes if p//(10**(L-1)) > 0])  # set() is a LOT faster than list when 'in'
		for fix_digits in range(2, L):  # 3 to L-1 fixed spots
			print("fix", fix_digits)
			fixed_spots_inds = Structures().combinations(list(range(L-1)), N=fix_digits)
			for fixed_spots_ind in fixed_spots_inds:  # fix spots pos
				# print(fixed_spots_ind)
				# collect all possible prime candidate templates
				non_fixed_spots_ind = set(range(L)) - set(fixed_spots_ind) # L-3 to 1 non-fixed

				templates = []
				for prime in prime_candidates:
					templates.append(''.join([str(prime)[ind] for ind in non_fixed_spots_ind]))
				templates = set(templates)
				# print(len(templates))

				prime_candidates_templates = []
				for cand in templates:  # str
					tmp = [-1] * L
					for ind, digit in zip(non_fixed_spots_ind, list(cand)):  # other spots
						tmp[ind] = digit
					prime_candidates_templates.append(tmp)  
				# print(len(prime_candidates_templates))

				for node_candidate_template in prime_candidates_templates:
					cnt = 0  # count the # in the prime family
					for i in range(0, 10):
						for j in fixed_spots_ind:
							node_candidate_template[j] = i
						number = ''.join([str(k) for k in node_candidate_template])
						if int(number) in prime_candidates:  # 
							if number[0] != 0:  # lead zeros not valid
								cnt += 1

					if cnt >= 8:
						return node_candidate_template, fixed_spots_ind



	return -1 

def p58():
	"""
	(note: ppl think this one is easy, but it seems bulky to me...)
	(but it is much easier to use recursive than generating a formula!)

	A square spiral (de-clockwise) with side length 7, 8 out of 13 numbers on the diagonals are prime:
	37 36 35 34 33 32 31
	38 17 16 15 14 13 30
	39 18  5  4  3 12 29
	40 19  6  1  2 11 28
	41 20  7  8  9 10 27
	42 21 22 23 24 25 26
	43 44 45 46 47 48 49

	find the smallest side length L, where the ratio of the primes on diagonal: #(p)/(2L-1) < 10%
	
	(do not use recursive, will get "maximum recursion depth exceeded" at depth ~3900)
	"""

	# generate the diagonal numbers, 

	# (1, 3, 13, 31)
	prime_factor_candidates = Cores().primesBelowN(10**6)
	res = [1]
	res_prime = [0] # bools
	pre = 1
	L = 1
	ratio = 1
	while ratio > 0.1:
		L = L+2
		# de-clock wise from the upper-right corner
		for i in range(1, 5):
			new_no = pre+(L-1)*i
			if Cores().primeCheck(new_no, prime_factor_candidates):  #
				res_prime.append(1)
			else:
				res_prime.append(0)
			res.append(new_no)

		if new_no > 10**12:
			print("larger")
			sys.exit()

		pre = new_no
		ratio = sum(res_prime)/len(res_prime)

	# print(res)
	return L

def p60():
	"""
	(combinatoric) (graph theory)
	Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
	"""

	t = time.time()
	k = 5
	prime_factor_candidates = Cores().primesBelowN(10000) # could check to 10**10
	print("candidates generation finished", time.time() - t) 

	t = time.time()
	edges = []
	N = set()

	# prime_pairs = Structures().combinations(prime_factor_candidates, N=2) # will be very slow with the recursive 

	prime_pairs = []
	for i in range(len(prime_factor_candidates)-1):
		for j in range(i+1, len(prime_factor_candidates)):
			prime_pairs.append([prime_factor_candidates[i], prime_factor_candidates[j]])

	for pair in prime_pairs: 
		# print(pair)
		if Cores().primeCheck(int(''.join([str(pair[0]), str(pair[1])])), prime_factor_candidates) and \
		   Cores().primeCheck(int(''.join([str(pair[1]), str(pair[0])])), prime_factor_candidates):
			edges.append([pair[0], pair[1]])  # undirected
			N.add(pair[0])
			N.add(pair[1])

	N = list(N)

	print("edge generation finished", time.time() - t)  # debug
	print("#edges", len(edges))
	# print(([13, 7] in edges))
	# print(([7, 13] in edges))  # '7013' - 7|013 - 013|7 not valid

	t = time.time()

	A, A_ind = GraphTheory().get_adjacency_list(N, edges, directed=0)
	print("max degree", max([len(l) for l in A]))
	print("non-degree nodes", sum([1 for l in A if len(l) == 0])/len(A))
	# print(edges, len(A), len(edges))

	curr_lowest_sum = 10**10
	curr_clique = []
	for node in sorted(N):    # sequentially delete the non-cliquable nodes to make it more efficient
		k_cliques = GraphTheory().get_k_clique(A, A_ind[node], k=k)  # could be optimized: only consider the nodes having >= k-1 degree in the subgraph
		for clique in k_cliques:
			curr_sum = sum([N[i] for i in clique])
			if curr_lowest_sum > curr_sum:
				curr_lowest_sum = curr_sum
				curr_clique = clique 
				# print([prime_candidates[n] for n in curr_clique])
			# print(cluster)
	print("finding clique", time.time() - t)

	return [N[n] for n in curr_clique]

def p61():
	"""
	Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, 
	is represented by a different number in the set.

	1. Get all these P(k, n) 4-digit numbers
	2. Find all the cyclic-six sets (using recursive to directly do the search)
	"""

	# 1. Get all these P(k, n) 4-digit numbers

	def p_kn(k, n):
		if k == 3:
			return n*(n+1)/2
		elif k == 4:
			return n**2
		elif k == 5:
			return n*(3*n-1)/2
		elif k == 6:
			return n*(2*n-1)
		elif k == 7:
			return n*(5*n-3)/2
		elif k == 8:
			return n*(3*n-2)
		else:
			return -1

	P_kn = []

	for k in range(3, 8+1):
		P_kn.append([])
		for n in range(1000):
			N = p_kn(k, n)
			if 1 <= (N // 1000) <= 9:
				P_kn[-1].append(N)

	# 2. Find all the cyclic-six sets (using recursive to directly do the search)

	res = []
	def cyclic_six(candidates, curr_ind, curr_ns, remain_ks, pre):
		if len(curr_ind) == 6:  # (k_i, n_i)
			# check with the head 
			head_n = candidates[curr_ind[0][0]][curr_ind[0][1]]
			tail_n = candidates[curr_ind[-1][0]][curr_ind[-1][1]]
			if (head_n//100) == (tail_n%100):
				res.append(curr_ind)
			return
		if len(remain_ks) == 0:
			return 

		for k in remain_ks:
			for n, c in enumerate(candidates[k]):
				if (c//100 == pre%100) | (pre == 0):
					remain_ks_new = copy.copy(remain_ks)
					remain_ks_new.pop(remain_ks_new.index(k))
					cyclic_six(candidates, curr_ind+[(k, n)], curr_ns+[n], 
											remain_ks_new, c)

	cyclic_six(P_kn, [], [], [0, 1, 2, 3, 4, 5], 0)
	for ind_l in res:
		print([P_kn[ind[0]][ind[1]] for ind in ind_l])

	return 

def p64():
	"""
	How many continued fractions for N<10000 have an odd period?
	"""
	cnt = 0
	for n in range(10001):
		_, period = Cores().sqrtExpansion(n)
		if len(period) % 2 == 1:
			cnt += 1
	return cnt

def p65():
	"""
	Convergents of e

	Find the sum of digits in the numerator of the 100th 
	convergent of the continued fraction for e.
	test case: first ten terms in ... of e
	2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
	"""
	# e = [2; 1, 2, 1, 1, 4, 1, 1, 6, ...]
	def e_infinite_fraction_gen():

		yield 1
		cnt = 1
		while 1:
			yield cnt * 2
			yield 1
			yield 1
			cnt += 1

		return  # never reach here

	e_gen = e_infinite_fraction_gen()
	num, den = Cores().infiniteContinuedFraction(2, e_gen, 100)

	return num, den

def p66():
	"""
	Find the minimal int solution x in (x, y, D) for D <= 1000

	x^2 - D*y^2 = 1

	Directly use the conclusion from Pell's equation
	"""

	# 1. Get all D' <= 1000 that does not contain a square part, D' != k * q^2 
	# -----well at least we have some of our own input to this problem...-----

	D_set = []
	for D in range(2, 1001):
		D_factors = Cores().primeFactorDecompose(D)
		has_square_comp = 0
		for factor in D_factors:
			if factor[1] > 1:  # has a square component
				has_square_comp = 1
				break
		if has_square_comp == 0:
			D_set.append(D)

	# Pell's equation

	res = dict([(D, 0) for D in D_set])
	max_x_D = -1
	max_x = -1
	for D in D_set:
		# get the sqrt(N) infinite fraction expansion cycle representation
		int_part, cycle_rep = Cores().sqrtExpansion(D)
		def gen(int_part, cycle_rep):
			yield int_part
			cyc = cycle(cycle_rep)
			while 1:
				yield cyc.__next__()

		seq = gen(int_part, cycle_rep)

		x_y_gen = Cores().infiniteContinuedFraction(seq)

		while 1:
			x, y = x_y_gen.__next__()
			if x**2 - D * y**2 == 1:  # the min x for this D found
				if x > max_x:
					max_x = x
					max_x_D = D
				break	

	return max_x_D, max_x

def p77():
	"""
	(divide & conquer)
	(difficult 25%, solved within 1h)
	10 can be written 10 as the sum of primes in 5 different ways:
	7 + 3
	5 + 5
	5 + 3 + 2
	3 + 3 + 2 + 2
	2 + 2 + 2 + 2 + 2

	the first value which can be written as the sum of primes in over five thousand different ways

	#(N) = #(N-m) * #(m)
	#(N) = #(p1)#(p2)...#(pn)

	1. Get the ways of sums for the *primes* to N
		* each combo is a descending order
	2. iterate the natural numbers, get their decomposition of the prime, and return the first number found to have #(N) >= 5000
	"""
	
	def sum_of_primes(n, candidates, curr_sum=0, curr_arr=[], last_d=0):
		if curr_sum == n: 
			res.append(curr_arr)
			return 

		for i, c in enumerate(candidates): 
			if c <= last_d:
				s = curr_sum+c
				next_candidates = copy.copy(candidates)
				if c > n-s:  # could not be used again
					next_candidates = next_candidates[i+1:] # candidates are sorted in ascending order
				else:
					next_candidates = next_candidates[i:]
				sum_of_primes(n, next_candidates, curr_sum=s, curr_arr=curr_arr+[c], last_d=c)	

	# 	1. Get the ways of sums for the *primes* to N: * each combo is a descending order
	prime_factor_candidates = Cores().primesBelowN(100)
	prime_factor_sum_ways = []
	for i, p in enumerate(prime_factor_candidates):
		primes_below_p = prime_factor_candidates[:i+1][::-1]
		print(primes_below_p)
		res = []
		sum_of_primes(p, primes_below_p, curr_sum=0, curr_arr=[], last_d=p)
		prime_factor_sum_ways.append(len(res))
		print(len(res))

	# iterate the natural numbers, get their decomposition of the prime, 
	# and return the first number found to have #(N) >= 5000
	for n in range(100):
		decomposition = Cores().primeFactorDecompose(n, prime_factor_candidates=prime_factor_candidates)
		no_sum_ways = 1
		for combo in decomposition:
			for i in range(combo[1]):
				no_sum_ways *= prime_factor_sum_ways[prime_factor_candidates.index(combo[0])]
		if no_sum_ways >= 5000:
			print(n)
			return 	

def p87():
	"""
	("complexity control")
	difficulty 20% (I think ppl give up earlier), <20min... 

	How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
	"""
	# the largest prime candidate satisfies: 5 * 10^7 = P^2 + 2^3 + 2^4  => P_max
	p_max = int(math.sqrt(5*(10**7) - 8 - 16))+1  # 10**3
	prime_factor_candidates = Cores().primesBelowN(p_max)

	squares = []
	cubes = []
	fourth_powers = []
	for p in prime_factor_candidates:
		if p**2 < 5*(10**7):
			squares.append(p**2)
		if p**3 < 5*(10**7):
			cubes.append(p**3)
		if p**4 < 5*(10**7):
			fourth_powers.append(p**4)

	res = set()
	print(len(squares), len(cubes), len(fourth_powers))

	for square in squares:
		for cube in cubes:
			for fourth_power in fourth_powers:
				s = square + cube + fourth_power
				if s <= 5 * (10**7):
					res.add(s)
	print(len(res))
	return 

def p97():
	"""Find the last 10 digits of 28433*2^7830457+1, the non-Mersenne prime"""
	# only calculate * 2 on the last 10 digits of the returned result from the previous calculation

	n = 28433
	for i in range(7830457):
		n = n * 2
		n = n % (10**11)  # truncate to the last 10 digits

	return n+1


if __name__ == "__main__":
	print(p13())
			 



