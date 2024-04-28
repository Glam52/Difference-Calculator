import json


def get_data(file1, file2):
    data1 = {}
    data2 = {}

    if file1.endswith('.json'):
        with open(file1, 'r') as file1:
            data1 = json.load(file1)

    if file2.endswith('.json'):
        with open(file2, 'r') as file2:
            data2 = json.load(file2)

    else:
        return 'Invalid file format'

    return data1, data2
