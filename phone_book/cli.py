import prompt
from phone_book.scripts.get_phones import get_phones


def add() -> dict:
    print('Enter:\n')
    first_name = prompt.string('First name: ', empty=False)
    last_name = prompt.string('Last name: ', empty=False)
    patronymic = prompt.string('Patronymic: ')
    organization = prompt.string('Organization: ')
    work_telephone = prompt.string('Work telephone: ')
    personal_telephone = prompt.string('Personal telephone: ', empty=False)
    result = {
        "first_name": first_name,
        "last_name": last_name,
        "patronymic": patronymic,
        "organization": organization,
        "work_telephone": work_telephone,
        "personal_telephone": personal_telephone,
    }
    return result


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
                print(get_phones(query, add()))
            case 'exit':
                return True
            case _:
                print('Invalid query!')
