"""
String formatting in Python
 - More on: 
     https://pyformat.info/

"""


def greet_user():
     name = input('What is your name? ')
     # this is the a string formatting method introduced in Python 2
     return "Hello, %s!" %name.title()

     # using format()
     return "Hello, {}!".format(name.title) 

     # using f string
     return f"Hello, {name.title()}!"


def user_details():
     name = input('Name? ')
     age = int(input('Age? '))
     
     return 'You name is %s, and you age is %d' % (name.title(), age)

if __name__ == "__main__":
     print(greet_user())
     print(user_details())
   
     print('{:_<10}'.format('test'))