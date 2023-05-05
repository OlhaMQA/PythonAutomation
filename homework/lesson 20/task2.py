from abc import ABC, abstractmethod


class DishFactory(ABC):          # Abstract dish factory

    @abstractmethod
    def cook_meal(self):
        pass


class PizzaFactory(DishFactory):        # Pizza Factory

    def cook_meal(self):            # Method returns Pizza object
        return Pizza()


class PastaFactory(DishFactory):        # Pasta factory

    def cook_meal(self):            # Method returns Pasta object
        return Pasta()


class RisottoFactory(DishFactory):      # Risotto factory

    def cook_meal(self):            # Method returns Risotto object
        return Risotto()


class Pizza:

    def __init__(self):
        self.name = 'Pizza Margherita'
        self.price = 10
        self.cooking_time = 7


class Pasta:

    def __init__(self):
        self.name = 'Pasta Bolognese'
        self.price = 15
        self.cooking_time = 10


class Risotto:

    def __init__(self):
        self.name = 'Risotto with mushrooms'
        self.price = 20
        self.cooking_time = 30


# Code to order a meal
class OrderPart:

    def italian_order(self):
        order = input('What is your order? ')
        if order == 'pizza':
            factory = PizzaFactory()
        elif order == 'pasta':
            factory = PastaFactory()
        elif order == 'risotto':
            factory = RisottoFactory()
        else:
            print('Out of menu')
            return self.italian_order()

        meal = factory.cook_meal()
        return meal


# Execute
order_part = OrderPart()
meal = order_part.italian_order()
print(meal.name)


