#!/usr/bin/env python3


from cli import cli


def main():
    user_input = cli()
    print(get_phones(user_input.operation)
          )


if __name__ == '__main__':
    main()
