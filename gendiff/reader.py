import json
import yaml

def get_data(file1, file2):
    data1 = {}
    data2 = {}

    if file1.endswith('.json'):
        with open(file1, 'r') as f:
            data1 = json.load(f)
    elif file1.endswith('.yaml'):
        with open(file1, 'r') as f:
            data1 = yaml.safe_load(f)

    if file2.endswith('.json'):
        with open(file2, 'r') as f:
            data2 = json.load(f)
    elif file2.endswith('.yaml'):
        with open(file2, 'r') as f:
            data2 = yaml.safe_load(f)

    else:
        return 'Invalid file format'

    return data1, data2

