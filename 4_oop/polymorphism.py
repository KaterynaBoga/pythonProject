class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self, sound=''):
        print(sound)
        print('oyoyoyoy')

class Bear:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self, sound=''):
        print(sound)
        print('rrrrrrrrr')


wolf = Wolf('Grey', 5)
bear = Bear('Brown', 7)

for animal in (wolf, bear):
    animal.make_sound()

