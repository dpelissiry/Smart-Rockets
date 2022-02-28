#import matplotlib
from rocket_class import Rocket, Barrier, fitness_values
import random


rockets = []
barriers = []

lifespan = 300
population = 200
life_count = 0
generation = 0

def setup():
    global rocket
    global vectors
    global barriers
    size(800, 800)
    #fig = plt.figure()
    #axe = fig.add_axes([0,0,1,1])
    
    for i in range(population):
        rockets.append(Rocket())
    
    #for i in range(50):
        
        #barriers.append(Barrier(random.randint(0, width), random.randint(0,height),40, 40))
    
    barriers.append(Barrier(width/4+100, height/3*2,width/4*3, 50))
    barriers.append(Barrier(0, height/3,width/4*3-100, 50))
    goal_box = Barrier((width/2)-10,40,20,20)
    barriers.append(goal_box)
    display_data()
        

def select():
    global rockets
    global fitness_values_list
    global fitness_values

    key_list = fitness_values.keys()
    fitness_values_list = fitness_values.values()
    fitness_values_list_sorted = sorted(fitness_values_list, reverse = True)

    fitness_values_list_weighted = []

    #creates weighted list of fitnesses
    for i in range(0, len(fitness_values_list_sorted)):
        for j in range(0, i**2):
            fitness_values_list_weighted.append(fitness_values_list_sorted[i])
    

    selected = []
    #selects the chosen population for crossover

    for i in range(0, population):
        selected.append(random.choice(fitness_values_list_weighted))

    #takes the list of fitnesses and turns into list of class instances
    for count, select in enumerate(selected):
        selected[count] = key_list[fitness_values_list.index(select)]

    #mates and initialize rockets list to zero to add the new rockets to it
    rockets = []
    
    for i in range(0, len(selected)/2):
        mom = random.choice(selected)
        selected.remove(mom)
        dad = random.choice(selected)
        selected.remove(dad)
        #print(dad.getDna())
        crossover(mom, dad)
    #print(selected)

def crossover(mom, dad):
    crossover_point = random.randint(0,lifespan)
    first_parent = random.randint(1,2)
    if first_parent == 1:
        mom_dna_spliced = mom.getDna()[:crossover_point]
        dad_dna_spliced = dad.getDna()[crossover_point:]
        child_one_dna = mom_dna_spliced+dad_dna_spliced
        #mutation within first child dna
        if crossover_point < 10:
            rand_indexes = []
            for i in range(crossover_point):
                rand_indexes.append(random.randint(0,lifespan-1))
            
            for i in rand_indexes:
                
                child_one_dna[i] = PVector(random.uniform(-1,1), random.uniform(-1,1))
        rocket = Rocket()
        rocket.loadDna(child_one_dna)
        rockets.append(rocket)
        crossover_point_two = random.randint(0,lifespan)
        first_parent = random.randint(1,2)
        if first_parent == 1:
            mom_dna_spliced = mom.getDna()[:crossover_point]
            dad_dna_spliced = dad.getDna()[crossover_point:]
            child_two_dna = mom_dna_spliced+dad_dna_spliced
            rocket2 = Rocket()
            rocket2.loadDna(child_two_dna)
            rockets.append(rocket2)
        else:
            mom_dna_spliced = mom.getDna()[crossover_point:]
            dad_dna_spliced = dad.getDna()[:crossover_point]
            child_two_dna = dad_dna_spliced+mom_dna_spliced
            rocket2 = Rocket()
            rocket2.loadDna(child_two_dna)
            rockets.append(rocket2)
    else:
        
        mom_dna_spliced = mom.getDna()[crossover_point:]
        dad_dna_spliced = dad.getDna()[:crossover_point]
        child_one_dna = dad_dna_spliced+mom_dna_spliced
        #mutation within first child dna
        if crossover_point < 10:
            rand_indexes = []
            for i in range(crossover_point):
                rand_indexes.append(random.randint(0,lifespan-1))
            for i in rand_indexes:
                
                print(len(child_one_dna), rand_indexes)
                child_one_dna[i] = PVector(random.uniform(-1,1), random.uniform(-1,1))
        rocket = Rocket()
        rocket.loadDna(child_one_dna)
        rockets.append(rocket)
        crossover_point_two = random.randint(0,lifespan)
        first_parent = random.randint(1,2)
        if first_parent == 1:
            mom_dna_spliced = mom.getDna()[:crossover_point]
            dad_dna_spliced = dad.getDna()[crossover_point:]
            child_two_dna = mom_dna_spliced+dad_dna_spliced
            rocket2 = Rocket()
            rocket2.loadDna(child_two_dna)
            rockets.append(rocket2)
        else:
            mom_dna_spliced = mom.getDna()[crossover_point:]
            dad_dna_spliced = dad.getDna()[:crossover_point]
            child_two_dna = dad_dna_spliced+mom_dna_spliced
            rocket2 = Rocket()
            rocket2.loadDna(child_two_dna)
            rockets.append(rocket2)
    
def display_data():
    textSize(24)
    fill(255)
    text("Generation: %s" % generation, 10, 50)
    text(life_count, 10, 150)
    if generation > 0:
        fitness_total = sum(fitness_values_list)
        #print(fitness_total, len(fitness_values_list))
        text("Avg Fitness: %s" % (int(fitness_total)/int(len(fitness_values_list))), 10, 100)

    #USE FOR AVERAGE FOR GRAPH
    '''
    for i in range(0,len(fitness_values)):
        fitness_values[i] = fitness_values[i]/fitness_total
    fitness_values.sort()
    fitness_values_accumulated = []
    for i in range(1,len(fitness_values)+1):
        #print(fitness_values[:i])
        fitness_values_accumulated.append(sum(fitness_values[:i]))
    print(fitness_values_accumulated)
    '''
def draw():
    global life_count
    global generation
    global fitness_values
    global recent_fitness_values
    background(0)
    display_data()
    
    #rocket.draw_rocket()
    fill(200,0,0)
    ellipse(width/2, 50, 40, 40)


    for rocket in rockets:
        #print(vectors[life_count])
        
        rocket.display()
        rocket.move()
        rocket.applyForce(life_count)
        rocket.collisionWall() 
        for barrier in barriers:
            barrier.show()
            rocket.collisionBarrier(barrier)
        #rocket.fitness()
    life_count +=1
    if life_count == lifespan-1:
        for rocket in rockets:
            rocket.eval()
        
        select()
        fitness_values.clear()
        life_count = 0
        generation += 1
        
