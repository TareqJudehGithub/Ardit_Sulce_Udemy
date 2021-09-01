import re

"""
Inputs in Python
 
 - input() prompts the user to enter input data
"""

def greet_user():
     name = input('What is you name? ').title()
     print(f'Hi, {name}')



def temp_today(temp):
    if temp > 25:
        return 'Hot'
    
    elif temp >= 15 and temp <= 25:
        return 'Warm'
    
    else:
        return 'Cold'


def old_str_format():
    
    valid_email = r'(^[a-z0-9._]{3}+@+[a-z]+\.[a-z]{3}$)'
    validator = re.compile(valid_email)

    name = input('Enter name: ').title()
    
    while True:
        email = input('Email: ').lower()

        if validator.fullmatch(email):
            return 'Your name is %s, and your email address is %s' % (name, email)

        else:
            print('Invalid email address format')


if __name__ == "__main__":
    # enter_temp = float(input('Enter temperature: '))
    # # print(temp_today(enter_temp))

    # # create a list from multiple inputs
    # grocery_basket = input("Enter items: ").title().split()
    # print(grocery_basket, end='\n')

    # # create int list from multiple inputs
    # numbers_list = list(map(int, input('Enter numbers: ').split()))
    # print(numbers_list, end='\n')

    print(old_str_format())

    

 