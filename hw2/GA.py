import Tool
import numpy as np

def Combined (parent1, parent2):
    comb = parent1
    return comb

def Cross_Over(list_cities):
    le = len(list_cities)
    i = 0
    while i < le:
        new_cities = np.copy(list_cities[i])
        list_cities.append(np.random.shuffle((new_cities)))


def Generic_Algorithm(cities,k,t):
    list_cities = Tool.Generate_Solution(cities, k)
    i = 0
    while i < t:
        list_cities = Cross_Over(list_cities)
        list_cities = Tool.Get_Condensed_List(list_cities,k)
        i = i + 1
    return list_cities[0] , Tool.Get_Total_Distance(list_cities[0])

if __name__ == "__main__":
    k = 5
    t = 1
    data = np.genfromtxt('15cities.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)
#    data1 =np.asarray([[1,1],[6,3],[1,3],[6,1],[8,1]])

    a,b = Generic_Algorithm(data,k,t)
    print (a)
    print (b)