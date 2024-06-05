from gendiff.gendiff import generate_diff
import os
import pytest


@pytest.mark.parametrize(
    "file1, file2, expected_file, style",
    [
        ("file1.json", "file2.json", "result_stylish", "stylish"),
        ("file1.yaml", "file2.yaml", "result_yaml", "stylish"),
        ("file1.json", "file2.json", "result_plain", "plain"),
        ("file1.json", "file2.json", "result_json", "json"),
    ],
)
def test_generate_diff(file1, file2, expected_file, style):
    """
    Test function to compare the differences between two
    files based on a specified style.
    Args:
        file1 (str): Path to the first file for comparison.
        file2 (str): Path to the second file for comparison.
        expected_file (str): Path to the expected result file.
        style (str): Style of the difference output
        ('stylish', 'plain', or 'json').
    """
    file1_path = os.path.join(os.path.dirname(__file__), "fixtures", file1)
    file2_path = os.path.join(os.path.dirname(__file__), "fixtures", file2)
    expected_result = open(
        os.path.join(os.path.dirname(__file__), "fixtures", expected_file), "r"
    ).read()

    result = generate_diff(file1_path, file2_path, style)

    assert result == expected_result
