
import numpy as np
from Tool import Tool
import datetime
import csv
import copy
import matplotlib.pyplot as plt

if __name__ == "__main__":
    t0 = 1
    alpha = 0.95
    m = 1000
    epoch = 50
    tmin = alpha**(m)
    st = 1 #swap time
    name = '15cities'
    data = np.genfromtxt(name+'.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)
    #data1 = np.asarray([[1, 1], [6, 3], [1, 3], [6, 1], [8, 1]])
    ade = 0.1
    alpha_root = 0.95
    resultSum = []
    resultSD = []
    result = []
    time = []

    bestR = []
    bestD = 10**(20)
    dict = []
    st_root = 1
    for idx in range(5):
        result = []
        alpha = alpha_root - 0.1*idx
        # st = st_root + 2*idx
        tmin = alpha ** (m)
        ep = []

        tools = Tool(data)
        start = datetime.datetime.now().timestamp()
        a, b, c = tools.Stimulated_Annealing(t0, tmin, alpha,st)
        end = datetime.datetime.now().timestamp()
        time.append(end-start)

        for i in range(10):
            np.random.shuffle(data)
            tools = Tool(data)
            a, b, c,e = tools.Stimulated_Annealing_Epoch(t0, tmin, alpha, st,epoch)
            ep.append(e)
            if  b < bestD:
                bestR = np.copy(a)
                bestD = b
                dict = copy.deepcopy(c)

        ep = np.asarray(ep)
        resultSum.append(np.sum(ep,axis=0).tolist())
        resultSD.append(np.std(ep,axis=0).tolist())
        result = copy.deepcopy(resultSum)
        result.extend(resultSD)
    #    print(result)
        with open("Result\Summary\AS"+name+"_"+str(alpha)+"alpha_"+str(m)+"iterate_"+str(st)+"swaptime.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)
    #print (time)
    with open("Result\Summary\Time\ASTime" + name + "_" + str(alpha) + "alpha_" + str(m) + "iterate_" + str(
            st) + "swaptime.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(time)

    tools = Tool(data)
    nameGraph = "Result\Summary\Graph\AS" + name
    tools.Draw_Graph(bestR,dict,nameGraph,'bo-','AS'+name)

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
