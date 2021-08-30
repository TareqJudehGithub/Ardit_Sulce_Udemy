"""
Lists
 
 - Lists are mutable, ordered data structure type.
 - range(start, stop, stepover)

"""
# Creating a list using range()

one_ten = list(range(1, 11))
print(one_ten)


print('\n')


# calculate the average of students average
# students_grades = list([91, 75, 88, 69])

def mean(grades):
     grades_total = sum(grades)
     grades_count = len(grades)
     result = grades_total / grades_count
     return result


if __name__ == '__main__':
     
     student_grade = list(map(int, input('Enter students grades: ').split()))

     print(mean(student_grade))


"""
dir() keyword
 - dir lists all attributes of a data type
 - dir(list)

help(object.attribute)
 - help(returns an description/documentation of a datatype/attribute)
"""


# Python program showing how to
# multiple input using split
 
# taking two inputs at a time
# x, y = input("Enter a two value: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
# print()
 
# # taking three inputs at a time
# x, y, z = input("Enter a three value: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)
# print()
 
# # taking two inputs at a time
# a, b = input("Enter a two value: ").split()
# print("First number is {} and second number is {}".format(a, b))
# print()
 
# # taking multiple inputs at a time
# # and type casting using list() function
# x = list(map(int, input("Enter a multiple value: ").split()))
# print("List of students: ", x)