"""
dictionaries

 - dictionary is made of pairs of keys and values. 
"""

grade_5_b_heights = {
     'leen': '150 cm',
     'ela': '153 cm',
     'meral': '145 cm',
     'ghazi': '135 cm',
     'kamooleh': '159 cm'
}

# accessing a dict key:
# get me ghazi's height
print(grade_5_b_heights['ghazi'])



# convert the following list to a dict:

grade_5_b_grades = [
     ['leen', 97.5],
     ['ela', 92],
     ['meral', 94],
     ['ghazi', 85],
     ['kamooleh', 88]
]

to_dict = dict(grade_5_b_grades)

print(to_dict)

print(to_dict['leen'])