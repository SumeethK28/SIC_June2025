import numpy as np

def f(x, y):
    return 10 * x + y

if __name__ == '__main__':
    array = np.fromfunction(f, (5,4), dtype = float)

    print(array)
    
    # Slicing of numpy arrays 
    print(array[2, 3])   # Just prints the element of Row-3 and Column-4
    print(array[0:5, 1])   # Prints elements of Column-2 from Row-1 to Row-6 (it has only 5 rows so exclusive of Row-6)
    print(array[:, 1])   # Prints elements of Column-2 of all Rows
    print(array[1:3, 2])   # Prints elements of Column-3 from Row-2 to Row-4 (exclusive of Row-4)