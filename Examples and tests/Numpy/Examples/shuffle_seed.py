import numpy as np
array = [1, 2, 3, 4, 5]
def shuffle_seed(array):
    seed = np.random.randint(2**31)
    np.random.seed(seed)
    result = np.random.permutation(array)
    return result, seed

print(shuffle_seed (array))

