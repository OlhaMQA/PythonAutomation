class People:

    def __init__(self, name, height, mass, hair_color, skin_color):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
