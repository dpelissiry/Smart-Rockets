import random
from dna_class import Dna
width = 800
goal = PVector(width/2, 50)
fitness_values = {}

class Rocket():
    
    def __init__(self):
        self.pos = PVector(width/2, height-20)
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        self.dna = Dna()
        self.crashed = False
        self.dna.createDna()
        
        self.fitness = 0
    def display(self):
        push()
        noStroke()
        translate(self.pos.x, self.pos.y)
        rotate(self.vel.heading())
        rectMode(CENTER)
        fill (255,255,255, 150)
        rect(0, 0, 30, 5)
        pop()
        
    def move(self):
        
        #deletes the velocity if crashed
        if not self.crashed:
            self.pos.add(self.vel)
            self.vel.add(self.acc)
        self.acc.mult(0)
    def applyForce(self, force):
        self.acc.add(self.dna.getGene(force))
    
    def eval(self):
        global fitness_values
        self.fitness = self.pos.dist(goal)
        fitness_values[self] = self.fitness
        
    def getFitness(self):
        return self.fitness
    
    def loadDna(self, dna):
        self.dna.changeDna(dna)
    
    def getDna(self):
        return self.dna.returnDna()
    def collisionBarrier(self, barrier):
        barrierprops = barrier.return_property()
        if self.pos.x > barrierprops[0] and self.pos.x < barrierprops[0] + barrierprops[2]:
            if self.pos.y > barrierprops[1] and self.pos.y < barrierprops[1]+barrierprops[3]:
                self.crashed = True
                if barrierprops[1] < 100:
                    print(self.dna.returnDna())
    def collisionWall(self):
        if self.pos.x < 0 or self.pos.x > width or self.pos.y < 0 or self.pos.y > height:
            self.crashed = True
        
    
class Barrier():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def show(self):
        fill(0, 0, 200)
        
        rect(self.x, self.y, self.w, self.h)
    def return_property(self):
        return [self.x, self.y, self.w, self.h]
    
    
        
        
        
    
