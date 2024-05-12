import json
import yaml


def get_data(file):
    data = {}

    if file.endswith(".json"):
        with open(file, "r") as f:
            data = json.load(f)
    elif file.endswith(".yaml"):
        with open(file, "r") as f:
            data = yaml.safe_load(f)
    else:
        return "Invalid file format"

    return data
