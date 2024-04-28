from gendiff.reader import get_data
import os


file1_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
file2_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')


data1, data2 = get_data(file1_path, file2_path)

print(data1)
print(data2)

print(type(data1))
print(type(data2))
