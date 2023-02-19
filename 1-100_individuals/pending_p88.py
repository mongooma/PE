import PE
from PE.cores import Cores


def p88(N):
	"""
	For every composite, get full factor decomposition

	N = 2^(p1) * 3^(p2) * ...

	enumerate from the smallest composite,
	to reach the min composite for some k, 
	compose the sum using all factors

	sum_N = (2 + 2 + 2 + ... + 2) + (3 + 3 + 3 + ...) + ()

	It is provable that this sum of factors is the lowest for N;
	Therefore we reach the min N for some k;

	Hypothesis:
	if we have reached k with S, 
		then all k_i < k unreached could be filled by the same S
	(good for 2<=k<=12)
	(seems troublesome)

	---

	Primes are not applicable, since it has same sum and product of the factors
	"""

	MAX = 100000
	primesUnderMax = Cores().primesBelowN(MAX)
	prime_set = set(primesUnderMax)
	
	# k_filled = [0 for i in range(N+1)]
	curr_k_max = -1

	min_set = set()

	for n in range(2, MAX):
		if n not in prime_set:
			decomp = list(Cores().primeFactorDecompose(n, primesUnderMax))

			sum_N = sum([p*k for p, k, _ in decomp])
			num_decomp = sum([k for p, k, _ in decomp])

			# if not k_filled[(n - sum_N) + num_decomp]:
			if curr_k_max < (n - sum_N) + num_decomp:
				curr_k_max = max(curr_k_max, (n - sum_N) + num_decomp)
				min_set.add(n)
				if curr_k_max >= N:
					print("filled")
					break
				# print(n, "reached k", (n - sum_N) + num_decomp)
				# k_filled[(n - sum_N) + num_decomp] = 1


	print(n)
	# print(min_set)  # error

	return sum(list(min_set))

if __name__ == "__main__":
	print(p88(12000))




