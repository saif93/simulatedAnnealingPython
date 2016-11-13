
from copy import deepcopy
from City import city
import random

class Tour:

#    // Holds our tour of cities
    distance =0
#    // Constructs a blank tour
    def __init__(self,tour=[]):
        self.tour =  tour
        self.cities = deepcopy(city.cities)
        
        if self.tour ==[]:
            self.tour= [0 for i in range (len(self.cities))]
    
#    // Returns tour information
    def getTour(self):
        return self.tour


#    // Creates a random individual
    def generateIndividual(self):
#        // Loop through all our destination cities and add them to our tour
        for cityIndex in range (len(self.cities)):
          self.setCity(cityIndex, self.cities[cityIndex])
        
#        // Randomly reorder the tour
        random.shuffle(self.tour)
   
#    // Gets a city from the tour
    def getCity(self,tourPosition):
        return self.tour[tourPosition]
    

#    // Sets a city in a certain position within a tour
    def setCity(self, tourPosition, city):
        self.tour[tourPosition]=city
#        // If the tours been altered we need to reset the fitness and distance
        self.distance = 0;
    
    
#    // Gets the total distance of the tour
    def getDistance(self):
        if (self.distance == 0):
            tourDistance = 0
#            // Loop through our tour's cities
            for cityIndex in range (len(self.tour)) :
#                // Get city we're traveling from
                fromCity = self.getCity(cityIndex)
#                // City we're traveling to
#                destinationCity;
#                // Check we're not on our tour's last city, if we are set our
#                // tour's final destination city to our starting city
                if(cityIndex+1 < len(self.tour)):
                    destinationCity = self.getCity(cityIndex+1)
                else:
                    destinationCity = self.getCity(0)
                
#                // Get the distance between the two cities
                tourDistance += city.getDistance(fromCity,destinationCity)
            self.distance = tourDistance
        
        return self.distance;
    

#    // Get number of cities on our tour
    def tourSize(self):
        return len(self.tour)

