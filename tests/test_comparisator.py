from gendiff.comparisator import compare_dicts
from gendiff.reader import get_data


data1, data2 = get_data('file1.json', 'file2.json')

print(compare_dicts(data1, data2))