#array creation from list
# Replace ___ with your code
import numpy as np

# take a list input
user_input = input()

# safely convert the user input into a list
list1 = eval(user_input)

# convert list1 into a NumPy array
list=np.array(list1)

# print the resulting array
print(list)