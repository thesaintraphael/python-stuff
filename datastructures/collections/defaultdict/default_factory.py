"""Passing Arguments to .default_factory"""


from collections import defaultdict
from functools import partial


def factory(arg: str) -> str:
    return arg.upper()


# Using lambda
def_dict = defaultdict(lambda: factory("default"))
print(def_dict["missing"])


# Using partial
def_dict.default_factory = partial(factory, "2nd default")
print(def_dict["2nd_missing"])
