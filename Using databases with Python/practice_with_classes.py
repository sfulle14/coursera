class PartyAnimal:
    x = 0

    # constructor
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

    # destructor
    # def __del__(self):
    #     print('I am destructed', self.x)

# an = PartyAnimal()  #redefines call statement

# an.party()  #classes function in PartyAnimal
# an.party()
# an.party()
# an = 42
# print('an contains', an)

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()

# print(type(an))
# print(dir(an))