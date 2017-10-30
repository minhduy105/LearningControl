from Tool import Tool
import numpy as np
import datetime
import csv
import matplotlib.pyplot as plt
import copy

if __name__ == "__main__":
    k = 30
    t = 1000
    st = 1
    epoch = 50
    name = '15cities'
    data = np.genfromtxt(name+'.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)


    resultSum = []
    resultSD = []
    result = []
    time = []
    bestR = []
    bestD = 10**(20)
    dict = []
    constk = 10
    st_root = 1
    for idx in range(5):
        result = []
        k = (idx+1)*constk
        # st = st_root + 2 * idx
        ep = []

        #get the time
        tools = Tool(data)
        start = datetime.datetime.now().timestamp()
        a, b, c = tools.Evolution_Algorithm(k, t, st)
        end = datetime.datetime.now().timestamp()
        time.append(end-start)

        for i in range(10):
            np.random.shuffle(data)
            tools = Tool(data)
            a, b, c, e = tools.Evolution_Algorithm_Epoch(k,t,st, epoch)
            ep.append(e)
            if  b < bestD:
                bestR = np.copy(a)
                bestD = b
                dict = copy.deepcopy(c)

        ep = np.asarray(ep)
        resultSum.append(np.sum(ep, axis=0).tolist())
        resultSD.append(np.std(ep, axis=0).tolist())
        result = copy.deepcopy(resultSum)
        result.extend(resultSD)
        print(result)
        with open("Result\Summary\EA" + name + "_" + str(k) + "binsize_" + str(t) + "iterate_" + str(
                st) + "swaptime.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

    with open("Result\Summary\Time\EATime" + name + "_" + str(k) + "binsize_" + str(t) + "iterate_" + str(
            st) + "swaptime.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(time)

    tools = Tool(data)
    nameGraph = "Result\Summary\Graph\EA" + name
    tools.Draw_Graph(bestR, dict, nameGraph, 'bo-', 'EA' + name)

        # time = []
    # for i in range(1):
    #     start = datetime.datetime.now().timestamp()
    #     a, b, c = tools.Evolution_Algorithm(k,t,st)
    #     end = datetime.datetime.now().timestamp()
    #     time.append(end - start)
    # with open("Result\Time\outEA" + name, "w", newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows([time])
    # print(time)
    # tools.Draw_Graph( a, c, name, 'bo-')