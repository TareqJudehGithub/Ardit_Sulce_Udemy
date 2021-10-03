"""
- Objects are created by classes

- self is var that holds the obj instance created by a class

"""
class User:
  def __init__(self, name, age):
      self.name = name
      self.age = int(age)
      print("self: %s" % self)

user_1 = User('Emma', 25)
user_2 = User('Mike', '30')
print(user_2.age)
    
