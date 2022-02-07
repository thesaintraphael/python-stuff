import json
from json import JSONEncoder


class User:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


user = User("Max", 23)

# userJSON = json.dumps(user) TypeError: User object is not JSON erializable


def encode_user(obj: User) -> dict:
    return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}


userJSON = json.dumps(user, default=encode_user, indent=4)
print(userJSON)


# Custom Class

class UserEncoder(JSONEncoder):

    def default(self, o: User) -> dict:
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}


userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

userJSON = UserEncoder().encode(user)

user = json.loads(userJSON)  # dict
