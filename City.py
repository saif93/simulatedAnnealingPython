
import math
__author__ = "saif"
__date__ = "$Oct 23, 2016 12:36:26 PM$"
from copy import deepcopy
class city:
    
    def __init__(self,cityList=[i for i in range(20)],
                coords=[(20,20),(20,40),(20,160),(40,120),(60,20),(60,80),(60,200),(80,180),(100,40)
                ,(100,120),(100,160),(120,80),(140,140),(140,180),(160,20),(180,60)
                ,(180,100),(180,200),(200,140),(200,160)]):
        city.cities = cityList
        city.matrix = deepcopy(self.cartesian_matrix(coords))

    def cartesian_matrix(self,coords):
        matrix={}
        max = [[0 for i in range(20)] for j in range(20)]
        for i,(x1,y1) in enumerate(coords):
            for j,(x2,y2) in enumerate(coords):
                dx,dy=x1-x2,y1-y2
                dist=math.sqrt(dx*dx + dy*dy)
                matrix[i,j]=dist
                max[i][j] = round(dist,1)
        return matrix

    def getDistance(city1,city2):
        return city.matrix[city1,city2]
    
    

