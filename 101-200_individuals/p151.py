import copy
from copy import deepcopy
import numpy as np

def p151():
	"""
	Enumerate:
	
	node: (n1, n2, n3, n4, n5)

	E[n1, n2, n3, n4, n5]: 
		the expected number of this node in the tree

	* each branch having different possibilities
	  b1,      b2,
	   o      o
		\    /
		 o  /
		 ...
		 (0, 0, 1, 0, 0)
		  p1, p2  -> E = 1 * p1 + 1 * p2

	To get the branch possibilities, we need to enumerate from top;

	"""

	E_T = np.zeros((17, 17, 17, 17, 17))  # maximum 4 same sized sheets for A5

	def E(n1, n2, n3, n4, n5, p):
		"""
		p is the total path probability until this node
		"""
		if n1 == n2 == n3 == n4 == n5 == 0:
			return

		# fill [0, ..., 0, 1, 0, ..., 0]
		if n1 + n2 + n3 + n4 + n5 == 1:
			if n2 > 0:
				E_T[0, 1, 0, 0, 0] += p
			if n3 > 0:
				E_T[0, 0, 1, 0, 0] += p
			if n4 > 0:
				E_T[0, 0, 0, 1, 0] += p
		

		num = n1 + n2 + n3 + n4 + n5
		E(n1-1, n2+1, n3+1, n4+1, n5+1, p*n1/num) if n1 > 0 else None
		E(n1, n2-1, n3+1, n4+1, n5+1, p*n2/num) if n2 > 0 else None
		E(n1, n2, n3-1, n4+1, n5+1, p*n3/num) if n3 > 0 else None
		E(n1, n2, n3, n4-1, n5+1, p*n4/num) if n4 > 0 else None
		E(n1, n2, n3, n4, n5-1, p*n5/num) if n5 > 0 else None

		return
	
	E(1, 0, 0, 0, 0, 1)
	# totalBranchCnt = E_T[1, 0, 0, 0, 0]
	singleSheetCnt = E_T[0, 1, 0, 0, 0] + E_T[0, 0, 1, 0, 0] + E_T[0, 0, 0, 1, 0]

	# print("E_T[1, 0, 0, 0, 0]", totalBranchCnt)
	# print("E_T[0, 0, 0, 0, 1]", E_T[0,0,0,0,1])

	return singleSheetCnt

if __name__ == "__main__":
	print('{:.6f}'.format(p151()))






