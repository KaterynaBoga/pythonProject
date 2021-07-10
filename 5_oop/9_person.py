class Person:
    __slots__ = ('name', 'age', 'country')

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


kat = Person('Kat', 37, 'Ukraine')
print(kat.__slots__)
kat.age = 38
print(kat.age)