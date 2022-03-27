from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class Capital(Position):
    country: str = "Unknown"
    # will be crashed if you don't set default value for country, because order for __init__ is will be as following:
    #  __init__(self, name, lon=0.0, lat=0.0, country) Non default arguments must be specified before default arguments.


def main():
    capital = Capital("Moscow", lon=37.6, lat=55.7, country="Russia")
    print(capital)


if __name__ == "__main__":
    main()
