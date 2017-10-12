import Tool
import numpy as np


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
