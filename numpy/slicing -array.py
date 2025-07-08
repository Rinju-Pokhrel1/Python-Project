#slicing 3d array
import numpy as np
list1 = eval(input())
arr = np.array(list1)

print(arr[0])
print(arr[1, :, 2])
print(arr[:, 1])