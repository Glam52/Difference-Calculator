from gendiff.diff_run import gendiff
import os


# test_yaml_gendiff()
# file3_json_path = os.path.join(
#     os.path.dirname(__file__), "fixtures", "file1.json"
# )
# file4_json_path = os.path.join(
#     os.path.dirname(__file__), "fixtures", "file2.json"
# )
# file_json_result_path = os.path.join(
#     os.path.dirname(__file__), "fixtures", "json_compare"
# )


def test_json():
    file1 = os.path.join(os.path.dirname(__file__), "fixtures", "file1.json")
    file2 = os.path.join(os.path.dirname(__file__), "fixtures", "file2.json")
    file_json_result_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "json_compare"
    )
    result = gendiff(file1, file2)

    with open(file_json_result_path) as file:
        expected_result = file.read()
    print(result)
    assert result == expected_result, "Файлы не совпадают"


test_json()
