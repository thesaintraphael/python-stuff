import json
from dumps import personJSON


person = json.loads(personJSON)
print(person, type(person))  # dict


with open("json/person.json", "r") as file:
    person = json.load(file)
    print(person, "file")
