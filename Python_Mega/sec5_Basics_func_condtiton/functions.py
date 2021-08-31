"""
Functions in Python

 isinstance(obj, class)
 - isinstance() is a function that gets two arguments, an object 
  and a class. 
 - isinstance() checks if the object is an instance of the class and returns 
   True or False.
"""

# write a func that calculate the mean of a list or a dict
grade_5b = {
     'leen': 97.5,
     'ela': 89,
     'meral': 92,
     'ghazi': 85,
     'kamooleh': 87
}
grades_5b_list = [ 90, 86, 79, 86, 83]

def mean_calc(grades):
     """mean calculator"""
     # check iterable type using type() keyword
     if type(grades) == list:
          mean = sum(grades) / len(grades)

     # check iterable type using isinstance() keyword
     elif isinstance(grades, dict):
          mean =sum(grades.values()) / len(grades)     

     # else:
     #      mean =sum(grades.values()) / len(grades)
     
     return mean


def square_area(x):
     """square area calculator"""
     area = x ** 2
     return area


def str_length(my_str):
     """check string length"""
     return len(my_str) >= 8


def warm_or_cold(temp):
     """check temperature"""
     return 'Warm' if temp > 7 else 'Cold'


# more conditionals case
def temp_today(temp):
    if temp > 25:
        return 'Hot'
    
    elif temp >= 15 and temp <= 25:
        return 'Warm'
    
    else:
        return 'Cold'


# using ternary operator
if __name__ == '__main__':
     # mean calculator
     print(mean_calc(grade_5b))

     print('')
     print('Square Area')
     print(square_area(4))

     print('')
     print('check string length')
     print(str_length('1234567'))  # >>> $ False

     print('')
     print('check temp')
     print(warm_or_cold(-10))

     print('')
     print('check temp V2')
     print(temp_today(10))



     