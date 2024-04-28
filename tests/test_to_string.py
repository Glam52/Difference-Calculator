from gendiff.to_string import to_text
from gendiff.reader import get_data
from gendiff.comparisator import compare_dicts

# получение данных
data1, data2 = get_data('file1.json', 'file2.json')

# сравнение данных
comp1 = compare_dicts(data1, data2)

# осоритрованный вовыод строки
text1 = to_text(comp1)

print(text1)
