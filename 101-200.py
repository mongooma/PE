from fundamentals.cores import Cores, Structures, GraphTheory, Array
import time
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import copy
from itertools import cycle


def p107():
	"""
	MST problem
	"""
	mat_raw = ''''''

	weighted_edges = []
	nodes = []
	for i, l in enumerate(mat_raw.split('\n')):
		for j, w in enumerate(l.split(',')):
			if w != '-':
				weighted_edges.append((i, j, int(w)))
				nodes.extend([i, j])

	nodes = list(set(nodes))

	MST_edges = GraphTheory().Prim(nodes, weighted_edges)
	max_saving = sum([w for u, v, w in weighted_edges])/2 - \
				sum([w for u, v, w in MST_edges])

	return max_saving