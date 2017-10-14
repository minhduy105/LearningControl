from random import sample, choices
import numpy as np

class Tool ():
    def __init__(self,list_cities):
        self.cities = np.arange(len(list_cities))
        self.list_dict = dict(zip(self.cities,list_cities))

    def Get_Distance (self,A,B): #get distance between two points
        return np.sqrt((np.abs(self.list_dict[A][0] - self.list_dict[B][0]))**2
                       + (np.abs(self.list_dict[A][1] - self.list_dict[B][1]))**2)

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
        value = np.asarray(value)
        value = value - np.min(value) + 0.00001
        #add +0.00001 in case all the values ia equally good, which will mess up the random.choices function in Get_Condensed_List function
        return value

    def Get_Condensed_List(self,list_cities,k):
        fit_value = self.Get_Fit_Value(list_cities)
        le = len(fit_value)
        i = 0
        while i < le -k:
            [idx] = choices(range(len(fit_value)), weights=fit_value)
            del list_cities[idx]
            fit_value = np.delete(fit_value,idx)
            i = i + 1
        return list_cities

    def Mutated(self,list_cities):
        le = len(list_cities)
        i = 0
        while i < le:
            list_cities.append(self.Swap_Element(list_cities[i]))
            i = i + 1
        return list_cities

    def Get_Best_Solution_Location(self,list_cities):
        fit_value = self.Get_Fit_Value(list_cities)
        order = np.asarray(fit_value)
        order = np.argsort(order)
        return order[0]

    def Evolution_Algorithm(self, k, t):
        list_cities = self.Generate_Solution(k)
        i = 0
        while i < t:
            list_cities = self.Mutated(list_cities)
            list_cities = self.Get_Condensed_List(list_cities, k)
            i = i + 1
        idx = self.Get_Best_Solution_Location(list_cities)
        return list_cities[idx], self.Get_Total_Distance(list_cities[idx]), self.list_dict

    def Combined(self,parent1, parent2,b):
        comb = parent1[:int(len(parent1)*b)]
        dif = np.setdiff1d(parent2, comb, assume_unique=True)
        comb = np.append(comb,dif)
        return comb

    def Cross_Over(self,list_cities,b):
        le = len(list_cities)
        i = 0
        while i < le:
            new_cities = np.copy(list_cities[i])
            np.random.shuffle(new_cities)
            list_cities.append(new_cities)
            child = self.Combined(list_cities[i],new_cities,b)
            list_cities.append(child)
            i = i + 1

        return list_cities

    def Generic_Algorithm(self,k,t,b):
        list_cities = self.Generate_Solution(k)
        i = 0
        while i < t:
            list_cities = self.Cross_Over(list_cities,b)
            list_cities = self.Get_Condensed_List(list_cities,k)
            i = i + 1
        idx = self.Get_Best_Solution_Location(list_cities)
        return list_cities[idx], self.Get_Total_Distance(list_cities[idx]), self.list_dict



