
import numpy as np
from Tool import Tool

if __name__ == "__main__":
    t0 = 1000000
    tmin = 0.00001
    alpha = 0.95
    data = np.genfromtxt('15cities.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)
    data1 = np.asarray([[1, 1], [6, 3], [1, 3], [6, 1], [8, 1]])
    np.random.shuffle(data)
    tools = Tool(data)

    a,b,c = tools.Stimulated_Annealing(t0, tmin, alpha)
    print (a)
    print (b)
