class PartyAnimal:
    x = 0

    # constructor
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

"""
FootballFan includes everything in PartyAnimal plus what is in itself.
It is an extention of PartyAnimal.
FootballFan is a subclass of the class PartyAnimal.
"""
class FootballFan(PartyAnimal): 
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()
