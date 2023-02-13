import numpy as np

def p113(k):
	"""
	Get the number of non-bouncy numbers below 10**k
	(k-digits) 

	e.g. increasing: 

	N[i, n], the number of non-bouncy numbers of n digits ending with i

	i = 1, 2, 3, 4, ..., 9

	N[i, n] = sum([N[j, n-1] for j in range(1, i+1)])

	  n-1 n
	1  x  x  x  x 
	2  x
	3  x
	..
	9  x  o
          


	N[1, *] = 1
	N[*, 1] = 1
	"""

	# increasing

	N = np.zeros((10, k+1)) # 0, 1, 2, ..., 100

	N[1, 1:] = 1
	N[1:, 1] = 1
	for i in range(2, 10): # 2, 3, 4..., 9
		for n in range(2, k+1):
			N[i, n] = sum([N[j, n-1] for j in range(1, i+1)]) # i inclusive

	cntIncrease = sum([np.sum(N[:, n]) for n in range(1, k+1)])
	# decreasing

	cntDecrease = sum([(k-n+1) * np.sum(N[:, n]) for n in range(1, k+1)])  # xx00000...000

	# print(cntIncrease, cntDecrease)
	return cntIncrease + cntDecrease - 9*k # xxxxx, monotonous


def p112():
	"""
	Find the least number for which the proportion of bouncy numbers is exactly 99%

	directly numerate/check the non-bouncy numbers from 0 
	O(10**6) 
	"""
	L = 10  # test for 6, 7, 8.. digits
	l = [-1 for i in range(L)] # fill from low to high
	l[0] = 0

	cnt = 0
	N = 0
	while True:
		N += 1
		l[0] += 1
		carry = l[0] // 10
		l[0] %= 10
		if carry:
			j = 1
			while j < L:
				l[j] = max(l[j], 0)
				l[j] += carry
				carry = l[j] // 10
				l[j] %= 10
				if carry == 0:
					break
				j += 1

		if N >= 10:
			# check increasing, [2, 1, -1, -1]
			j = 1
			if l[j] != -1:
				found = 1
				while l[j] != -1:
					if l[j] < l[j-1]:
						found = 0
						break
					j += 1

				if found:
					cnt += 1

			# check decreasing
			j = 1
			if l[j] != -1:
				found = 1
				while l[j] != -1:
					if l[j] > l[j-1]:
						found = 0
						break
					j += 1

				if found:
					cnt += 1

			if len(set(l)) == 2: # [-1, x]:
				cnt -= 1 # both increasing/non-increasing
		else:
			cnt += 1

		# if N > 538: break;
		# if 1 > (N-cnt) / N >= 0.50 and N != 10:
		# if (N-cnt) / N == 0.90 and N != 10:
		# 	break

		if (N-cnt) / N == 0.99 and N != 10:
			break
		print(l, N, cnt, (N-cnt) / N)
		
	return l





if __name__ == "__main__":

	# print(p113(1))

	# print(p113(6))

	# print(p113(10))

	# print(p113(100))

	print(p112())



