import numpy as np

if __name__ == '__main__':
    print(0 * np.nan)
    print(np.nan == np.nan)
    print(np.inf > np.nan)
    print(np.nan - np.nan)
    print(np.nan in set([np.nan]))
    print(0.3 == 3 * 0.1)