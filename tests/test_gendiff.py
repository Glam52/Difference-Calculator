from gendiff.diff_run import gendiff
import os


file1_json_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
file2_json_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
file_json_result_path = os.path.join(os.path.dirname(__file__),
                                'fixtures',
                                'json_compare_result'
                                )


def test_json_gendiff():
    result = gendiff(file1_json_path, file2_json_path)

    with open(file_json_result_path) as file:
        expected_result = file.read()

    print(result)
    #assert result == expected_result, 'Файлы не совпадают'

# Запуск теста
test_json_gendiff()


#Тестирование сравнения yaml файлов
file1_yaml_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yaml')
file2_yaml_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yaml')
file_yaml_result_path = os.path.join(os.path.dirname(__file__),
                                     'fixtures',
                                     'yml_compare_result'
                                     )
def test_yaml_gendiff():
    result = gendiff(file1_yaml_path, file2_yaml_path)

    with open(file_yaml_result_path) as file:
        expected_result = file.read()

    print(result)
    assert result == expected_result, 'Файлы не совпадают'


test_yaml_gendiff()

