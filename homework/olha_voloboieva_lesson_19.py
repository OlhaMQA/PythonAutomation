from random import choice


class Station:      # Class Station with a name and some people on it

    def __init__(self, name: str):
        self.name = name
        self.people_waiting = []


class Passenger:        # Class Passenger with a name, wagon, seat, station in and out
    def __init__(self, name: str, station_initial: str, station_destination: str):
        self.name = name
        self.current_station = station_initial
        self.destination = station_destination
        self.seat = None
        self.wagon = None

    def __str__(self):
        return f"'name': '{self.name}', 'wagon': '{self.wagon}, " \
               f"'seat': {self.seat}, destination: {self.destination}"


class Wagon:     # Class Wagon with a dictionary with seats and people seating, seats limit is 10.

    def __init__(self):
        self.seats_limit: int = 10
        self.seat_passenger: dict = {seat: None for seat in range(1, self.seats_limit + 1)}
        self.number: int = 0    # Number is 0 until is in train

    def __len__(self):
        occupied = [seat for seat in self.seat_passenger if self.seat_passenger[seat]]
        return len(occupied)

    def __str__(self):
        return str(self.number)

    @property
    def seats_available(self) -> list:      # Seats without passengers
        seats = []
        for seat in self.seat_passenger:
            if not self.seat_passenger[seat]:
                seats.append(seat)
        return seats

    def __add__(self, new_passenger: Passenger):        # Way to add passengers to the wagon
        seat = self.seats_available[0]
        self.seat_passenger[seat] = new_passenger
        new_passenger.wagon = self
        new_passenger.seat = seat
        return self


class Train:            # Class Train has wagons and location

    def __init__(self, train_station):
        self.wagons = list()
        self.current_station = train_station

    def __len__(self):
        return len(self.wagons)

    def __add__(self, other):       # Way to add wagons or passengers
        if isinstance(other, Wagon):
            self.wagons.append(other)
            other.number = self.wagons.index(other) + 1
        elif isinstance(other, Passenger):
            if self.wagons_available():
                self.wagons_available()[0] + other
        return self

    def __sub__(self, passenger_leaving_train: Passenger):      # Way to subtract passengers
        passenger_leaving_train.wagon.seat_passenger[passenger_leaving_train.seat] = None
        passenger_leaving_train.seat = None
        passenger_leaving_train.wagon = None
        return self

    def __str__(self):
        return f'Train with {len(self.wagons)} wagons and {len(self.passengers_in_train())} passengers onboard'

    def passengers_in_train(self):      # Who is in the train
        passengers_in_train = []
        for wagon in self.wagons:
            for passenger in wagon.seat_passenger.values():
                if passenger:
                    passengers_in_train.append(passenger)
        return passengers_in_train

    def wagons_available(self):     # Which wagons have seats available
        wagons = [wagon for wagon in self.wagons if wagon.seats_available]
        return wagons

    def move_to_station(self, station: Station):     # Move to stations
        print(f'We are in {station.name}')
        print(f'Some people are leaving the train:')    # Let people out
        for passenger in self.passengers_in_train():
            if passenger.destination == station.name:
                self - passenger
                print(passenger)

        print(f'Some people are getting on the train:')
        for passenger in station.people_waiting:     # Let people in
            if not self.wagons_available():
                new_wagon = Wagon()
                self + new_wagon     # Add new wagon if needed
                print(f'New wagon added! Number: {new_wagon.number}')
            self + passenger
            print(passenger)

        self.current_station = station       # update train station
        station.people_waiting.clear()      # clear the station waiting room
        return None

################ TEST ###################
# Let the journey begin!
# Create 2 stations: London and Paris. Train will move between 2 of them
london = Station('London')
paris = Station('Paris')

# Create a train, his starting station is london
train = Train(london)

# Create a first wagon. It's a luxury wagon with 10 seats only by default
# Then add wagon to a train
wagon_1 = Wagon()
train = train + wagon_1

# Let's create passengers. There are many - 45 passengers at least!
passengers = []

for i in range(45):
    current_station = choice([london.name, paris.name])
    destination = 'London' if current_station == 'Paris' else 'Paris'
    passenger = Passenger(f'Passenger {i}', current_station, destination)
    passengers.append(passenger)


# Passengers have to wait for the train on the stations, let's see who is where:
for i in passengers:
    if i.current_station == 'London':
        london.people_waiting.append(i)
    elif i.current_station == 'Paris':
        paris.people_waiting.append(i)


print("Let's check our train")
print(train)
print(len(train))
print()
print()
print("Let's start in London")
print('Nobody is leaving, it is only a starting point. people are taking seats.'
      ' New wagons are added when there is no seats left' )
train.move_to_station(london)
print()
print()
print("Let's go to Paris")
train.move_to_station(paris)
print()
print()
print("Let's go back to London")
train.move_to_station(london)

print('All passengers were delivered to their destination')
print(f'{len(train)} wagons were enough')
print("Let's make sure there there is nobody left" )
print(len(train.wagons[0]))
