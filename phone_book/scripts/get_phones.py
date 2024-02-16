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


def write(data):
    with open(BOOK, 'w') as contacts:
        contacts.write(data)


def add_item(new_item):
    parsed_book = read()
    current_id = get_id(parsed_book)
    parsed_book[current_id] = new_item
    json_object = json.dumps(parsed_book, indent=4)
    write(json_object)
    return parsed_book


def find_item(required_unit) -> dict:
    parsed_book = read()
    query = list(
        filter(lambda item: item[1] is not None, required_unit.items()))
    filtered_book = parsed_book.items()
    for key, value in query:
        filtered_book = filter(
            lambda data: data[1][key] == value, filtered_book)
    return dict(filtered_book)


def read() -> str:
    with open(BOOK) as data:
        parsed_book = json.load(data)
        return parsed_book


def is_contact_exist(id_contact):
    parsed_book = read()
    return id_contact in parsed_book.keys()


def update(info: tuple) -> str:
    id_contact, data = info
    is_update = False
    parsed_book = read()
    updating_contact = parsed_book[id_contact]

    try:
        updating_contact.update(
            {"first_name": data['first_name']})
        updating_contact.update({"last_name": data['last_name']})
        updating_contact.update(
            {"patronymic": data['patronymic']})
        updating_contact.update(
            {"organization": data['organization']})
        updating_contact.update(
            {"work_telephone": data['work_telephone']})
        updating_contact.update(
            {"personal_telephone": data['personal_telephone']})

        is_update = True
        json_object = json.dumps(parsed_book, indent=4)
        write(json_object)
        return read()

    except ValueError:
        print("Format error. Please enter a correct data!.")

    if is_update is False:
        print("Data not found. Please enter a correct name\n")


def get_phones(query: str, opts={}) -> str:
    result = ''
    match query:
        case 'add':
            result = add_item(opts)
        case 'read':
            result = read()
        case 'find':
            result = find_item(opts)
        case 'update':
            result = update(opts)
        case _:
            return Exception
    return plain(result)
