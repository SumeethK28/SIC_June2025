import numpy as np

if __name__ == '__main__':
    array = np.array([[1,2,3,4,5], [6,7,8,9,0]])    # Broadcasting

    array2 = array + 5

    print(array2)