"""
Lists
 
 - Lists are mutable, ordered data structure type.
 - range(start, stop, stepover)

"""
# Creating a list using range()

one_ten = list(range(1, 11))
print(one_ten)

one_ten.insert(len(one_ten), 11)
print('\n')


# calculate the average of students average
# students_grades = list([91, 75, 88, 69])

def mean(grades):
     grades_total = sum(grades)
     grades_count = len(grades)
     result = grades_total / grades_count
     return result


"""
dir() keyword
 - dir lists all attributes of a data type
 - dir(list)

help(object.attribute)
 - help(returns an description/documentation of a datatype/attribute)
"""


# Now, calculate avg heights for students in a dict

grade_5_b = {
     'leen': 150,
     'ela': 153,
     'meral': 145,
     'ghazi': 135,
     'kamooleh': 159
}

def avg_height():
     """Average height calculator"""
     return sum(grade_5_b.values()) / len(grade_5_b)

new_set = {1, 2, 3, 5, 6}
new_set.add(4)
# sorted(new_set)

if __name__ == '__main__':
     
     student_grade = list(map(int, input('Enter students grades: ').split()))
     print(mean(student_grade))
     print('')

     print(avg_height())

     print(new_set)
     print(one_ten)