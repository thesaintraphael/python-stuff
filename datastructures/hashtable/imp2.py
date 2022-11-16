from typing import Any, NamedTuple


class Pair(NamedTuple):

    key: Any
    value: Any


class HashTable:
    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary) * 10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("Capacity must be a positive integer")
        self._slots = [None] * capacity

    def __len__(self) -> int:
        return len(self.pairs)

    def __setitem__(self, key: Any, value: Any) -> None:
        self._slots[self._index(key)] = Pair(key, value)

    def __getitem__(self, key: Any) -> Any:
        pair = self._slots[self._index(key)]

        if pair is None:
            raise KeyError(key)

        return pair.value

    def __contains__(self, key: Any) -> bool:
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key: Any) -> None:
        if key in self:
            self._slots[self._index(key)] = None

        else:
            raise KeyError()

    def __iter__(self):
        yield from self.keys

    def __str__(self):
        pairs = [f"{key!r}: {value!r}" for key, value in self.pairs]
        return "{" + ", ".join(pairs) + "}"

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    @property
    def pairs(self) -> list:
        return [pair for pair in self._slots if pair is not None]

    @property
    def values(self):
        return {pair.value for pair in self.pairs}

    @property
    def keys(self):
        return {pair.key for pair in self.pairs}

    @property
    def capacity(self) -> int:
        return len(self._slots)

    def _index(self, key: Any) -> int:
        return hash(key) % len(self._slots)

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), self.capacity)


if __name__ == "__main__":
    hash_map = HashTable(10)

    hash_map["a"] = 1
    hash_map["b"] = 2

    print(hash_map["a"])  # 1
    print(hash_map["b"])  # 2
    print(hash_map.get("c", "default"))  # default

    del hash_map["a"]
    print(hash_map.get("a", "deleted"))  # deleted

    print(len(hash_map))  # 10

    print("b" in hash_map)  # True
    print("a" in hash_map)  # False

    print(hash_map)  # {'b': 2}
