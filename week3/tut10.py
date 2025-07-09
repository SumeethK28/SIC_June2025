import numpy as np

if __name__ == '__main__':
    arr = np.random.randint(10, size = (5,5))  # random method can take only one parameter i.e., size of array but randint takes two parameters i.e., range of numbers to generate random numbers and then size of array to display the random numbers 

    print(arr)

    values = arr - np.mean(arr)
    print(values)

    values = np.std(arr)
    print(values)

    print((arr - (np.mean(arr))) // (np.std(arr)))