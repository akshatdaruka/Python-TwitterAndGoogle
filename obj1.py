class PartyAnimal:
    x=0
    def __init__(self):
        print("i am constructed")
    def party(self):
        self.x=self.x+1
        print("so far",self.x)
    def __del__(self):
        print("i am destructed",self.x)
an=PartyAnimal()
an.party()
an.party()
an=77
print("an contains",an)
an=PartyAnimal()
an=99
