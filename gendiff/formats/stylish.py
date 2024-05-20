def format_value(value, depth: int) -> str:
    """
    Auxiliary function, handles string output
    :param value: value to be formatted
    :param depth: indentation depth
    :return: formatted value
    """
    # depth depending on nesting
    if isinstance(value, dict):
        formatted = ["{"]
        for key, val in value.items():
            formatted.append(
                f"{'    ' * (depth + 2)}{key}: {format_value(val, depth + 1)}"
            )
        formatted.append(f"{'    ' * (depth + 1)}}}")
        return "\n".join(formatted)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return str(value)


def stylish(compared_result: list[dict], depth: int = 0) -> str:
    """
    The function takes the result of the comparison and
     returns the difference in the edited text
    :param compared_result: compared_result from comparisator.py
    :param depth: indentation depth
    :return: formatted difference
    """
    indent = "    " * depth
    lines = ["{"]
    for item in compared_result:
        key = item["key"]
        if item["type"] == "untouched":
            lines.append(
                f"{indent}    {key}: {format_value(item['value'], depth)}"
            )
        elif item["type"] == "nested":
            lines.append(
                f"{indent}    {key}: {stylish(item['children'], depth + 1)}"
            )
        elif item["type"] == "deleted":
            lines.append(
                f"{indent}  - {key}: {format_value(item['value'], depth)}"
            )
        elif item["type"] == "new":
            lines.append(
                f"{indent}  + {key}: {format_value(item['value'], depth)}"
            )
        elif item["type"] == "modified":
            lines.append(
                f"{indent}  - {key}: {format_value(item['value1'], depth)}"
            )
            lines.append(
                f"{indent}  + {key}: {format_value(item['value2'], depth)}"
            )
    lines.append(indent + "}")

    formatted_result: str = "\n".join(lines)

    return formatted_result
