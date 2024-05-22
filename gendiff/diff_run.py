from gendiff.reader import get_data
from gendiff.comparisator import compare_dicts
from gendiff.formats.stylish import stylish
from gendiff.formats.json import convert_to_json
from gendiff.formats.plain import create_plain_text
from typing import IO


def gendiff(file1: IO, file2: IO, formatter='stylish') -> str:
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
    if formatter == 'stylish':
        text_final: str = stylish(compare_data)
    if formatter == 'json':
        text_final: str = convert_to_json(compare_data)
    if formatter == 'plain':
        text_final: str = create_plain_text(compare_data)

    return text_final
