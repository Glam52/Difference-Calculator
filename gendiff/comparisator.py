def compare_dicts(dict1: dict, dict2: dict) -> list[dict]:
    """
    Compares two dictionaries using the same keys
    :param dict1: dict from first file
    :param dict2: dict from second file
    :return: list of dictionaries
    """
    compared_result = []  # The list to be filled with dictionaries
    # Selection of unique keys
    set_of_keys = set.union(set(dict1.keys()), set(dict2.keys()))
    # iterates each key, then sorts alphabetically
    for key in sorted(set_of_keys):
        # If the key is not in the second list, adds the type - deleted
        if key not in dict2:
            compared_result.append(
                {"key": key, "value": dict1[key], "type": "deleted"}
            )
        # If the key is not in the first list, adds the type - new
        elif key not in dict1:
            compared_result.append(
                {"key": key, "value": dict2[key], "type": "new"}
            )
        # If the key turns out to be nested, the type - nested is added
        # and the nested dictionary is checked using recursion
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            compared_result.append(
                {
                    "key": key,
                    "children": compare_dicts(dict1[key], dict2[key]),
                    "type": "nested",
                }
            )
        # If the key is in both dictionaries but their values are different,
        # both values are added and the type is modified
        elif dict1[key] != dict2[key]:
            compared_result.append(
                {
                    "key": key,
                    "value1": dict1[key],
                    "value2": dict2[key],
                    "type": "modified",
                }
            )
        # If both key and value match in two dictionaries,
        # the type is added - untouched
        else:
            compared_result.append(
                {"key": key, "value": dict1[key], "type": "untouched"}
            )

    return compared_result
