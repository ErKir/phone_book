#!/usr/bin/env python3


from phone_book.cli import cli
from phone_book.scripts.get_phones import get_phones


def main():
    user_input = cli()
    print(get_phones(user_input.operation)
          )


if __name__ == '__main__':
    main()
