from gendiff.diff_run import gendiff
import os


file1_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
file2_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')

result = gendiff(file1_path, file2_path)
print(result)