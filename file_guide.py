'''
The module helps the user go through .json file.
'''
import json
from pprint import pprint


def read_file(path):
    '''
    The function reads .json file.
    '''

    json_f = open(path, encoding='utf-8')
    encoded = json.load(json_f)

    return encoded


def open_dobject(obj: dict):
    '''
    The function opens returns insight of a dictionary object.
    '''
    choise = '|'
    for key in obj:
        choise += ' ' + str(key) + ' |'

    message = f'\nChoose among the following keys:\n\n{choise}\n\n'
    user_choise = input(message)

    while user_choise not in choise or user_choise != 'all':

        if user_choise == 'all':
            pprint(obj)
            return True

        if user_choise in obj.keys():
            return obj[user_choise]

        message = f'\nChoose among the following keys:\n\n{choise}\n\n'
        user_choise = input(message)


def open_lobject(obj: list):
    '''
    The function opens returns insight of a list object.
    '''
    choise = '|'
    for _ in range(len(obj)):
        choise += ' ' + str(_) + ' |'

    message = f'\nChoose among the following elements:\n\n{choise}\n\n'
    user_choise = input(message)

    while user_choise not in choise or user_choise != 'all':

        if user_choise == 'all':
            pprint(obj)
            return True

        if user_choise in choise:
            return obj[int(user_choise)]

        message = f'\nChoose among the following elements:\n\n{choise}\n\n'
        user_choise = input(message)


def detect_object(data):
    '''
    The function detects, whether an object is a dictionary or a list. In case
    the object is none of those types, returns all the data.
    '''
    if isinstance(data, dict):
        result = open_dobject(data)
        return detect_object(result)

    if isinstance(data, list):
        result = open_lobject(data)
        return detect_object(result)

    pprint(data)
    return True


def main():
    '''
    Main module.
    '''
    start_message = '\nPlease, enter a path to the file: '
    way_to_file = input(start_message)

    try:
        js_file = read_file(way_to_file)
    except FileNotFoundError:
        main()

    result = detect_object(js_file)

    if result:

        next_choise = input('\nType "yes" to start over again: ')

        if next_choise == 'yes':
            main()

    return '\nciao!'


if __name__ == "__main__":
    print(main())
