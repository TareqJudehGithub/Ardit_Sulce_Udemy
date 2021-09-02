"""
for loop
 
 - for loop iterates over iterables right until the last item and then
   stop
"""

import math

# Rounding in Python

# round()
print('round ', round(9.4))

# ceil() rounds to the greater nearest integer
print('ceil ', math.ceil(9.4))

# floor() round to the least nearest integer
print('floor ', math.floor(9.4))

print('\n')

# =============================

# Iterating over lists
monday_temps = [9.1, 8.8, 7.6]


for temp in monday_temps:
     print(temp)


print('\n')

# =============================

# Iterating over dictionaries



class_5c_grades = {
     'Leen': 97.5,
     'Ela': 94,
     'Meral': 95,
     'Kamooleh': 84
}
names_list = list()
grades_list = list()

for k, v in class_5c_grades.items():
     names_list.append(k)
     grades_list.append(v)


# join both lists items as tuples

class_5c_tuple = zip(names_list, grades_list)

# put the tuple items in a new dictionary:
class_5c = dict(class_5c_tuple)
print(class_5c)


print('\n')

# =============================

# replace '+' with '00' in the dict values below 
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for num in phone_numbers.values():
     new_num = num.replace('+', '00')

     print(new_num)