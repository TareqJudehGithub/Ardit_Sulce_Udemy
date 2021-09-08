import json
import os

# import json file


def dictionary():
    if os.path.exists('./files/data.json'):
        
        # load and read a json file
        data = json.load(open('./files/data.json'))

        while True:
            user_entry = input(' Enter something: ').lower()

            for k, v in data.items():
                if user_entry == k:
                    return "".join(v)
                else:
                    continue
    else:
        print('no file')


if __name__ == '__main__':
    print(dictionary())