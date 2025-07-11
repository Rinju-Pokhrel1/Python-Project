import numpy as np

# create array A with numbers from 1 to 10 using arange()
A = np.arange(1,11)

# create array B with numbers from 11 to 20 using arange()
B = np.arange(11,21)

# add A and B element-wise
C = [a+b for a,b in zip(A,B)]

# square each element of C
D = [c**2 for c in C]

# calculate the sum of all elements in D
sum_value=sum(D)

# print the final sum
print(sum_value)