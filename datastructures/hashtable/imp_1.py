from typing import Any


BLANK = object()


class HashTable:
    def __init__(self, capacity: int) -> None:
        self.values = [BLANK] * capacity

    def __len__(self) -> int:
        return len(self.values)

    def __setitem__(self, key: Any, value: Any) -> None:
        self.values[self.__index(key)] = value

    def __getitem__(self, key: Any) -> Any:
        value = self.values[self.__index(key)]

        if value is BLANK:
            raise KeyError(key)

        return value

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
            self[key] = BLANK

        else:
            raise KeyError()

    def __index(self, key: Any) -> int:
        return hash(key) % len(self)
