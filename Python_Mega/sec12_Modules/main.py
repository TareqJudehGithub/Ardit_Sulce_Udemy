"""
Modules
 - not built it methods and functions are called standard modules. 
 - Modules needs to be imported in order to be able to use them and all
   their methods and functions.
"""

import sys
import time
import os

# show where python interpreter is installed:
print('Python located at:')
print(sys.prefix, end='\n\n')

# list of all built-in modules in Python:
built_in = sys.builtin_module_names

# lets try the sleep built-in method
# build a function that count down from 10 to 1
print('')
print('Countdown using time.sleep() module and method')


def countdown():
    for i in range(3, -1, -1):
        if i < 1:
            print('GO!!')
        else:
            time.sleep(1)
            print(i)


print('')
print('Check if file exists using module os.path.exists()')


def check_and_open():
    if os.path.exists('./files/vegetables.txt'):
        with open('./files/vegetables.txt', mode='r') as file:
            read_me = file.read()
            return read_me

    else:
        return 'File not found!'


if __name__ == '__main__':
    countdown()
    print(check_and_open())
