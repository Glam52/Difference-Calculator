from gendiff.to_string import to_text
from gendiff.reader import get_data
from gendiff.comparisator import compare_dicts
import os


file1_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
file2_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')

# получение данных
data1, data2 = get_data(file1_path, file2_path)

# сравнение данных
compare_data = compare_dicts(data1, data2)

# осоритрованный вывод строки
text_final = to_text(compare_data)

print(text_final)
