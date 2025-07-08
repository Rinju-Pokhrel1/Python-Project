#reshaping an array
import numpy as np


input_str = input()
elements = list(map(int, input_str.strip().split()))


if len(elements) != 8:

    exit()

arr_1= np.array(elements)

arr_2 = arr_1.reshape((2, 4), order='C')

print(arr_2)
