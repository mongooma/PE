import numpy as np

def p164():
	"""
	(DP)

	How many 20 digit numbers n (without any leading zero) 
	exist such that no three consecutive digits of n have 
	a sum greater than 9?

	The count of valid arrays of length L, starting at (a, b)
	C[L, a, b]

	a, (b, i, ...

	C[L, a, b] = sum([C[L-1, b, i] for i in range(9-a-b+1)])

	C[2, i, j] = 1, i + j <=9

	sum all C[20, :, :] except C[20, 0, :]

	"""

	C = np.zeros((21, 10, 10))

	for i in range(10):
		for j in range(10):
			C[2, i, j] = 1

	for L in range(3, 21):
		for a in range(10):
			for b in range(9-a+1):
				C[L, a, b] = sum([C[L-1, b, i] for i in range(9-a-b+1)])

	return np.sum(C[20, 1:, :])


if __name__ == "__main__":
	print(p164())
