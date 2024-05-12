from gendiff.reader import get_data
from gendiff.comparisator import compare_dicts
from gendiff.stylish import stylish


def gendiff(file1, file2):
    # получение данных
    data1 = get_data(file1)
    data2 = get_data(file2)
    # сравнение данных
    compare_data = compare_dicts(data1, data2)
    # вывод отсортированной строки
    text_final = stylish(compare_data)

    return text_final
