# config.py

import json

with open("config.json") as config_file:
    config_data = json.load(config_file)

OPENAI_API_KEY = config_data.get("OPENAI_API_KEY")