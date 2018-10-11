""" Example 2
Read json from string
"""

import json
from collections import namedtuple

JSON_STRING = """
	{
		"researcher": {
			"name": "Ford Prefect",
			"species": "Betelgeusian",
			"relatives": [{
					"name": "Zaphod Beeblebrox",
					"species"- "Betelgeusian"
			}
			]
		}
	}
"""
DATA = json.loads(
    JSON_STRING, object_hook=lambda d: namedtuple('x', d.keys())(*d.values()))

print DATA
print DATA.researcher
print DATA.researcher.name
print DATA.researcher.species
print DATA.researcher.relatives
print DATA.researcher.relatives[0]
print DATA.researcher.relatives[0].name
print DATA.researcher.relatives[0].species
