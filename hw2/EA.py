import Tool
import numpy as np

def Mutated(list_cities):
    le = len(list_cities)
    i = 0
    while i < le:
        list_cities.append(Tool.Swap_Element(list_cities[i]))
        i = i + 1
    return list_cities

def Evolution_Algorithm(cities,k,t):
    list_cities = Tool.Generate_Solution(cities, k)
    i = 0
    while i < t:
        list_cities = Mutated(list_cities)
        list_cities = Tool.Get_Condensed_List(list_cities,k)
        i = i + 1
    return list_cities[0] , Tool.Get_Total_Distance(list_cities[0])

if __name__ == "__main__":
    k = 5
    t = 500
    data = np.genfromtxt('15cities.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)
#    data1 =np.asarray([[1,1],[6,3],[1,3],[6,1],[8,1]])

    a,b = Evolution_Algorithm(data,k,t)
    print (a)
    print (b)
    #
    # list_cities = Generate_Solution(data1,k)
    # fit_value = Get_Fit_Value(list_cities)
    #
    # order = np.asarray(fit_value)
    # order = np.argsort(order)
    # print (fit_value)
    # print (order)
    # # i = 2
    # while i < len(dele):
    #     del dict[dele[i]]
    #     i = i + 1
    #
    # print (dict)

    # a,b = (data, t0, tmin, alpha)
    # print (a)
    # print (b)
