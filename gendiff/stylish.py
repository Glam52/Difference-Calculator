def format_value(value, depth):
    if isinstance(value, dict):
        formatted = ['{']
        for key, val in value.items():
            formatted.append(f"{'    ' * (depth + 2)}{key}: {format_value(val, depth + 1)}")
        formatted.append(f"{'    ' * (depth + 1)}}}")
        return '\n'.join(formatted)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)

def stylish(compared_result, depth=0):
    indent = '    ' * depth
    lines = ['{']
    for item in compared_result:
        key = item['key']
        if item['type'] == 'untouched':
            lines.append(f"{indent}    {key}: {format_value(item['value'], depth)}")
        elif item['type'] == 'nested':
            lines.append(f"{indent}    {key}: {stylish(item['children'], depth + 1)}")
        elif item['type'] == 'deleted':
            lines.append(f"{indent}  - {key}: {format_value(item['value'], depth)}")
        elif item['type'] == 'new':
            lines.append(f"{indent}  + {key}: {format_value(item['value'], depth)}")
        elif item['type'] == 'modified':
            lines.append(f"{indent}  - {key}: {format_value(item['value1'], depth)}")
            lines.append(f"{indent}  + {key}: {format_value(item['value2'], depth)}")
    lines.append(indent + '}')

    formatted_result = '\n'.join(lines)

    return formatted_result
