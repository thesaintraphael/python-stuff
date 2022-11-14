from collections import defaultdict

def_dict = defaultdict(
    list
)  # Pass list (or any valid Python callable) to .default_factory
def_dict["one"] = 1
def_dict["missing"]  # Access a missing key returns an empty list
def_dict["another_missing"].append(4)  # Modify a missing key
def_dict["another_missing"].append(5)

print(def_dict)
