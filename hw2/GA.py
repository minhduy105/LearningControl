from Tool import Tool
import numpy as np

if __name__ == "__main__":
    k = 20
    t = 1000
    b = 0.3
    data = np.genfromtxt('15cities.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)
    data1 =np.asarray([[1,1],[6,3],[1,3],[6,1],[8,1]])
    tools = Tool(data)
    a,b,c = tools.Generic_Algorithm(k,t,b)
    print (a)
    print (b)
