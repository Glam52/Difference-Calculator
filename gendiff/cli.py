import argparse
from gendiff.gendiff import generate_diff


def gendiff_final():
    """
    Parses command line arguments to generate and display
    the difference between two files in the specified format.
    """
    # Help output, arguments and options
    parser = argparse.ArgumentParser(
        description="usage: gendiff [-h] first_file second_file"
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        choices=["stylish", "json", "plain"],
        default="stylish",
    )
    args = parser.parse_args()

    # collecting and run diff
    result = generate_diff(args.first_file, args.second_file, args.format)

    # Output of the finished solution
    print(result)


if __name__ == "__main__":
    gendiff_final()
