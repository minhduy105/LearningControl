from Tool import Tool
import numpy as np

if __name__ == "__main__":
    k = 5
    t = 500
    data = np.genfromtxt('15cities.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)
#    data1 =np.asarray([[1,1],[6,3],[1,3],[6,1],[8,1]])
    tools = Tool(data)
    a,b,c = tools.Evolution_Algorithm(k,t)
    print (a)
    print (b)
