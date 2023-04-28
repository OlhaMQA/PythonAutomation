from datetime import datetime


class Station:

    def __init__(self, name):
        self.name = name
        self.passengers_in = []
        self.passengers_out = []

    def __str__(self):
        return f'{self.name}, in {self.passengers_in}, out {self.passengers_out}'

class Passenger:
    def __init__(self, name, destination: Station):
        self.name = name
        self.seat = None
        self.wagon = None
        self.destination = destination



class TrainCar:
    def __init__(self):
        self.__seats_limit: int = 10
        self.passengers = {seat: None for seat in range(1, self.__seats_limit + 1)}
        self.number = None


    @property
    def seats_available(self):
        number = [i for i in self.passengers if not self.passengers[i]]
        return number

    @property
    def seats_available_amount(self):
        seats_available = len(self.seats_available)
        return seats_available

    @property
    def first_seat_available(self) -> int | None:
        for i in self.passengers:
            if not self.passengers[i]:
                return i
        return None

    def __len__(self):
        return self.seats_occupied_amount

    def __str__(self):
        return f'Train car with {self.seats_occupied_amount} passengers on board'

    def __add__(self, passenger: Passenger):
        if self.seats_available_amount:
            seat_number = self.first_seat_available
            self.passengers[seat_number] = passenger
            passenger.seat = seat_number
            passenger.wagon = self.number
        return self

    def __sub__(self, passenger: Passenger):
        self.passengers[passenger.seat] = None
        passenger.seat = None
        passenger.wagon = None
        return self


class Train:

    def __init__(self):
        self.wagons = list()
        self.current_station = None

    def first_wagon_available(self) -> TrainCar | None:
        for i in self.wagons:
            if i.seats_available_amount:
                return i
        return None

    def move_to_station(self, station: Station):
        self.current_station = station
        return self.current_station

    def hop_on_train(self, passenger: Passenger):
        try:
            wagon = self.first_wagon_available()
            print(self.first_wagon_available())
            wagon = wagon + passenger
            self.current_station.passengers_in.append(passenger)
            return wagon
        except AttributeError:
            print('False')
            return False

    def hop_off_train(self, passenger: Passenger):
        try:
            self.current_station.passengers_out.append(passenger)
            wagon = passenger.wagon - passenger
            return wagon
        except:
            return False

    def __len__(self):
        return len(self.wagons)

    def __add__(self, wagon: TrainCar):
        self.wagons.append(wagon)
        wagon.number = self.wagons.index(wagon)
        return self

    def __radd__(self, wagon: TrainCar):
        self.wagons.append(wagon)
        wagon.is_in_train = True
        wagon.number = self.wagons.index(wagon)
        return self

    def __str__(self):
        return f'Train with {len(self.wagons)} wagons'


station = Station('Odesa')
passenger = Passenger('Test', station)

train = Train()
wagon_1 = TrainCar()
wagon_2 = TrainCar()
wagon_3 = TrainCar()

train = train + wagon_1
train = train + wagon_2
train = train + wagon_3
print(train)

train.hop_on_train(passenger)

print(wagon_1.passengers)

print(passenger)
print(station)

