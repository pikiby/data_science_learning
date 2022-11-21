import numpy as np

def get_chess ():
    length_of_square = int(input('Input the length of the square: '))
    zero_array = np.zeros([length_of_square, length_of_square])
    zero_array[1::2, ::2] = 1
    zero_array[::2, 1::2] = 1
    print(zero_array)
    
get_chess ()