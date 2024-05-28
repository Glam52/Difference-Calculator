import json
import yaml


def get_data(file) -> dict:
    """
    Reads and load data from file and returns it as a dictionary
    :param file: .json or .yaml file
    :return: dictionary
    """

    data = "Incorrect data format"
    # Processing .json files
    if file.endswith(".json"):
        with open(file, "r") as f:
            data = json.load(f)
    # Processing .yaml files
    elif file.endswith(".yaml") or file.endswith(".yml"):
        with open(file, "r") as f:
            data = yaml.safe_load(f)

    return data
