def compare_dicts(dict1, dict2):
    compared_result = []

    # Проверяем ключи из первого словаря
    for key in dict1:
        if key in dict2:
            # Если значения одинаковы, добавляем их как untouched
            if dict1[key] == dict2[key]:
                compared_result.append({'key': key, 'value': dict1[key], 'type': 'untouched'})
            # Если значения различаются, добавляем их как modified
            else:
                compared_result.append({'key': key, 'value1': dict1[key], 'value2': dict2[key], 'type': 'modified'})
        else:
            # Если ключ есть только в первом словаре, добавляем его как deleted
            compared_result.append({'key': key, 'value': dict1[key], 'type': 'deleted'})

    # Проверяем ключи из второго словаря, чтобы найти новые ключи
    for key in dict2:
        if key not in dict1:
            # Если ключ есть только во втором словаре, добавляем его как new
            compared_result.append({'key': key, 'value': dict2[key], 'type': 'new'})

    return compared_result
