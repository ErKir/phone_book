import os
import json
from phone_book.scripts.formatter import plain

BOOK = os.path.abspath('phone_book/phones/phones.json')


def get_id(phones) -> str:
    '''
    Функция получает id от каждого абонента
    телефонной книги и возвращает id
    для нового абонента.
    '''
    keys = phones.keys()
    max_id = max(keys, key=lambda i: int(i))
    current_id = str(int(max_id) + 1)
    return current_id


def add_item(src, new_item):
    parsed_book = read(src)
    current_id = get_id(parsed_book)
    with open(src, 'w') as data:
        print(new_item, current_id)
        parsed_book[current_id] = new_item
        json_object = json.dumps(parsed_book, indent=4)
        data.write(json_object)
    return parsed_book


def read(src) -> str:
    with open(src) as data:
        parsed_book = json.load(data)
        return parsed_book


def get_phones(query: str, opts={}) -> str:
    result = ''
    match query:
        case 'add':
            result = add_item(BOOK, opts)
        case 'read':
            result = read(BOOK)
        case _:
            return Exception
    return plain(result)
