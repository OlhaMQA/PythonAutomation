import random


class Rabbit:

    def __init__(self, gender):
        self.ears_length = random.randint(5, 20)
        self.gender = gender        # 0 or 1
        self.children = 0

    @staticmethod
    def rabbit_info():
        print('Gender: 0 refers to a "female", 1 refers to a "male". \n'
              'Ears length is random when creating Rabbit, but if make_new_rabbit method is used,\n'
              'then new child rabbit can only have the ears_length of his parents')

    def make_new_rabbit(self, obj):
        if self.gender != obj.gender:
            self.children += 1
            obj.children += 1
            child = Rabbit(random.randint(0, 1))
            child.ears_length = random.choice([self.ears_length, obj.ears_length])
            return child
        else:
            print('Same genders!')
            raise ValueError


Rabbit.rabbit_info()
rabbit_dad = Rabbit(1)
rabbit_mom = Rabbit(0)
rabbit_child = rabbit_mom.make_new_rabbit(rabbit_dad)
print(f'Here you can see a wonderful family of 3 rabbits. '
      f'Their total length of ears is '
      f'{rabbit_child.ears_length + rabbit_mom.ears_length + rabbit_dad.ears_length} centimeters!!!')


class Company:

    # Initialize the Company. Company has some open job positions and some workers on board.
    # Hire and fire workers using the methods of the Company class
    def __init__(self, name, open_positions):
        self.name = name
        self.workers = 0
        self.open_positions = open_positions
        self.hiring = True

    # Hire the worker. A new Worker class object is created
    def hire(self, job_title, name):
        self.workers += 1
        self.open_positions -= 1
        if self.open_positions > 0:
            self.hiring = True
        else:
            self.hiring = False
        return _Worker(job_title, name)

    # Fire the worker. Worker status becomes active = False
    def fire(self, worker):
        self.workers -= 1
        self.open_positions += 1
        worker.active = False
        self.hiring = True

    # Sometimes worker can become a private entrepreneur.
    # A classmethod allows to create a new Company using workers data
    # FOP has 1 worker - himself, no open positions and isn't hiring
    @classmethod
    def create_fop_from_worker(cls, worker):
        fop = cls(worker.name, 0)
        fop.workers = 1
        fop.hiring = False
        return fop


# A private class to create a worker. Worker can only be created by being hired by the Company
class _Worker:

    def __init__(self, job_title, name):
        self.active = True
        self.job_title = job_title,
        self.salary = 0
        self.name = name


apple = Company('Apple', 2)
aqa_engineer = apple.hire('AQA', 'Vasyl S.')

# Suddenly there was a layoff!
# Vasyl got fired from the company staff but was kindly proposed to work for the company as a FOP.
apple.fire(aqa_engineer)
vasyl_fop = Company.create_fop_from_worker(aqa_engineer)
print(vasyl_fop.name)
