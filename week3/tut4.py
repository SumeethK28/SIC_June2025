import pdb
pdb.set_trace()

import numpy as np

if __name__ == '__main__':
    matrix1 = np.array([[3, 3, 4], [2, 3, 9]])
    matrix2 = np.array([[2, 5, 4], [2, 3, 19]])

    matrix3 = np.dot(matrix1, matrix2.T)   # It wont multiply two matrices having same size, any one matrix should be tranposed to do dot product

    print(matrix1 + matrix2)
    print(matrix1 - matrix2)
    print(matrix1 * matrix2)   # This is not dot product, just normal multiplication
    print(matrix3)
    print(matrix1 / matrix2)