def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"


def create_plain_text(compared_result: list[dict], parent_key="") -> str:
    result = ""
    for item in compared_result:
        key = item.get("key")
        if parent_key:
            full_key = f"{parent_key}.{key}"
        else:
            full_key = key

        if item.get("type") == "new":
            value = item.get("value")
            if isinstance(value, dict) or isinstance(value, list):
                result += (f"Property '{full_key}' was added with value:"
                           f" {format_value(item['value'])}\n")
            else:
                result += (f"Property '{full_key}' was added with value:"
                           f" {format_value(item['value'])}\n")
        elif item.get("type") == "deleted":
            result += f"Property '{full_key}' was removed\n"
        elif item.get("type") == "modified":
            value1 = item.get("value1")
            value2 = item.get("value2")
            if isinstance(value1, dict) or isinstance(value2, dict):
                result += (f"Property '{full_key}' was updated. "
                           f"From {format_value(item['value1'])}"
                           f" to {format_value(item['value2'])}\n")
            else:
                result += (f"Property '{full_key}' was updated. "
                           f"From {format_value(item['value1'])}"
                           f" to {format_value(item['value2'])}\n")
        elif item.get("type") == "nested":
            result += create_plain_text(item.get("children"), full_key)

    return result
