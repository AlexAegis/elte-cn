import json

# read json from string

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
data = json.loads(json_string)
for rel in data["researcher"]["relatives"]:
    print('Name: %s (%s)' % (rel["name"], rel["species"]))
