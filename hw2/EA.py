from Tool import Tool
import numpy as np
import datetime
import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    k = 20
    t = 1000
    st = 1
    name = '100cities.csv'
    data = np.genfromtxt(name, delimiter=',')
    data = np.delete(data, (0), axis=0)
    data1 =np.asarray([[1,1],[6,3],[1,3],[6,1],[8,1]])
    tools = Tool(data)
    time = []
    for i in range(1):
        start = datetime.datetime.now().timestamp()
        a, b, c = tools.Evolution_Algorithm(k,t,st)
        end = datetime.datetime.now().timestamp()
        time.append(end - start)
    # with open("Result\Time\outEA" + name, "w", newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows([time])
    # print(time)
    tools.Draw_Graph( a, c, name, 'bo-')