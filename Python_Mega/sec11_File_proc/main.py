"""
FILE IO

 file.read()
  - After python finishes reading a file, the cursor will wait AFTER the last 
    char in that file. 
    file_a = open('fruits.txt', mode='r')
    file_a.read()
          pear
          apple
          orange
          watermelon
          pomegranate
          lemon
          strawberries
          bluberries(THIS IS WHERE THE CURSOR will be at)
 with() content manager
  - With with() closing the file occurs automatally after Python reads the file.
     with open('file_name', mode='r') as file:
          new_file = file.read() 

 Writing to a file
     mode='w'  writes new contents to a file and creates one in case the file
     does not exist.
     
"""

# assigning file to a variable:
my_file = open(file='./files/fruits.txt', mode='r')

# using with() content manager:
with open('./files/fruits.txt', mode='r') as file:
     fruits_read = file.read()


# writing to a file using mode='w'
with open('./files/cart.txt', mode='w') as file:
     file.write('Bread\nMilk\nCereal\n')
     
# read the newly created file cart
with open(file='./files/cart.txt', mode='r') as file:
     cart = file.read()
     
# read the first 92 char in the bears.txt file:
with open(file='./files/bears.txt', mode='r') as file:
     
     read_me = file.read()
     # using string slicing to print out only the 1st 90 characters
     first_90char = read_me[:90]


# count how many char in bears.txt

def count_char(char, filepath):
    with open(filepath, mode='r') as file:
        for c in file:
          return c.count(char)



# read the first ninety characters and write them to a new file:
# def read_and_write():
#      with open('./files/bears.txt', mode='r') as file:
#           first_90char = file.read()[:90]
    
#      with open('./files/first.txt', mode="w+") as first:
#           first.write(first_90char)
#           # seek() returns the cursor in target file to a specified place.
#           first.seek(0)
#           return first.read()


# append bears.txt into bears2.txt
# def read_and_append():
#      with open('./files/bears.txt') as bear1:
#           bear_1 = bear1.read()

#      with open('./files/bears2.txt', mode='a+') as bear2:
#           bear2.write(bear_1)
#           bear2.seek(0)

#           return bear2.read()


# copy n-times(E):
def copy_n_times():
     with open('./files/data2.txt', mode='a+') as file:
          file.seek(0)
          data = file.read()
          file.seek(0)
          file.write(data)
          file.write(data)

          return file.read()
         
         
          
if __name__ == "__main__":
     # reading a file
     print(my_file.read())

     # closing a file
     my_file.close()

     # print(fruits_read)
     # print(cart)
     # print(len(cart), end='\n\n')
     # print(first_90char, end='\n\n')
     # print(count_char(char='b', filepath='./files/bears.txt'), end='\n\n')
     # print('read and write..and read :D')
     # print(read_and_write(), end='\n\n')
     # print(read_and_append())
     print(copy_n_times())