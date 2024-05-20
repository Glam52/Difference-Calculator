from gendiff.diff_run import gendiff
import os


def test_json():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")

    result = gendiff(file1, file2)

    print(result)


test_json()
