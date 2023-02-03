import math
import matplotlib.pyplot as plt 


def p104_generation():
	"""
	Quicker if use the generating function?
	"""

	def fn(n):
		"""
		Generating function of fibonacci
		"""
		s = math.sqrt(5)
		# res = int((((1+s)/2)**n - ((1-s)/2)**n)/s)
		# print(res, '***********')
		return str((((1+s)/2)**n - ((1-s)/2)**n)/s)
		# result too large

	def check(n):
		l = [int(i) for i in n.split('.')[0]]
		if set(l[:9]) == set([1, 2, 3, 4, 5, 6, 7, 8, 9]) and set(l[-9:]) == set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
			return 1
		else:
			return 0
	
	n = 3
	while not check(fn(n)):
		n += 1

		if n % 10000 == 0:
			print(n)

	return n


def p104():
	"""
	> 1min
	HINT: for each cell, use a large INT, e.g. store 10**9 in one cell and calculate the meta-exceed from one cell to the upper cell.
	As it seems 1+1 takes a similar time of 10**n + 10**n ?
	List manipulation is more costly as it requires dynamic memory state change (...?) -- BRUSH UP YOUR PYTHON KNOWLEDGE!

	-------
	It's easy to just look out for the last 9 digits, as we only need to save the last 9 digits' result

	... * * * * * * * * * 
	... * * * * * * * * * 

	However, to account for the first 9 digits, we need to keep track of anything below them, but only keep aware of where another '1' will exceed from the add-up in the down-position digits

	* * * * * * * * * ... 
	* * * * * * * * * ...
					+1?
	And to see if the +1 is available from lower positions, all the digits need to be keep track of?

	But if we observe the structure of addings in larger digit numbers:

	3 4
	5 5
	8 9
	13 14 --> 144

	  8 9
	1 4 4
	1 12 13 --> 2 3 3

	So if we keep a separated record of the adds on every digit, every time the exceeded '1' will got pushed into the digit above. 

	This is exactly how to do "shushi". 

	Although the computation is the same, the benefit is to efficiently store up the digits in a data-structure rather as an object, and we will have more digits allowed for representation.

	---
	(This is a similar problem to *<100.)
	---
	The procedure:

	1. Keep 2 lists, [None], [None] to store up f1, f2 in the reversed order (for easier manipulation), add None to the tail of it to indicate the exhaustion. Maintain a clock t, starting from 3.
	2. t+=1, Manipulate f1 by adding f2 to it from the low digit position
		
		i = 0
		while f2[i]:
			n = f1[i] + f2[i]
			f1[i] += n % 10
			if f1[i+1]:
				f1[i+1] += n // 10 # could be > 1
			else:
				f1[i+1] = 1
				f1.append(None)
		check the first and last 1-9 digits of f1 
	3. t+=1. For the next step, in a similar way, manipulate f2 by adding f1 to it.

	4. repeat from step 2. Until the required is found. stop and return t.
	"""

	
	def check_1(l):
		if set(l[:9]) == set([1, 2, 3, 4, 5, 6, 7, 8, 9]) and set(l[-10:-1]) == set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
			return 1
		else:
			return 0

	def check_2(l):
		if set(l[:9]) == set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
			return 1
		else:
			return 0

	def check_3(l):
		if set(l[-10:-1]) == set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
			return 1
		else:
			return 0

	
	def run(check):
		#########
		# debug
		t_record = []
		# debug
		##########


		f1 = [1, None]
		f2 = [1, None]
		# if use 3 lists would have simpler format down below
		f = [f1, f2]

		t = 2 # time 2, check f2, time 1 check f1
	
		MAX_T = 100000

		# while t < MAX_T: # 
		while not check(f[t%2-1]):
			########
			# debug
			if check(f[t%2-1]):
				t_record.append(t)
			# debug
			#########


			# if t % 10000 == 0:
				# print(t)
			t += 1
			
			if t%2 == 1: # odd times, 1 <- 2
				l1, l2 = f[1], f[0]
			else: # even times, 2 -> 1
				l1, l2 = f[0], f[1]

			# adding two lists
			i = 0 
			while l1[i] is not None:
				n = l1[i] + (l2[i] if l2[i] is not None else 0)
				
				if l2[i] is None:
					l2.append(None)
				l2[i] = n % 10	
				
				if n // 10: # if need to add exceed
					if l2[i+1] is not None:
						l2[i+1] += n // 10
					else:
						l2[i+1] = 1
						l2.append(None)
				
				i += 1

		# print(t)
		return t_record

	# run(check_1)
	t1 = run(check_2) # 541
	t2 = run(check_3) # 2749

	return t1, t2

if __name__ == "__main__":
	# print(p104_generation())

	t1, t2 = p104()

	plt.figure()
	plt.plot(t1)
	plt.plot(t2)
	plt.show()
	plt.close()



