import numpy as np

if __name__ == '__main__':
    # tile method prints the given array dimension with given number of times 

    chess_board = np.tile(np.array([["*"," "], [" ","*"]]), (4,4))
    # chess_board = np.tile(np.array([[1,0], [0,1]]), (4,4))    

    print(chess_board)

    list1 = []
    for array in chess_board:
        list1 = list(array)
        string = " ".join(map(str, list1))
        print(string)