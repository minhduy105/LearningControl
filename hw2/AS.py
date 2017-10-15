
import numpy as np
from Tool import Tool
import datetime
import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    t0 = 1
    alpha = 0.95
    m = 2000
    epoch = 50
    tmin = alpha**(m)
    st = 1 #swap time
    name = '100cities'
    data = np.genfromtxt(name+'.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)
    #data1 = np.asarray([[1, 1], [6, 3], [1, 3], [6, 1], [8, 1]])
    ade = 0.05
    alpha_root = 0.99

    for idx in range(10):
        alpha = alpha_root - idx*ade
        tmin = alpha ** (m)
        ep = []
        for i in range(10):
            np.random.shuffle(data)
            tools = Tool(data)
            a, b, c,e = tools.Stimulated_Annealing_Epoch(t0, tmin, alpha, st,epoch)
            ep.append(e)
        print(alpha)
        print(ep)

        with open("Result\Epoch\\"+name+"_"+str(alpha)+"alpha_"+str(m)+"iterate_"+str(st)+"swaptime.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(ep)



    # time = []
    # for i in range(1):
    #     start = datetime.datetime.now().timestamp()
    #     a,b,c = tools.Stimulated_Annealing(t0, tmin, alpha,st)
    #     end = datetime.datetime.now().timestamp()
    #     time.append(end-start)
    # print (b)

    # with open("Result\Time\outAS"+name, "w", newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows([time])
    # print (time)
