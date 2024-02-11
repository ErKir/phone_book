import os
import json
from phone_book.scripts.formatter import plain

path_to_book = os.path.abspath('phone_book/phones/phones.json')


def add_item(phone_book, new_item):
    print(new_item)
    return phone_book


def get_phones(query: str, opts={}) -> str:
    with open(path_to_book) as data:
        parsed_book = json.load(data)
        match query:
            case 'add':
                return plain(add_item(parsed_book, opts))
            case 'read':
                return plain(parsed_book)

    return
