"""
- Objects are created (instantiated) by classes

- self is var that holds the obj instance created by a class
  The keyword self represents the instance of a class and binds the attributes 
  with the given arguments.

"""
class User:
  # init method or constructor   
  def __init__(self, name, age):
      # attributes
      self.name = name
      self.age = int(age)
      print("self: %s" % self)

# initialize a instance

user_1 = User('Emma', 25) # 'Emma' and 25 are passed as arguments, these \ 
# arguments will be passed to the __init__ method to initialize the object.

user_2 = User('Mike', '30')
print(user_2.age)
    
