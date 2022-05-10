from before import EnglishLocalizer, FrenchLocalizer, SpanishLocalizer


LOCALIZERS = {
    "French": FrenchLocalizer,
    "English": EnglishLocalizer,
    "Spanish": SpanishLocalizer,
}


def language_factory(language="English"):

    return LOCALIZERS[language]()


if __name__ == "__main__":

    french = language_factory("French")
    english = language_factory("English")
    spanish = language_factory("Spanish")

    messages = ("car", "bike", "cycle")

    for msg in messages:
        print(french.localize(msg))
        print(english.localize(msg))
        print(spanish.localize(msg))
