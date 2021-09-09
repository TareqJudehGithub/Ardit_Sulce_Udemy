import json
import os
from difflib import get_close_matches
import mysql.connector


# sql connection
conn = mysql.connector.connect(
    user = 'root',
    password = 'pass123@',
    host = 'localhost',
    database = 'people'
)

# query MySQL
cursor = conn.cursor()
query = cursor.execute()



def restart():
    while True:
        restart_program = input('Search another word? (y/n) ').lower()
        if restart_program == 'y':
            return dictionary()
        if restart_program == 'n':
            return 'Thank you. Good bye!'
        else:
            print('Invalid input!', end='\n\n')

            continue
        
    


def dictionary():
    if os.path.exists('./files/data.json'):
        
        # load and read a json file
        data = json.load(open('./files/data.json'))

        while True:
            user_entry = input('Enter a word, or type \quit to end program.\n').lower()
            print('')
            # matching word:
            match_word = get_close_matches(word=user_entry, possibilities=data.keys())

            if user_entry == '\quit':
                return 'Thank you. Good bye!' 

            elif user_entry == data.keys() or user_entry in data.keys():

                print(" ".join(data[user_entry]), end='\n\n') 
                return restart()
            
             
            elif user_entry.title() == data.keys() or user_entry.title() in data.keys():
        
                    print(" ".join(data[user_entry.title()]), end='\n\n') 
                    return restart()
            
            elif user_entry.upper() == data.keys() or user_entry.upper() in data.keys():
        
                    print(" ".join(data[user_entry.upper()]), end='\n\n') 
                    return restart()

            elif len(match_word) > 0:
                answer = input('%s not found. Maybe you mean %s? (y/n) ' 
                % (user_entry, match_word[0])) 
                print('')

                if answer == 'y'.lower():
                    print(" ".join(data[match_word[0]]), end='\n\n')
                    return restart()
                
                else:
                    print('Please enter a new word. or type \quit to end program.\n')
                    
            elif user_entry not in data.keys():
                print('%s not found. Please try another word. or type \quit to end program.\n' 
                % user_entry, end='\n\n')

            else:
                continue
            
            # ask user to search another word
            
                
               
    else:
        print('no file')


if __name__ == '__main__':
    print(dictionary())