from gendiff.gendiff import diff_run
import os


def test_stylish_json():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")
    final_file = open(
        os.path.join(os.path.dirname(__file__), "fixtures", "result_stylish"),
        "r",
    ).read()

    result = diff_run(file1, file2)
    with open("test_st", "w") as file:
        file.write(result)
    assert result == final_file


def test_stylish_yaml():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.yaml")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.yaml")
    final_file = open(
        os.path.join(os.path.dirname(__file__), "fixtures", "result_yaml"), "r"
    ).read()

    result = diff_run(file1, file2, "stylish")
    with open("test_st", "w") as file:
        file.write(result)
    assert result == final_file


def test_plain():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")
    final_file = open(
        os.path.join(os.path.dirname(__file__), "fixtures", "result_plain"), "r"
    ).read()
    result = diff_run(file1, file2, "plain")
    with open("test_st", "w") as file:
        file.write(result)
    assert result == final_file


def test_json():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")
    final_file = open(
        os.path.join(os.path.dirname(__file__), "fixtures", "result_json"), "r"
    ).read()
    result = diff_run(file1, file2, "json")
    with open("test_st", "w") as file:
        file.write(result)
    assert result == final_file
