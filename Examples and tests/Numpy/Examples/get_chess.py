from re import A
import numpy as np

def get_chess ():
    length_of_square = int(input('Input the length of the square: '))
    array_length = length_of_square**2
    zero_array = np.zeros(array_length)
    length_zero_array = len(zero_array)
    for i in range(1,length_zero_array,2):
        zero_array[i] = 1
    zero_array.shape = (length_of_square, length_of_square) 
    print (zero_array)
    
get_chess ()