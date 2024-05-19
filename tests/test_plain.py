from gendiff.plain import create_plain_text
from gendiff.reader import get_data
from gendiff.comparisator import compare_dicts
import os


file1_path = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
file2_path = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")
file_final = os.path.join(os.path.dirname(__file__), "fixtures",
                          "plain_compare")

# получение данных
data1 = get_data(file1_path)
data2 = get_data(file2_path)

# сравнение данных
compare_data = compare_dicts(data1, data2)

text_final = create_plain_text(compare_data)

print(text_final)

assert text_final == file_final
