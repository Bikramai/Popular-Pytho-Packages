import numpy as np

array = np.array([1, 2, 3])
print(array)
print(type(array))
print('\n')

#Matrix in array

array = np.array([[1, 2, 3], [4, 5, 6]]) # matrix of two rows and 3 cols
print(array)
print(array.shape)
print('\n')

# Matrix of three rows and colunms
array = np.zeros((3, 4), dtype=int) #zeros method
print(array)
print('\n')

# Matrix of three rows and colunms
array = np.ones((3, 4), dtype=int) #ones method
print(array)
print('\n')

# Matrix of three rows and colunms
array = np.full((3, 4), 5, dtype=int) #full method
print(array)
print('\n')

# Matrix of three rows and colunms
array = np.random.random((3, 4)) #random method
print(array)
# print(array[0, 0]) #get the element of first row and first col
# print(array > 0.3)
# print(array[array > 0.2]) #boolean expression
# print(np.sum(array)) #sum
print(np.floor(array)) #floor method
print(np.ceil(array)) #ceil method
print(np.round(array))
print('\n')

# Arthmatic operations between arrays and numbers
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])

print(first + second)

# real world senerios
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
print('\n')

#if you want to do on python with out using Numpy. Our code be longer. Let's see
dimensions_inch = [1, 2, 3]
dimensions_cm = [x * 2.54 for x in dimensions_inch ]