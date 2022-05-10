class FrenchLocalizer:
    def __init__(self) -> None:
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette",
        }

    def localize(self, msg) -> str:
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg


if __name__ == "__main__":

    french = FrenchLocalizer()
    english = EnglishLocalizer()
    spanish = SpanishLocalizer()

    messages = ("car", "bike", "cycle")

    for msg in messages:
        print(french.localize(msg))
        print(english.localize(msg))
        print(spanish.localize(msg))
