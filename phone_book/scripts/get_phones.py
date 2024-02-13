import os
import json
from phone_book.scripts.formatter import plain

BOOK = os.path.abspath('phone_book/phones/phones.json')


def get_id(phones) -> str:
    '''
    Функция получает телефонную книгу
    и возвращает id для нового абонента.
    '''
    keys = phones.keys()
    max_id = max(keys, key=lambda i: int(i))
    current_id = str(int(max_id) + 1)
    return current_id


def add_item(src, new_item):
    parsed_book = read(src)
    current_id = get_id(parsed_book)
    with open(src, 'w') as data:
        parsed_book[current_id] = new_item
        json_object = json.dumps(parsed_book, indent=4)
        data.write(json_object)
    return parsed_book


def find_item(src, required_unit) -> dict:
    parsed_book = read(src)
    query = list(
        filter(lambda item: item[1] is not None, required_unit.items()))
    filtered_book = parsed_book.items()
    for key, value in query:
        filtered_book = filter(
            lambda data: data[1][key] == value, filtered_book)
    return dict(filtered_book)


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
        case 'find':
            result = find_item(BOOK, opts)
        case _:
            return Exception
    return plain(result)
