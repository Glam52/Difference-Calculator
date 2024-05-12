def compare_dicts(dict1, dict2):
    compared_result = []
    set_of_keys = set.union(set(dict1.keys()), set(dict2.keys()))
    for key in sorted(set_of_keys):
        if key not in dict2:
            compared_result.append(
                {"key": key, "value": dict1[key], "type": "deleted"}
            )
        elif key not in dict1:
            compared_result.append(
                {"key": key, "value": dict2[key], "type": "new"}
            )
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            compared_result.append(
                {
                    "key": key,
                    "children": compare_dicts(dict1[key], dict2[key]),
                    "type": "nested",
                }
            )
        elif dict1[key] != dict2[key]:
            compared_result.append(
                {
                    "key": key,
                    "value1": dict1[key],
                    "value2": dict2[key],
                    "type": "modified",
                }
            )
        else:
            compared_result.append(
                {"key": key, "value": dict1[key], "type": "untouched"}
            )

    return compared_result
