from typing import Union


def format_value(value: Union[bool, None, str, dict], depth: int) -> str:
    """
    Auxiliary function, handles string output
    :param value: value to be formatted
    :param depth: indentation depth
    :return: new formatted value for text
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


def format_untouched_stylish(
    item, depth: int
) -> str:  # format for type - untouched
    key = item["key"]
    return f"{'    ' * depth}    {key}: {format_value(item['value'], depth)}"


def format_nested_stylish(item, depth: int) -> str:  # format for type - nested
    key = item["key"]
    return f"{'    ' * depth}    {key}: {stylish(item['children'], depth + 1)}"


def format_deleted_stylish(
    item, depth: int
) -> str:  # format for type - deleted
    key = item["key"]
    return f"{'    ' * depth}  - {key}: {format_value(item['value'], depth)}"


def format_new_stylish(item, depth: int) -> str:  # format for type - new
    key = item["key"]
    return f"{'    ' * depth}  + {key}: {format_value(item['value'], depth)}"


def format_modified_stylish(
    item, depth: int
) -> str:  # format for type - modified
    key = item["key"]
    return (
        f"{'    ' * depth}  - {key}: {format_value(item['value1'], depth)}\n"
        f"{'    ' * depth}  + {key}: {format_value(item['value2'], depth)}"
    )


def stylish(compared_result: list[dict], depth: int = 0) -> str:
    """
    The function takes the result of the comparison and
     returns the difference in the edited text
    :param compared_result: compared_result from comparisator.py
    :param depth: indentation depth
    :return: recursive comparison format
    """
    lines = ["{"]
    for item in compared_result:
        formatter = {
            "untouched": format_untouched_stylish,
            "nested": format_nested_stylish,
            "deleted": format_deleted_stylish,
            "new": format_new_stylish,
            "modified": format_modified_stylish,
        }.get(item["type"])
        if formatter:
            lines.append(formatter(item, depth))
    lines.append("    " * depth + "}")

    return "\n".join(lines)
