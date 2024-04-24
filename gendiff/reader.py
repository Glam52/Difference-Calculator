def get_data(file1, file2):
    data = {}

    if file1.endswith('.json'):
        data['file1'] = {'type': 'json'}

    if file2.endswith('.json'):
        data['file2'] = {'type': 'json'}
    pass