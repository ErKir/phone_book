import argparse


def cli():
    desc = 'A simple console app that implements KRUD for phone book'

    parser = argparse.ArgumentParser(
        prog='Phone book',
        description=desc,
    )

    parser.add_argument('-o', '--operation', type=str, default='read',
                        help=("operations for phone book"
                              " (add, read, update: (*fields), find: (*fields))"
                              ),
                        )

    args = parser.parse_args()
    return args
