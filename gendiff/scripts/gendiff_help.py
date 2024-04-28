import argparse


def main():
    parser = argparse.ArgumentParser(prog='gendiff')

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format',
                        dest='format',
                        help='set format of output'
                        )
    parser.parse_args(['-h'])
    parser.parse_args(['-f FORMAT'])


if __name__ == '__main__':
    main()
