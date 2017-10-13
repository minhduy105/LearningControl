from random import sample, choices
import numpy as np

class Tool ():
    def __init__(self,list_cities):
        self.cities = np.arange(len(list_cities))
        self.list_dict = dict(zip(self.cities,list_cities))

    def Get_Distance (self,A,B): #get distance between two points
        return np.sqrt(np.square(np.abs(self.list_dict[A][0] - self.list_dict[B][0]))
                       + np.square(np.abs(self.list_dict[A][1] - self.list_dict[B][1])))

    def Get_Total_Distance(self,Cities):# get total distance from a path
        total_distance = 0
        num_cities = Cities.shape[0]
        for i in range (num_cities - 1):
            total_distance = total_distance + self.Get_Distance(Cities[i],Cities[i+1])
        total_distance = total_distance + self.Get_Distance(Cities[0],Cities[num_cities - 1])
        return total_distance

    def Swap_Element(self,cities): #Swap location of two city
        new_cities = np.copy(cities)
        [iA, iB] = sample(range(cities.shape[0]), k=2)
        new_cities[iA],new_cities[iB] = cities[iB],cities[iA]
        return new_cities

    def Stimulated_Annealing(self, t0, tmin, alpha):
        t = t0
        old_dis = 0
        while t > tmin:
            new_cities = self.Swap_Element(self.cities)
            new_dis = self.Get_Total_Distance(new_cities)
            old_dis = self.Get_Total_Distance(self.cities)
            if (new_dis < old_dis):
                self.cities = new_cities
            else:
                p = np.exp(-(new_dis - old_dis) / t)
                [A] = choices((True, False), weights=[p, 1.0 - p])  # choice based on the probability
                if A:
                    self.cities = new_cities
            t = t * alpha
        return self.cities, old_dis, self.list_dict

    def Generate_Solution(self,k):
        list_cities = []
        list_cities.append(self.cities)
        for i in range(k-1):
            new_cities = np.copy(self.cities)
            np.random.shuffle((new_cities))
            list_cities.append(new_cities)
        return list_cities

    def Get_Fit_Value(self,list_cites):
        value = []
        for i in list_cites:
            value.append(self.Get_Total_Distance(i))
        return value

    def Get_Condensed_List(self,list_cities,k):
        fit_value = self.Get_Fit_Value(list_cities)
        order = np.asarray(fit_value)
        order = np.argsort(order)
        i = 0
        shorted_list = []
        while i < k:
            shorted_list.append(list_cities[order[i]])
            i = i + 1
        return shorted_list

    def Mutated(self,list_cities):
        le = len(list_cities)
        i = 0
        while i < le:
            list_cities.append(self.Swap_Element(list_cities[i]))
            i = i + 1
        return list_cities

    def Evolution_Algorithm(self, k, t):
        list_cities = self.Generate_Solution(k)
        i = 0
        while i < t:
            list_cities = self.Mutated(list_cities)
            list_cities = self.Get_Condensed_List(list_cities, k)
            i = i + 1
        return list_cities[0], self.Get_Total_Distance(list_cities[0]), self.list_dict


