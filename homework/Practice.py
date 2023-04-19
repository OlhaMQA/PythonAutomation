class Cat:

    def make_noise(self):
        pass


class Tiger(Cat):

    def __init__(self):
        self.color = 'Stripes'
        self.paws = 4

    def make_noise(self):
        print('ROAR')


class Lynx(Cat):

    def __init__(self):
        self.color = 'Polka Dot'
        self.paws = 4

    def make_noise(self):
        print('Shhhh')


lynx = Lynx()
tiger = Tiger()
lynx.make_noise()
tiger.make_noise()
