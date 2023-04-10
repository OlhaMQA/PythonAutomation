class Cats:

    def __init__(self, name, age, breed, colour, character):
        self.gender = None
        self.name = name
        self.age = age
        self.breed = breed
        self.colour = colour
        self.character = character


    def is_adult(self):
        if self.age > 2:
            return True
        else:
            return False


    def gender(self):
        list_of_boys_names = ['Barsik', 'Cat2']
        if self.name in list_of_boys_names:
            self.gender = 'boy'
        else:
            self.gender = 'girl'


cat = Cats('Barsik', 1, 'no name', 'black', 'good boy')

print(cat.age)
print(cat.name)

cat_girl = Cats('Murka', 15, 'persian', 'red', 'bad')

print(cat.is_adult())
print(cat_girl.is_adult())

cat.gender()
print(cat.gender)
