#tools
import json

def save_lycees_dict_in_json_file (lyccees):
    with open("lyccees.json", "w") as f:
        json.dump(lyccees, f, indent=4)