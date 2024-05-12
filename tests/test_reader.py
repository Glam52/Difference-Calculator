from gendiff.reader import get_data
import os


file1_json_path = os.path.join(
    os.path.dirname(__file__), "fixtures", "file3.json"
)
file2_json_path = os.path.join(
    os.path.dirname(__file__), "fixtures", "file4.json"
)


data1 = get_data(file1_json_path)
data2 = get_data(file2_json_path)

print("1 json-файл:", data1)
print("2 json-файл:", data2)

file1_yaml_path = os.path.join(
    os.path.dirname(__file__), "fixtures", "file1.yaml"
)
file2_yaml_path = os.path.join(
    os.path.dirname(__file__), "fixtures", "file2.yaml"
)

data1 = get_data(file1_yaml_path)
data2 = get_data(file2_yaml_path)

print("1 yaml-файл: ", data1)
print("2 yaml-файл: ", data2)
