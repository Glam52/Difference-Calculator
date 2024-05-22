from gendiff.diff_run import gendiff
import os


def test_stylish_json():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")

    result = gendiff(file1, file2)

    return result


print(test_stylish_json())


def test_stylish_yaml():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.yaml")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.yaml")

    result = gendiff(file1, file2, "stylish")
    return result


print(test_stylish_yaml())


def test_plain():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")

    result = gendiff(file1, file2, "plain")
    return result


print(test_plain())


def test_json():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")

    result = gendiff(file1, file2, "json")

    return result


print(test_json())
