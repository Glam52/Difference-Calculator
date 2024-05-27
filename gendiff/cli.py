import argparse
from gendiff.diff_run import gendiff


# def main():
#     parser = argparse.ArgumentParser(prog="gendiff")
#
#     parser.add_argument("first_file")
#     parser.add_argument("second_file")
#
#     parser.add_argument(
#         "-f", "--format", dest="format", help="set format of output"
#     )
#     parser.parse_args(["-h"])
#     parser.parse_args(["-f FORMAT"])
def main():
    parser = argparse.ArgumentParser(description='usage: gendiff [-h] first_file second_file')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('--format', choices=['stylish', 'json', 'plain'], default='stylish')
    args = parser.parse_args()

    result = gendiff(args.file1, args.file2, args.format)
    print(result)

if __name__ == "__main__":
    main()