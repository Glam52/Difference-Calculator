from gendiff.formats.stylish import stylish
from gendiff.reader import get_data
from gendiff.comparisator import compare_dicts
import os


file1_path = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
file2_path = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")
file_final = os.path.join(os.path.dirname(__file__), "fixtures", "result_stylish")
# получение данных
data1 = get_data(file1_path)
data2 = get_data(file2_path)

# сравнение данных
compare_data = compare_dicts(data1, data2)

# осоритрованный вывод строки
text_final = stylish(compare_data)

print(text_final)
