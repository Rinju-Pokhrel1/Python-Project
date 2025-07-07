#comparison function
import numpy as np

a = np.array([9, 12, 21])
b = np.array([21, 12, 9])

# use of less()
result = np.less(a, b)
print(result)    # Output: [ True False False]

# use of less_equal()
result = np.less_equal(a, b)
print(result)    # Output: [ True  True False]

# use of greater()
result = np.greater(a, b)
print(result)    # Output: [False False  True]

# use of greater_equal()
result = np.greater_equal(a, b)
print(result)    # Output: [False  True  True]

# use of equal()
result = np.equal(a, b)
print(result)    # Output: [False  True False]

# use of not_equal()
result = np.not_equal(a, b)
print(result)    # Output: [ True False  True]