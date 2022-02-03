from itertools import groupby
from tokenize import group

people = [
    {"name": "Michael", "age": 19, "state": "NC"},
    {"name": "Andy", "age": 30, "state": "NC"},
    {"name": "Andy", "age": 26, "state": "NY"},
    {"name": "Justin", "age": 19, "state": "NC"},

]


def get_state(person):
    return person['state']


# list should be sorted with this key otherwise result will be unexpected (duplicates)
person_state_group = groupby(sorted(people, key=get_state), key=get_state)

for key, group in person_state_group:
    print(f'{key}: {list(group)}')
