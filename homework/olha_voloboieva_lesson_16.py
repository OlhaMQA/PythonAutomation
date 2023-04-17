from abc import ABC, abstractmethod


# abstract class for Transport
class Transport(ABC):

    def __init__(self):
        self.wheels = None
        self.path = None
        self.passengers = 0
        self.moving = None

    # Abstract method to move
    @abstractmethod
    def move(self):
        self.moving = True

    # Non-abstract method to stop
    def stop(self):
        print(f'Stopped')
        self.moving = False

    # Abstract method to add passengers to the car
    @abstractmethod
    def pick_up_passenger(self, number):
        # some logic to add passengers
        pass


class Car(Transport):

    def __init__(self):
        super().__init__()
        self.wheels = 4
        self.path = 'Road'
        self.passengers_limit = 4
        self.brand = None

    # New method for class Car
    def horn(self):
        print('Bee-Bee')

    # Rewritten abstract method
    def move(self):
        self.moving = True

    # Rewritten abstract method
    def pick_up_passenger(self, number):
        self.passengers += number
        if self.passengers > self.passengers_limit:
            return 'Full'
        return 'Welcome'


# Grand-child class
class Ferrari(Car):

    def __init__(self):
        super().__init__()
        self.brand = 'Ferrari'

    # Rewritten from parent class
    def move(self):
        print(f'I\'m driving FAST by the {self.path}')
        self.moving = True


# Test grandchild class object
my_car = Ferrari()
my_car.move()  # Method rewritten in the child class
my_car.stop()  # Method from grandparent class
my_car.horn()  # Method from parent class







