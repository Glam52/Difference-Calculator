from gendiff.reader import get_data


print(get_data('file1.json', 'file2.json'))

data1, data2 = get_data('file1.json', 'file2.json')

print(data1)
print(data2)

print(type(data1))
print(type(data2))