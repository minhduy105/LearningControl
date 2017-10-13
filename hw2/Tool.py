from random import sample
import numpy as np

def Get_Distance (A,B): #get distance between two points
    return np.sqrt(np.square(np.abs(A[0] - B[0])) + np.square(np.abs(A[1] - B[1])))

def Get_Total_Distance(Cities):# get total distance from a path
    total_distance = 0
    num_cities = Cities.shape[0]
    for i in range (num_cities - 1):
        total_distance = total_distance + Get_Distance(Cities[i],Cities[i+1])
    total_distance = total_distance + Get_Distance(Cities[0],Cities[num_cities - 1])
    return total_distance

def Swap_Element(Cities): #Swap location of two city
    new_cities = np.copy(Cities)
    [iA, iB] = sample(range(Cities.shape[0]), k=2)
    new_cities[iA],new_cities[iB] = Cities[iB],Cities[iA]
    return new_cities

def Generate_Solution(cities,k):
    list_cities = []
    list_cities.append(cities)
    for i in range(k-1):
        new_cities = np.copy(cities)
        np.random.shuffle((new_cities))
        list_cities.append(new_cities)
    return list_cities

def Get_Fit_Value(list_cites):
    value = []
    for i in list_cites:
        value.append(Get_Total_Distance(i))
    return value

def Get_Condensed_List(list_cities,k):
    fit_value = Get_Fit_Value(list_cities)
    order = np.asarray(fit_value)
    order = np.argsort(order)
    i = 0
    shorted_list = []
    while i < k:
        shorted_list.append(list_cities[order[i]])
        i = i + 1
    return shorted_list