import os
from gendiff.comparisator import compare_dicts
from gendiff.reader import get_data
from gendiff.formats.json import convert_to_json

file1_path = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
file2_path = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")

data1 = get_data(file1_path)
data2 = get_data(file2_path)
compare_data = compare_dicts(data1, data2)

final = convert_to_json(compare_data)

print(final)
