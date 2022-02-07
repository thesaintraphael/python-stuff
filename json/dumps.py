import json

person = {"name": "John", "surname": "Snow", "age": 28,
          "city": "Winterfell", "hasChildren": False}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# sort keys argument (bools) sorts key of JSON alphabetically

with open("json/person.json", "w") as file:
    json.dump(person, file, indent=4)  # dump, not dumps
