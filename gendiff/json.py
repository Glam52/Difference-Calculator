import json

def convert_to_json(compared_result: list[dict]) -> str:
    """
    Converts the compared result to JSON format
    :param compared_result: Compared result list of dictionaries
    :return: JSON string
    """
    # Convert the result to JSON string
    json_result = json.dumps(compared_result, indent=4)
    return json_result

