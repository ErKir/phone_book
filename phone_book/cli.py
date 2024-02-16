import prompt
from phone_book.scripts.get_phones import get_phones, is_contact_exist


def query_builder(input_opt=True) -> dict:
    print('Enter:\n')
    first_name = prompt.string('First name: ', empty=input_opt)
    last_name = prompt.string('Last name: ', empty=input_opt)
    patronymic = prompt.string('Patronymic: ', empty=True)
    organization = prompt.string('Organization: ', empty=True)
    work_telephone = prompt.string('Work telephone: ', empty=True)
    personal_telephone = prompt.string('Personal telephone: ', empty=input_opt)
    result = {
        "first_name": first_name,
        "last_name": last_name,
        "patronymic": patronymic,
        "organization": organization,
        "work_telephone": work_telephone,
        "personal_telephone": personal_telephone,
    }
    return result


def get_update_data():
    id_contact = prompt.string('Enter contact id (No) you want to update: ')
    if is_contact_exist(id_contact):
        return query_builder()
    else:
        print('Data not found. Please enter a correct id (No)\n')


def cli():
    while True:
        query = prompt.string('\n'
                              'Please enter a query for phone book\n'
                              'Can be: read, to see the phone book;\n'
                              '        add, to add a new number;\n'
                              '        find, to search for a number;\n'
                              '        update, to change an existing one;\n'
                              '        exit, to leave phone book;\n'
                              )
        match query:
            case 'read':
                print(get_phones(query))
            case 'add':
                print(get_phones(query, query_builder(False)))
            case 'find':
                print(get_phones(query, query_builder(True)))
            case 'update':
                print(get_phones('read'))
                print(get_phones(query, get_update_data()))
            case 'exit':
                return True
            case _:
                print('Invalid query!')
