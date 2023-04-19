from abc import ABC, abstractmethod


# Art Object has some name, author, century it was created, style.
# Since it is in the museum then it should definitely be shown (abstract method 'show')
# and seen (property 'seen')
# Art object has a price and an owner, but both these properties are internal
# we cannot change them so easily
class ArtObject(ABC):

    def __init__(self):
        self.name = None
        self.author = None
        self.century = None
        self.style = None
        self.seen = 0
        self._price = None   # Art is priceless by default
        self._owner = None

    @abstractmethod
    def show(self, people):
        # logic of showing
        pass

    # To check the price we can use a getter
    @property
    def price(self):
        if self._price:
            return self._price
        return 'Priceless!'

    # To set the price we can use a setter
    @price.setter
    def price(self, price):
        self._price = price


# Painting is definitely an Art Object. It inherits all its properties and methods.
# When new painting is introduced we can set the name, author and other properties.
# By Default its 'unknown'
# Painting can be shown as any art object
# It can also be sold. Besides Painting's price buyer should pay a luxury tax and an auction fee
# These calculations are hidden from the users
class Painting(ArtObject):

    def __init__(self, name='unknown', author='unknown', century='unknown', style='unknown'):
        super().__init__()
        self.name = name
        self.author = author
        self.century = century
        self.style = style

    def show(self, people):
        for i in range(people):
            print(f'I\'ve seen {self.name}!')
        self.seen += people

    def __calculate_luxury_tax(self):
        tax = self._price * 0.4
        return tax

    def __calculate_auction_fee(self):
        fee = self._price * 0.2
        return fee

    def sell(self, buyer):
        fee = self.__calculate_auction_fee()
        tax = self.__calculate_luxury_tax()
        price = self.price + tax + fee
        self._owner = buyer
        print(f'SOLD to {buyer} for EUR {price}')
        return price


# Sculpture is an Art Object too. It inherits all its properties and methods.
# When new Sculpture is introduced we can set the name, author and other properties.
# By Default its 'unknown'
# Sculpture can be shown as any art object, but 'showing' is different from the Painting
# Unlike Painting which can be spoiled by bright camera flashlight, Sculpture can be photographed
# It can also be broken. When a Sculpture is broken, a broken peace of it becomes a new Sculpture object
class Sculpture(ArtObject):

    def __init__(self, name='unknown', author='unknown', century='unknown', style='unknown'):
        super().__init__()
        self.name = name
        self.author = author
        self.century = century
        self.style = style
        self.photo = 0

    # Sculpture can be shown as well, but they are allowed to be photographed
    def show(self, people):
        for i in range(people):
            print(f'I\'ve seen {self.name}!')
            print(f'Photo of {self.name} taken')
        self.seen += people
        self.photo += people

    # Sculpture can be broken. But it only makes it more expensive as well as a broken piece of it
    def broke(self):
        part = Sculpture(name=f'Part of {self.name}', author=self.author, century=self.century, style='Broken piece')
        self.name = self.name + ' Broken'
        if self.price:
            self.price = self.price * 2
        return part


# Create a paining of Mona Lisa. Check and Set its price: now it costs 1000000.
# Show it 3 times and then sell to a Secret buyer for 1600000 (tax and fee included)
# OOP principles used: Abstraction, Encapsulation, Polymorphism, Inheritance.
# Also used hiding
mona_lisa = Painting(name='Mona Lisa', century='16th', author='Leonardo da Vinci', style='Renaissance')
print(mona_lisa.price)
mona_lisa.price = 1000000
print(mona_lisa.price)
mona_lisa.show(3)
mona_lisa.sell('Secret Buyer')

# Create a sculpture of David. Show it to 2 people and allow to take a selfie.
# Then David is broken (What a shame!). A part of it is separated and a new sculpture is created
# David is now broken which is represented in his new name.
# OOP principles used: Abstraction, Encapsulation, Polymorphism, Inheritance.
david = Sculpture(name='David', century='16th', author='Michelangelo', style='Renaissance')
david.show(2)
part_of_david = david.broke()               # Not that part :)
print(part_of_david.name)
print(david.name)
