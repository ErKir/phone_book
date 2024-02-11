import prompt
from phone_book.scripts.get_phones import get_phones


def cli():
    query = prompt.string(
        'Please enter a query for phone book\n'
        'Can be: read, to see the phone book;\n'
        '        add, to add a new number;\n'
        '        find, to search for a number;\n'
        '        update, to change an existing one;\n'
    )
    match query:
        case 'read':
            print(get_phones(query))
        case _:
            print('Invalid query!')
    return


"""
на промптах из первого проекта можно дописать логику круда
поочередно спрашивать фио и тел, и складывать в словарь,
словарь передавать в джейс
"""
