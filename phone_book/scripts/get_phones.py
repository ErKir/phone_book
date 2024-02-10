import json

path_to_book = '/home/kirill/test_tasks/phone_book/phone_book/phones/phones.json'


def get_phones(ops):
    with open(path_to_book) as data:
        parsed_book = json.load(data)
    return parsed_book
