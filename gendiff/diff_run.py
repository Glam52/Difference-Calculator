from gendiff.reader import get_data
from gendiff.comparisator import compare_dicts
from gendiff.to_string import to_text


def gendiff(file1, file2):
# получение данных
    data1, data2 = get_data(file1, file2)
# сравнение данных
    compare_data = compare_dicts(data1, data2)
# вывод отсортированной строки
    text_final = to_text(compare_data)

    return text_final