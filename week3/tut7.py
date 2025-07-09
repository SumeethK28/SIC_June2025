

import numpy as np

if __name__ == '__main__':
    array = np.zeros((8,8), dtype = int)

    print(array)

    array[::2, ::2] = 8   #Starting from row-index-1 and there after, for all alternatives rows, and for all columns from index 0 and there after alternative columns, replace the cells with value 8
    array[::2, 1::2] = 1   # Odd indexed-rows Even Indexed-Columns

    print(array)