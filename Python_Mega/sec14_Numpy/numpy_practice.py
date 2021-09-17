""" Numpy

 - Numpy is a  fundamental package for scientific computing with Python.
 - Official page: https://numpy.org/
 - Numpy comes installed with Pandas library.


"""
import numpy


# .arange(int) created a new array with the specified int number.
n = numpy.arange(27)
print(n)
print(type(n))
print(len(n))

print("")
# creating multi-dimintion array
# .reshape() method creates a multi dimintion array
# numpy.arrange(int).reshape(numb_of_arrs, num_of_rows, num_of_columns)

new_array = numpy.arange(12)
print(new_array)

print("")
print("two dimensional array")
# two-dimintion array
two_dim_arr = new_array.reshape(3, 4)
# .reshape(rows, columns)
print(two_dim_arr)

print("")
print("three dimensional array")
# three-dimensional array
# three-dimensional array are less frequently used than two-dimensional array
three_dim = numpy.arange(24).reshape(3, 2, 4)
print(three_dim)
