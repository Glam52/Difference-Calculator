from gendiff.comparisator import compare_dicts
from gendiff.reader import get_data
import os

file1_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file3.json')
file2_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file4.json')

data1, data2 = get_data(file1_path, file2_path)

print(compare_dicts(data1, data2))
