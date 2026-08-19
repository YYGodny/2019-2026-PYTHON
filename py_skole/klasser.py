class dyr:
    def __init__(self, alder, species, name):
        self.alder = alder
        self.species = species
        self.name = name
    def spis(self):
        print(self.name, 'spiser')

class elefant(dyr):
    def __init__(self, alder, snabellengde, name):
        super().__init__(alder, 'elefant', name)
        self.snabellengde = snabellengde
    def snabel(self):
        print(self.name, 'bruker snabel')

e1 = elefant(29, '30', 'Jonh') 

class kontroller:
    def __init__(self):


    class batteri:
            def __init__(self):

        
