import numpy as np



def p116_117(N, L_min, L_max):
	"""
	modified from p114, 115:

	1. Fixed length tiles
	2. could be continous 

	L_min, L_max,

	S[n, k], pad length k block ending at pos n
    

    . .  .
	- -  -  -   ...   -
           n-k        n
	


	n >= k
	S[n, k] = sum([S[n_pre, k_pre]
				   for n_pre in range(L, n-k)
				   for k_pre in range(L, n-k)	
				   ])

	S[L_min, L_min] = 1
	S[<L_min, :] = 0

	"""
	S = np.zeros((N+1, N+1))

	S[L_min, L_min] = 1

	for n in range(L_min+1, N+1):
		for k in range(L_min, min(L_max+1, n+1)):
			S[n, k] = 1 + sum([S[n_pre, k_pre]
						   for n_pre in range(L_min, n-k+1) # n-k inclusive
						   for k_pre in range(L_min, L_max+1)	
						   ])

	print(S)
	return np.sum(S[:, :]) + 1  # +1 for 117 


if __name__ == "__main__":
	print(p116_117(5, 2, 2))
	print(p116_117(5, 3, 3))
	print(p116_117(5, 4, 4))

	print(p116_117(50, 2, 2) + p116_117(50, 3, 3) + p116_117(50, 4, 4)) # 116

	print(p116_117(5, 2, 4)) 
	print(p116_117(50, 2, 4)) # 117




