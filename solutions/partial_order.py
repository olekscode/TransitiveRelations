import numpy as np
import math

def int_to_binary_matrix(k, nrows):
    """Converts integer to its binary representation
    in the form of a square matrix"""

    binary = "{:0{}b}".format(k, nrows ** 2)
    elements = [int(char) for char in binary]
    matrix = np.array(elements).reshape(nrows, nrows)
    return matrix

def is_reflexive(matrix):
    n = len(matrix)

    for i in range(n):
        if matrix[i, i] == 0:
            return False

    return True

def is_antisymmetric(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i):
            if ((matrix[i, j] == 1) and
               (matrix[j, i] == 1)):
                return False

    return True

def is_transitive(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i, j] == 1:
                for k in range(n):
                    if ((matrix[j, k] == 1) and
                       (matrix[i, k] == 0)):
                        return False

    return True

def is_partial_order(matrix):
    return ((is_reflexive(matrix) and
           is_antisymmetric(matrix)) and
           is_transitive(matrix))

def number_of_partial_orders(size):
    nrelations = 2 ** (size * size)
    npartord = 0

    for k in range(nrelations):
        relation = int_to_binary_matrix(k, size)

        if is_partial_order(relation):
            npartord += 1

    return npartord

def C(n, k):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))

def S(n, k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    if n == k:
        return 1
    if k > n:
        return 0
    return S(n - 1, k - 1) + k * S(n - 1, k)

def N(n, k):
    res = 0
    for s in range(k + 1):
        res += C(n, s) * S(n - s, k - s)
    return res

def number_of_transitive_relations(size):
    print(S(6, 3))
    print(number_of_partial_orders(size))
    res = 0
    for k in range(1, size + 1):
        res += N(size, k) * number_of_partial_orders(k)
    return res
    
