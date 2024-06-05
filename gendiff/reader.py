import json
import yaml


def get_data(file: str) -> dict:
    """
    Reads and load data from file and returns it as a dictionary
    :param file: .json or .yaml file
    :return: dictionary
    """

    # Processing .json files
    if file.endswith(".json"):
        with open(file, "r") as f:
            data = json.load(f)
    # Processing .yaml files
    elif file.endswith(".yaml") or file.endswith(".yml"):
        with open(file, "r") as f:
            data = yaml.safe_load(f)
    else:
        raise ValueError("Invalid file format")

    return data
