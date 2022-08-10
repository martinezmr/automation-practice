import numpy as np

first_numpy_array = np.array([1,2,3,4])
print(first_numpy_array)

array_with_zeros = np.zeros((3,3))
array_with_zeros

array_with_ones = np.ones((3,3))
array_with_ones

array_with_empty = np.empty((2,3))
array_with_empty

np_arange = np.arange(12)
print(np_arange)

np_arange.reshape(3,4)

np_linspce = np.linspace(1,6,5)
print(np_linspce)

oneD_array = np.arange(15)
print(oneD_array)

TwoD_array = oneD_array.reshape(3.5)
print(TwoD_array)

ThreeD_array = np.arange(27).reshape(3,3,3)