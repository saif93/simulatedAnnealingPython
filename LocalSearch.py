"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
implementation of  Simulated Annealing in Python
Date:           Oct 22, 2016 7:31:55 PM
Programmed By:  Muhammad Saif ul islam
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import math
import random
from copy import deepcopy
from Tour import Tour
from City import city

class LocalSearch:
    
    temp = 10000
    coolingRate = 0.003
    
    def __init__(self):
        self.cities = deepcopy(city.cities)
    
    def acceptanceProbability(self,energy,  newEnergy, temperature):
#         If the new solution is better, accept it
        if (newEnergy < energy):
            return 1.0
#        // If the new solution is worse, calculate an acceptance probability

        return math.exp((energy - newEnergy) / temperature)
    
    
    def simulatedAnnealing(self):
        currentSolution = Tour()
        currentSolution.generateIndividual()
        
        print("Initial solution distance: " ,  currentSolution.getDistance())
        print("Initil path:",currentSolution.getTour())

#        // Set as current best
        best =  deepcopy(Tour(currentSolution.getTour()))
   
#        // Loop until system has cooled
        while (self.temp > 1) :
#            // Create new neighbour tour
            newSolution =  deepcopy(Tour(currentSolution.getTour()))
            
#            // Get a random positions in the tour random.randrange(0,19,1)
            tourPos1 = random.randrange(0,newSolution.tourSize(),1) 
            tourPos2 = random.randrange(0,newSolution.tourSize(),1)

#            // Get the cities at selected positions in the tour
            citySwap1 = newSolution.getCity(tourPos1)
            citySwap2 = newSolution.getCity(tourPos2)
           
#            // Swap them
            newSolution.setCity(tourPos2, citySwap1);
            newSolution.setCity(tourPos1, citySwap2);
            
#            // Get energy of solutions
            currentEnergy = currentSolution.getDistance()
            neighbourEnergy = newSolution.getDistance()

#            // Decide if we should accept the neighbour
            if (self.acceptanceProbability(currentEnergy, neighbourEnergy, self.temp) >= random.randint(1,19)) :
                currentSolution =  deepcopy(Tour(newSolution.getTour()))
               
                
#           // Keep track of the best solution found
            if (currentSolution.getDistance() < best.getDistance()) :
            
                best =  deepcopy(Tour(currentSolution.getTour()))
            
            
#            // Cool system
            self.temp *= 1- self.coolingRate
          
        print("\n\nFinal solution distance: " , best.getDistance())
        print("Final path: " , best.getTour())

"""
Testing
"""
initializeCities = city()

localSearch = LocalSearch()
localSearch.simulatedAnnealing()
