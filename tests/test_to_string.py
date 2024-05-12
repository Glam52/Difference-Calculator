from gendiff.stylish import stylish
from gendiff.reader import get_data
from gendiff.comparisator import compare_dicts
import os


file1_path = os.path.join(os.path.dirname(__file__), "fixtures", "file3.json")
file2_path = os.path.join(os.path.dirname(__file__), "fixtures", "file4.json")
file_final = os.path.join(
    os.path.dirname(__file__), "fixtures", "json_compare_res_2"
)
# получение данных
data1 = get_data(file1_path)
data2 = get_data(file2_path)

# сравнение данных
compare_data = compare_dicts(data1, data2)

# осоритрованный вывод строки
text_final = stylish(compare_data)
with open('myfile', 'w') as file:
    file.write(text_final)
assert text_final == file_final
