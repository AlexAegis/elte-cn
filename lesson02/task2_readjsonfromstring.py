import json
import marshal
from collections import namedtuple
# read json from string


class Researcher:
    name = ""
    species = ""
    relatives = []


json_string = """
        {
        "researcher": {
            "name": "Ford Prefect",
            "species": "Betelgeusian",
            "relatives": [
                {
                    "name": "Zaphod Beeblebrox",
                    "species": "Betelgeusian"
                }
            ]
        }
    }
"""
data = json.loads(json_string, object_hook=lambda d: namedtuple(
    'x', d.keys())(*d.values()))

print data
print data.researcher
print data.researcher.name
print data.researcher.species
print data.researcher.relatives
print data.researcher.relatives[0]
print data.researcher.relatives[0].name
print data.researcher.relatives[0].species
