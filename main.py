import numpy as np
from timer import timeit

def int_to_binary_matrix(k, nrows):
	"""Converts integer to its binary representation
	in the form of a square matrix"""

	binary = "{:0{}b}".format(k, nrows ** 2)
	elements = [int(char) for char in binary]
	matrix = np.array(elements).reshape(nrows, nrows)
	return matrix

def is_transitive(matrix):
	n = len(matrix)

	for i in range(n):
		for j in range(n):
			if matrix[i, j] == 1:
				for k in range(n):
					if (matrix[j, k] == 1) and (matrix[i, k] == 0):
						return False

	return True

@timeit
def number_of_transitive_relations(size):
	nrelations = 2 ** (size * size)
	ntransitive = 0

	for k in range(nrelations):
		relation = int_to_binary_matrix(k, size)

		if is_transitive(relation):
			ntransitive += 1

	return ntransitive


if __name__ == '__main__':
	size = 4
	ntransitive = number_of_transitive_relations(size)
	print(ntransitive)