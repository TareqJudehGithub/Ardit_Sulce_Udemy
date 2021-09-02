import re
"""
while loop iterates over iterables until a certain condition is met.
 - input() should be declared INSIDE the while loop.
 - use break to break out from the loop allowing the interpretter to read
   the rest of the code.
"""

def username_check():
     validator = re.compile(r'^[a-zA-z0-9_.]{5,12}$')
     
     try:
          while True:   
               username = input(' Enter a username: ')   

               if validator.fullmatch(username):
                    print('Your username is valid.')
                    print('')
                    break
               
               else:
                    print('Enter a valid username')
                    

     except ValueError as err:
          raise err
     
     else:     
          return f'Your user name is %s' %username


print(username_check())