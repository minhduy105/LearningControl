
import numpy as np
from random import sample, choices
import Tool

def Swap_Element(Cities): #Swap location of two city
    new_cities = np.copy(Cities)
    [iA, iB] = sample(range(Cities.shape[0]), k=2)
    new_cities[iA],new_cities[iB] = Cities[iB],Cities[iA]
    return new_cities

def Stimulated_Annealing(cites,t0,tmin,alpha):
    t = t0
    old_dis = 0
    while t > tmin:
        new_cities = Swap_Element(cites)
        new_dis = Tool.Get_Total_Distance(new_cities)
        old_dis = Tool.Get_Total_Distance(cites)
        if (new_dis < old_dis ):
            cites = new_cities
        else:
            p = np.exp(-(new_dis-old_dis)/t)
            [A] = choices((True, False), weights=[p,1.0-p ]) #choice based on the probability
            if A:
                cites = new_cities
        t = t*alpha
    return cites, old_dis


if __name__ == "__main__":
    t0 = 1000
    tmin = 0.00001
    alpha = 0.95
    data = np.genfromtxt('100cities.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)


    data1 =np.asarray([[1,1],[6,3],[1,3],[6,1]])
    a,b = Stimulated_Annealing(data, t0, tmin, alpha)
    print (a)
    print (b)
