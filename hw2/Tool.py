from random import sample, choices
import numpy as np
import matplotlib.pyplot as plt

class Tool ():
    #get the cities and assigned a ID number for it
    def __init__(self,list_cities):
        self.cities = np.arange(len(list_cities))
        self.list_dict = dict(zip(self.cities,list_cities))

    #Accepted the ID number of city A and B and calculate the distance between the two of them
    def Get_Distance (self,A,B): #get distance between two points
        return np.sqrt((np.abs(self.list_dict[A][0] - self.list_dict[B][0]))**2
                       + (np.abs(self.list_dict[A][1] - self.list_dict[B][1]))**2)

    # Get total distance from a solution path (Cities)
    def Get_Total_Distance(self,Cities):
        total_distance = 0
        num_cities = Cities.shape[0]
        for i in range (num_cities - 1):
            total_distance = total_distance + self.Get_Distance(Cities[i],Cities[i+1])
        total_distance = total_distance + self.Get_Distance(Cities[0],Cities[num_cities - 1])
        #distance between first and last element
        return total_distance

    # Swap the location of two city in a solution path (cities)
    # t is how many times you want to swap cities
    def Swap_Element(self,cities,t):
        new_cities = np.copy(cities)
        i = 0
        while i < t:
            [iA, iB] = sample(range(cities.shape[0]), k=2)
            new_cities[iA],new_cities[iB] = cities[iB],cities[iA]
            i = i + 1
        return new_cities

    # The stimulated Annealing function,
    # t0 is the initial temperature
    # tmin is the minimum temperature, the program will stop after this need to be smaller than t0
    # alpha is how much you update the temperature overtime, need to be < 1
    #st is how many times you want to swap the element
    def Stimulated_Annealing(self, t0, tmin, alpha,st):
        t = t0
        old_dis = 0
        while t > tmin:
            new_cities = self.Swap_Element(self.cities,st)
            new_dis = self.Get_Total_Distance(new_cities)
            old_dis = self.Get_Total_Distance(self.cities)
            if (new_dis < old_dis):
                self.cities = new_cities
            else:
                p = np.exp(-(new_dis - old_dis) / t) #calculate the probability
                [A] = choices((True, False), weights=[p, 1.0 - p])  # choice based on the probability
                if A:
                    self.cities = new_cities
            t = t * alpha
        return self.cities, old_dis, self.list_dict

    # The stimulated Annealing function,
    # t0 is the initial temperature
    # tmin is the minimum temperature, the program will stop after this need to be smaller than t0
    # alpha is how much you update the temperature overtime, need to be < 1
    #st is how many times you want to swap the element
    def Stimulated_Annealing_Epoch(self, t0, tmin, alpha,st,epoch_num):
        t = t0
        old_dis = 0
        iE = 0
        epoch = []
        while t > tmin:
            new_cities = self.Swap_Element(self.cities,st)
            new_dis = self.Get_Total_Distance(new_cities)
            old_dis = self.Get_Total_Distance(self.cities)
            if (new_dis < old_dis):
                self.cities = new_cities
            else:
                p = np.exp(-(new_dis. - old_dis) / t) #calculate the probability
                [A] = choices((True, False), weights=[p, 1.0 - p])  # choice based on the probability
                if A:
                    self.cities = new_cities
            iE = iE + 1
            if iE >= epoch_num:
                epoch.append(self.Get_Total_Distance(self.cities))
                iE =0

            t = t * alpha
        return self.cities, old_dis, self.list_dict, epoch


    # generate a list of solution, the size of the list is k
    def Generate_Solution(self,k):
        list_cities = []
        list_cities.append(self.cities)
        for i in range(k-1):
            new_cities = np.copy(self.cities)
            np.random.shuffle((new_cities))
            list_cities.append(new_cities)
        return list_cities

    # get the fit value, which is the dif between the path distances in the last and the best(smallest) path in the list
    # the reason for using the different is we want to emphasize it when we look at the best result
    # NOTE: it will return the fitness in reverse
    def Get_Fit_Value(self,list_cites):
        value = []
        for i in list_cites:
            value.append(self.Get_Total_Distance(i))
        value = np.asarray(value)
        value = value - np.min(value) + 0.00001
        #add +0.00001 in case all the values ia equally good,
        #which will mess up the random.choices function in Get_Condensed_List function
        return value

    # shorten the population back to k number of elements using fitness value
    def Get_Condensed_List(self,list_cities,k):
        fit_value = self.Get_Fit_Value(list_cities)
        le = len(fit_value)
        i = 0
        # the ideas is delete the path/solutions that is large, it pick them based on the inverse fit value
        while i < le -k:
            [idx] = choices(range(len(fit_value)), weights=fit_value)
            del list_cities[idx]#because this is list
            fit_value = np.delete(fit_value,idx)#because this is numpy
            i = i + 1
        return list_cities

    # this creates a mutation set of the cities list and add it back to the city list
    def Mutated(self,list_cities,st):
        le = len(list_cities)
        i = 0
        while i < le:
            new_cities = self.Swap_Element(list_cities[i],st)
            list_cities.append(new_cities)
            i = i + 1
        return list_cities

    # get the best solution from a list of cities
    def Get_Best_Solution_Location(self,list_cities):
        fit_value = self.Get_Fit_Value(list_cities)
        order = np.asarray(fit_value)
        order = np.argsort(order)
        return order[0]

    #this is the Evolution Algorithm program
    # k is the size of the population
    # t is the number of time we run the algorithm
    # st is how many times you want to swap the element
    def Evolution_Algorithm(self, k, t,st):
        list_cities = self.Generate_Solution(k)
        i = 0
        while i < t:
            list_cities = self.Mutated(list_cities,st)
            list_cities = self.Get_Condensed_List(list_cities, k)
            i = i + 1
        idx = self.Get_Best_Solution_Location(list_cities)
        return list_cities[idx], self.Get_Total_Distance(list_cities[idx]), self.list_dict

    # Combined two parents solution and return a child
    def Combined(self,parent1, parent2,b):
        comb = parent1[:int(len(parent1)*b)]
        dif = np.setdiff1d(parent2, comb, assume_unique=True)#get the cities that is in parent 2 but not in comb
        comb = np.append(comb,dif)
        return comb

    #this is the function that handle cross over between two parents
    def Cross_Over(self,list_cities,b):
        le = len(list_cities)
        i = 0
        # create the new population with a new element/parent and a child from that new parent and an existed parent
        while i < le:
            new_cities = np.copy(list_cities[i])# need to use copy for deepcopy
            np.random.shuffle(new_cities)
            list_cities.append(new_cities)
            child = self.Combined(list_cities[i],new_cities,b)
            list_cities.append(child)
            i = i + 1

        return list_cities

    # This is the Generic Algorithm
    # k is the size of the population
    # t is how many time we ran it
    # b is the percent of gene from the existed parent that we will keep
    def Generic_Algorithm(self,k,t,b):
        list_cities = self.Generate_Solution(k)
        i = 0
        while i < t:
            list_cities = self.Cross_Over(list_cities,b)
            list_cities = self.Get_Condensed_List(list_cities,k)
            i = i + 1
        idx = self.Get_Best_Solution_Location(list_cities)
        return list_cities[idx], self.Get_Total_Distance(list_cities[idx]), self.list_dict

    #Draw the graph based on the cities name and dictionary
    #cities is cities name
    #dict is the dictionary
    #name is the name of the file
    #color and line, ex 'ro-'
    def Draw_Graph(self,cities,dict,name,color):
        result = []
        for i in cities:
            result.append(dict[i])
        result = np.asarray(result)
        result = np.append(result, result[0].reshape((1, 2)), axis=0)
        x = result[:, 0]
        y = result[:, 1]
        fig = plt.figure()
        plt.plot(x, y, color)
        #plt.errorbar(x,y,yerr=20)
        plt.ylabel('y')
        plt.xlabel('x')
        plt.title(name)
        fig.savefig(name + '.png')
        plt.close(fig)
