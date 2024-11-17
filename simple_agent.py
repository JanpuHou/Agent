# Setting the parameters

vowels = ['a', 'i']

personalities = ['F', 'S'] # F= Flexible, S=Stubborn

def make_agent(vowel, personality):
    return [vowel, personality]

# For examaple, we can create a flexible agent with the vowel 'i' using our function

agent_one = make_agent(vowels[1], personalities[0])
print(agent_one)

# Create a function that generates a population of N identical agents with given parameters

def make_population_identical(N):
    
    population = []
    
    for i in range(N):
        
        agent = make_agent(vowels[1], personalities[0])
        
        population.append(agent)

    return population


# Call the function to make a population of 5 identical agents

population_test = make_population_identical(5)
print(population_test)

# Create a function that generates of population of N agents with randomly selected parameters from each list
# using "random.choice()"

import random

def make_population_random(N):
    
    population = []
    
    for i in range(N):
        
        v = random.choice(vowels)
        
        p = random.choice(personalities)
        
        agent = make_agent(v, p)
        
        population.append(agent)

    return population
    
# Call the function to make a population of 5 random agents
population = make_population_random(5)
print(population)    

# You can achieve the same goal using "random.int()" and using the index of the lists of possible parameters

def make_population(N):
    
    population = []
    
    for i in range(N):
        
        v = random.randint(0,1)
        
        p = random.randint(0,1)
        
        agent = make_agent(vowels[v], personalities[p])
        
        population.append(agent)

    return population

# Call the funtion and make a population of 8 random agents
# You can play with the numbers to make bigger or smaller populations
pop = make_population(8)
print(pop)

# Create a function that calculates the proportion of agents with the variant 'a' in the population

def count(population):
    t = 0. # must be a float!     
    for agent in population:
        if agent[0] == 'a':
            t += 1            # The syntax =+ Adds 1 to t (or: t = t + 1)
    return t / len(population)
    
# Call the funtion on a population of 20 random agents
# You can run this box multiple times to see the proportion in different populations of different sizes

prop_a = count(make_population(20))

print('The proportion of [a] in the population is', prop_a)

from numpy.random import choice

def choose_pair(population):
    i = random.randint(0, len(population) - 1) # phyton counts from 0, so pop(8) is an error
    j = random.randint(0, len(population) - 1)
    
    while i == j:
        j = random.randint(0, len(population) - 1) # make sure the same agent is not selected twice
        
    return population[i], population[j]


# And we'll test it to see that really does what we want
# You can run this box of code multiple times to make sure you are really getting random pairs

pop = make_population(8)
listener, producer = choose_pair(pop)

print('The population is', population)
print('This is the chosen pair', listener, producer)
print('The listener is', listener)
print('The producer is', producer)

from copy import deepcopy

def interact_test(listener,producer): 
    
    if listener[0] == producer[0]:
        return listener # if the listener and producer have the same vowel, no change
    else:
        if listener[1]=='S':
            return listener # if the listener is stubborn, no change
        else:
            listener[0]=deepcopy(producer[0])
            return listener
            
randomlistener, randomproducer = choose_pair(make_population(8))

print('The listener is', randomlistener)
print('The producer is', randomproducer)

updated_listener = interact_test(randomlistener, randomproducer)

print('After ineracting, the listener is',updated_listener)
            
# Create a function that only updates agents using "pass" (which means do nothing in Python)

def interact(listener,producer): 
    
    if listener[0] == producer[0]:
        pass   # do nothing
    else:
        if listener[1]=='S':
            pass
        else:
            listener[0]=deepcopy(producer[0])    

# Create a function that simulates a community of size N interacting randomly for K times       

def simulate(n, k):
    
    population = make_population(n)
    
    # print("Initial Population:", population)
    
    proportion = [] # make an empty list to keep track of the porportions after every interaction
    
    for i in range(k):
        
        pair = choose_pair(population) # choose a pair from the population
        
        interact(pair[0],pair[1])  # make the chosen pair interact
        
        proportion.append(count(population)) # track the proportion of the vowels in the population during intrtaction
    
    return population, proportion  

# Simulate 500 interctions between 20 agents 
new_population, proportion = simulate(20, 500)
print("Final Population:", new_population)

# Make a plot of the changes in proportion of 'a' over interactions 


#put plot in the notebook
import matplotlib.pyplot as plt # importing a plotting library
plt.plot(proportion)
plt.show()

# and add some details to the plot
plt.title('Changes in the proportion of [a] over time')
plt.ylabel('Proportion [a] users')
plt.xlabel('Time [No. of interactions]')
plt.ylim(0,1)

 # Simulate 5000 interctions between 200 agents 
new_population, proportion = simulate(200, 5000)
#print("Final Population:", new_population)

# Make a plot of the changes in proportion of 'a' over interactions 
print('   ')
print('Changes in the proportion of [a] over time')
plt.plot(proportion)
plt.ylim(0,1)   

# Create a function that runs s simulations of a community of size N interacting randomly for K times    

def batch_simulate(n,k,s):
    batch_proportions=[]
    for i in range(s):
        new_population, proportion = simulate(n, k)
        batch_proportions.append(proportion)
    return batch_proportions
 
# Make 20 simulations of 5000 interctions between 200 agents 
results = batch_simulate(200,5000,20)

plt.ylim(0,1)
plt.show()

for i in results:
    plt.plot(i) 
    
plt.show()