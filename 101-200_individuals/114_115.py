import numpy as np

def p114_115(N, L):
	"""
	L = 3

	S[n, k], pad length k block ending at pos n
    

    . .
	- -  -  -   ...   -
           n-k        n
	


	n >= k
	S[n, k] = sum([S[n_pre, k_pre]
				   for n_pre in range(L, n-k)
				   for k_pre in range(L, n-k)	
				   ])

	S[3, 3] = 1
	S[<3, :] = 0

	"""
	S = np.zeros((N+1, N+1))

	S[L, L] = 1

	for n in range(L+1, N+1):
		for k in range(L, n+1):
			S[n, k] = 1 + sum([S[n_pre, k_pre]
						   for n_pre in range(L, n-k)
						   for k_pre in range(L, n-k)	
						   ])

	# print(S)
	return np.sum(S[:, :]) + 1 # all zeros




if __name__ == "__main__":

	# 114
	print(p114_115(7, 3))

	print(p114_115(50, 3))

	print(p114_115(29, 3))

	print(p114_115(30, 3))

	print(p114_115(56, 10))

	print(p114_115(57, 10))

	# 115

	print(p114_115(167, 50)) # 

	# L = 50
	# # 115: For L = 50, find the least value of N for 
	# # 	   which the fill-count function first exceeds one million.
	left = 150
	right = 200
	while left < right:
		mid = (left + right) // 2
		res = p114_115(mid, 50)
		if res > 10**6:
			right = mid # keep this boundary
		elif res < 10**6:
			left = mid + 1
		else:
			break

		print(left, right)

	print(res)
	print(right)


