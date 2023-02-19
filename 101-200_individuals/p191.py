import numpy as np


def p191(N):
	"""
	30 day period:

	with one late day at i

	i-1, 30-i, two valid period

	with no late day

	30, one valid period

	C[L, a, b], the number of valid period of length L, 
	having the last two days with status (a, b), 
	a, b in {0, 1} for absent/not-absent

	C[L-1, :, 0]  -> C[L, 0, 1]
				  -> C[L, 0, 0]

	C[L-1, 0, 1] -> C[L, 1, 0]
				 -> C[L, 1, 1]

	C[2, 0, 0] = 1
	C[2, 0, 1] = 1
	C[2, 1, 0] = 1
	C[2, 1, 1] = 1

	C[1, 0, 0] = 1
	C[1, 0, 1] = 1

	C[0, 0, 0] = 1

	"""

	C = np.zeros((N+1, 2, 2))

	C[2, 0, 0] = C[2, 0, 1] = C[2, 1, 0] = C[2, 1, 1] = 1 
	C[1, 0, 0] = C[1, 0, 1] = 1
	C[0, 0, 0] = 1


	for L in range(3, N+1):
		C[L, 0, 0] = np.sum(C[L-1, :, 0])
		C[L, 0, 1] = np.sum(C[L-1, :, 0])
		C[L, 1, 0] = C[L-1, 0, 1] + C[L-1, 1, 1]
		C[L, 1, 1] = C[L-1, 0, 1]

	cnt = 0
	# with one late day
	for i in range(1, N+1):
		# print("late on day", i)
		cnt += np.sum(C[i-1, :, :]) * np.sum(C[N-i, :, :])
		# print("total:", np.sum(C[i-1, :, :]) * np.sum(C[N-i, :, :]))

	cnt += np.sum(C[N, :, :])
	# print("no late days, total", np.sum(C[N, :, :]))

	return cnt

if __name__ == "__main__":
	print(p191(30))
	print(p191(4))



