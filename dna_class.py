import random
lifespan = 300

class Dna():
    def __init__(self):
        self.dna = []
        
    def createDna(self):
        for v in range(lifespan):
            self.dna.append(PVector(random.uniform(-1,1), random.uniform(-1,1)))
    def returnDna(self):
        return self.dna
    def changeDna(self, dna):
        self.dna = dna
    def getGene(self, force):
        return self.dna[force]
    def getLength(self):
        return len(self.dna)
