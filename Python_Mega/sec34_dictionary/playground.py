import os, difflib, json




def dictionary_func():

     if os.path.exists('./files/data.json'):
          data = json.load(open('./files/data.json'))
          user_input = input('Enter a word: ')
          
          match_word = difflib.get_close_matches(user_input, data.keys())
          print(match_word)


if __name__ == '__main__':
     dictionary_func()


          

