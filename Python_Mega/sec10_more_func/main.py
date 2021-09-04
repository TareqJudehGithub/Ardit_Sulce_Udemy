# function header(parameters):
def greet(name='your name', age=45):
     # function body
    return 'Hello, %s! Your age is %d.' % (name, age)

# call the function(arguments)



"""
Default parameters:
 - func_header(name='john smith', age=45)
 - A function will execute successfully without arguments in case default
   parameters were specified.
 - ALL paramaters should have a default parameter in case we've decided to 
   include default parameters, or we will be getting a SyntaxError like the
   one below:
    SyntaxError: non-default argument follows default argument

Arguments keywords:
 - func_call(name='john smith', age=45)
 - order of arguments does not matter in case arguments have keywords
 - func_call(age=45, name='john smith')

 *args and **kwargs
  - *args save the trouble of including more than one parameter in case
    we got many arguments.

  - Similar to *args, **kwargs provides a cleaner and more readable code
    through minimizing parameters count.
  - With **kwargs, all arguments should have keys.  
  - In the function body, **kwargs works just like a dictionary! Where 
    the argument is the key.   kwargs['argument-name']




"""
def mean(*args):
     return sum(args)/len(args)


def full_name(**name):
  print("His last name is " + name["lastname"])
               


# exercises:

# add all arguments to a list, sorting the last and returns all items
# in uppercase format.

def cart(*args):
    basket = list()
    for item in args:
     basket.append(item.upper())
    basket.sort()
    
    return basket

def mean2(**kwargs):
     return sum(kwargs.values()) /len(kwargs)


def find_winner(**kwargs):
     # return the highest winner (name not score)
     return max(kwargs.keys())
 

if __name__ == "__main__":
     print(greet(name='john smith', age=46), end='\n\n')
     print(mean(95, 87, 64, 78, 81))
     full_name(first_name='john', lastname="smith")
     print(cart('orange', 'lemon', 'apple', 'banana'))
     print(mean2(n_1 =100, n_2=200, n_3=250))
     print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))