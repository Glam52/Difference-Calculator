from typing import Union


def format_value(value: Union[dict, bool, str, None, int]) -> Union[str, int]:
    """
    Auxiliary function, handles string output
    :param value:value from dict to be formatted
    :return: new formatted value for text
    """
    # Return values by job condition
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif int(value) == 0:
        return 0

    return value


def plain(compared_result: list[dict], parent_key: str = "") -> str:
    """
    The function takes the result of the comparison and
     returns the difference in the edited text
    :param compared_result: compared_result from comparisator.py
    :param parent_key: need for full key length
    :return: flat format difference
    """
    result = []

    for i, item in enumerate(compared_result):
        # collect the full name of the key
        key = item.get("key")
        full_key = f"{parent_key}.{key}" if parent_key else key
        # format for type - new
        if item.get("type") == "new":
            value = item.get("value")
            result.append(
                f"Property '{full_key}'"
                f" was added with value: {format_value(value)}"
            )
        # format for type - deleted
        elif item.get("type") == "deleted":
            result.append(f"Property '{full_key}' was removed")
        # format for type - modified
        elif item.get("type") == "modified":
            value1 = item.get("value1")
            value2 = item.get("value2")
            result.append(
                f"Property '{full_key}'"
                f" was updated. From {format_value(value1)}"
                f" to {format_value(value2)}"
            )
        # format for type - nested, start recursion
        elif item.get("type") == "nested":
            result.append(plain(item.get("children"), full_key))

    return "\n".join(result)
