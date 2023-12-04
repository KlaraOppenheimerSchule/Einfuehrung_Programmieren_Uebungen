# Creating List (instead of Array -> see readme.md)
list_forward = [i for i in range(10)]
print("List:", list_forward)

# Creating Array with numpy
import numpy as np

numpy_array = np.array([i for i in range(10)])

# Solution 1
list_backwards = list_forward[::-1]
print("Solution 1:", list_backwards)

# Solution 2 (using reversed Function)
list_backwards = list(reversed(list_forward))
print("Solution 2:", list_backwards)
