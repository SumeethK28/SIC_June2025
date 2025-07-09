import numpy as np 

if __name__ == '__main__':
    arr1 = np.zeros(3)
    arr2 = np.zeros((1, 4))
    arr3 = np.zeros((2, 5))
    arr4 = np.full((5, 5), 10, float)
    arr5 = np.arange(1, 5)

    print(type(arr1))
    print(type(arr2))
    print(arr4)
    print(arr5)