def to_text(compared_result):
    text = "{\n"

    # Сортируем список словарей по ключам для упорядоченного вывода
    compared_result.sort(key=lambda x: x['key'])

    for item in compared_result:
        key = item['key']
        if item['type'] == 'untouched':
            text += f"    {key}: {item['value']}\n"
        elif item['type'] == 'modified':
            text += f"  - {key}: {item['value1']}\n"
            text += f"  + {key}: {item['value2']}\n"
        elif item['type'] == 'deleted':
            text += f"  - {key}: {item['value']}\n"
        elif item['type'] == 'new':
            text += f"  + {key}: {item['value']}\n"

    text += "}"
    return text