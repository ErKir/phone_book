import argparse


def cli():
    desc = 'A simple console app that implements KRUD for phone book'

    parser = argparse.ArgumentParser(
        prog='Phone book',
        description=desc,
    )

    parser.add_argument('operation', type=str,
                        help=("operations for phone book"
                              " (add, read, update: (*fields), find: (*fields))"
                              ),
                        default='read')

    args = parser.parse_args()
    return args
