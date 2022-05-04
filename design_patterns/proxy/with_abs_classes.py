from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """Interface method"""


class Person(IPerson):
    def person_method(self):
        print("I am a person")


class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am a proxy person method")
        self.person.person_method()


p1 = Person()
p1.person_method()


p2 = ProxyPerson()
p2.person_method()


# Proxy is a structural design pattern that lets you provide a substitute
# or placeholder for another object. A proxy controls access to the original object.
