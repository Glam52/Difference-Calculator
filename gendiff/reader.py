import json
import yaml


def get_data(file) -> dict or str:
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
    elif file.endswith(".yaml"):
        with open(file, "r") as f:
            data = yaml.safe_load(f)

    return data
