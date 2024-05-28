def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif value == 0:
        return None


def plain(compared_result: list[dict], parent_key: str = "") -> str:
    result = ""
    for item in compared_result:
        key = item.get("key")
        full_key = f"{parent_key}.{key}" if parent_key else key

        if item.get("type") == "new":
            value = item.get("value")
            result += (
                f"Property '{full_key}'"
                f" was added with value: {format_value(value)}\n"
            )
        elif item.get("type") == "deleted":
            result += f"Property '{full_key}' was removed\n"
        elif item.get("type") == "modified":
            value1 = item.get("value1")
            value2 = item.get("value2")
            result += (
                f"Property '{full_key}'"
                f" was updated. From {format_value(value1)}"
                f" to {format_value(value2)}\n"
            )
        elif item.get("type") == "nested":
            result += plain(item.get("children"), full_key)

    return result
