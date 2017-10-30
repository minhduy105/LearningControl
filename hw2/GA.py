from Tool import Tool
import numpy as np
import datetime
import csv
import copy
if __name__ == "__main__":
    k = 30
    t = 1000
    percent = 0.3
    epoch = 50
    name = '25cities_A'
    data = np.genfromtxt(name + '.csv', delimiter=',')
    data = np.delete(data, (0), axis=0)


    resultSum = []
    resultSD = []
    result = []
    time = []
    bestR = []
    bestD = 10**(20)
    dict = []
    constk = 10
    for idx in range(5):
        result = []
        k = (idx+1)*constk
        # percent = 0.1 + 0.1*idx
        ep = []

        #get the time
        tools = Tool(data)
        start = datetime.datetime.now().timestamp()
        a, b, c = tools.Generic_Algorithm(k,t,percent)
        end = datetime.datetime.now().timestamp()
        time.append(end-start)

        for i in range(10):
            np.random.shuffle(data)
            tools = Tool(data)
            a, b, c, e = tools.Generic_Algorithm_Epoch(k,t,percent, epoch)
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
        with open("Result\Summary\GA" + name + "_" + str(k) + "binsize_" + str(t) + "iterate_" + str(
                percent) + "keepgene.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

    with open("Result\Summary\Time\GATime" + name + "_" + str(k) + "binsize_" + str(t) + "iterate_" + str(
            percent) + "keepgene.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(time)

    tools = Tool(data)
    nameGraph = "Result\Summary\Graph\GA" + name
    tools.Draw_Graph(bestR, dict, nameGraph, 'bo-', 'GA' + name)







    # tools = Tool(data)
    # time = []
    # for i in range(10):
    #     start = datetime.datetime.now().timestamp()
    #     a, b, c = tools.Generic_Algorithm(k,t,b)
    #     end = datetime.datetime.now().timestamp()
    #     time.append(end - start)
    # # with open("Result\Time\outGA" + name, "w", newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows([time])
    # print(time)
    # tools.Draw_Graph(a, c, name, 'ro-')