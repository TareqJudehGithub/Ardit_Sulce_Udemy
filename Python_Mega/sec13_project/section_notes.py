"""
Reading JSON files in Python
 - In order to to be able to read JSON files in Python, we need to import
   json module
 - .load('file_path/file_name') method is used to read json files.
 - json files data, are set in a dictionary format.
 - Use different iterating techniques to extract and read json data.
"""

import json


read_json = json.load(open('./files/data.json'))

# for loop:
for key, value in read_json.items():
     # print both keys and values
     # print(key, value)
     pass


# dictionary Comprehensions:
data = {k: v for (k,v) in read_json.items()}

# print only keys
print(data.keys())