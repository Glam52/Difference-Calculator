from gendiff.reader import get_data
from gendiff.comparisator import compare_dicts
from gendiff.stylish import stylish
from typing import IO


def gendiff(file1: IO, file2: IO) -> str:
    """
    Compares 2 files and returns the edited
     text of the comparison of these files
    :param file1: .json or .yaml file
    :param file2: .json or .yaml file
    :return:
    """
    # Data from files is written to variables
    data1 = get_data(file1)
    data2 = get_data(file2)

    # Variable to which the result of the comparison is written
    compare_data = compare_dicts(data1, data2)

    # Variable into which the edited text is written
    text_final: str = stylish(compare_data)

    return text_final
