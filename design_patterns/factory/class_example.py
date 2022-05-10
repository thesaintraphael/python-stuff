from before import EnglishLocalizer, FrenchLocalizer, SpanishLocalizer
from after import LOCALIZERS


class LocalizerFactory:
    def get_localizer(self, language="English"):
        return LOCALIZERS.get(language, "English")()


if __name__ == "__main__":

    french = LocalizerFactory.get_localizer("French")
    english = LocalizerFactory.get_localizer("English")
    spanish = LocalizerFactory.get_localizer("Spanish")

    messages = ("car", "bike", "cycle")

    for msg in messages:
        print(french.localize(msg))
        print(english.localize(msg))
        print(spanish.localize(msg))
