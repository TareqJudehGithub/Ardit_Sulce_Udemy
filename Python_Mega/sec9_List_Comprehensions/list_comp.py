"""
List comprehension
 - List comprehensions is Python unique feature.
 - List comprehension creates modified new lists in much lesser code.
"""

# clean the numbers is excel_list to 10s digit instead of 100s.

excel_list = [101, 2679, 36, 1094, -1500]

# if the number is 100 or higher clean it, if it is less then leave it as it:
clean_list = [float(i/10) if i >= 100 or i < 0 else float(i) for i in excel_list ]


# return only int items from some_list:
some_list = [99, 'no data', '94', 'milk', 1050, 56]

def int_only(param):
    return [i for i in param if isinstance(i, int)]


# replace str for zeros
def zero_for_str(param):
    return [i if isinstance(i, int) else 0 for i in param]


# convert str to int and find the sum
str_list = ['99', '100', '94', '55', '50', '190']

def int_sum(param):
     return sum([float(i) for i in param])


if __name__ == '__main__':
     print(clean_list)
     print(int_only(some_list))
     print(zero_for_str(some_list))
     print(int_sum(str_list))