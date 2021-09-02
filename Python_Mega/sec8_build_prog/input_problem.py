import re
# Write a program, that asks the user for input(s), until
# the user types \end
# user inputs should not include any symbols.
# return all user outputs



def inputs_problem():
     
     inputs = list()
     inputs_str = str()
     interrogatives = ('how', 'what', 'why', 'where')
     input_validator = re.compile(r"[\w a-z0-9']*$")

     while True:
          user_input = input('Type your input: ')

          if input_validator.fullmatch(user_input):

               if user_input.startswith(interrogatives):
                    inputs.append(user_input.capitalize() + '?')
               else:
                    inputs.append(user_input.capitalize() + '.')
          
          else: 
               print('Bad input format.')
               print('')
               continue         

          print
          more_input = input('More input? (yes/no) ')
          if more_input == 'no'.lower():
               inputs_str = ' '.join(inputs)
               return inputs_str
          else:
               continue


if __name__ ==  '__main__':
     print(inputs_problem())
