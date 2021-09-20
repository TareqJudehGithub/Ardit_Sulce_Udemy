"""
Handling errors in Python
"""
def divide_nums(num1, num2):
  try:
     result = num1/num2
  
  except ZeroDivisionError as err:
    raise "Cannot divide by zero!!!"

  else:
    return result

def cart():
  return list(map(str, input("Add your items here: ").title().split())) 
  
  
if __name__ == "__main__":
  num1, num2 = list(map(int, input("Enter numbers: ").split()))
  
  print(divide_nums(num1, num2))
  grocery = list(map(str, input("Enter your items here: ").split()))
  print("")
  print(grocery)
  for item in grocery:
    print(item)
  

print(cart())

