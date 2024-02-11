import os
import json
from phone_book.scripts.formatter import plain

path_to_book = os.path.abspath('phone_book/phones/phones.json')


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


def add_item(phone_book, new_item):
    current_id = get_id(phone_book)
    print(new_item, current_id)
    phone_book[current_id] = new_item
    json_object = json.dumps(phone_book, indent=4)
    return json_object


def get_phones(query: str, opts={}) -> str:
    with open(path_to_book) as data:
        parsed_book = json.load(data)
        match query:
            case 'add':
                new_data = add_item(parsed_book, opts)
                data.write(new_data)
                return plain(new_data)
            case 'read':
                return plain(parsed_book)

    return parsed_book
