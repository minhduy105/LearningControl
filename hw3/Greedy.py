import numpy as np
import random
from ArmBandit import ArmBanbit
import matplotlib.pyplot as plt

def Greedy_Algorithm(termT,obj,alpha):
    i = 0
    dec = [] #index or the decision make
    val = [] #get the value reward overtime
    tolR = []
    totalR = 0
    reward = np.ones(obj.Get_Reward().shape[0]) * random.randint(-15,15)
    while i < termT:
        value = obj.Get_Reward()
        # reward = reward + 1.0/(i+1) * (value - reward)
        # reward = reward + alpha *(value-reward)
        reward = reward + alpha * (value - reward)
        #print(reward)
        [locs] = np.asarray(np.where(reward == reward.max()))
        loc = random.choice(locs)
        dec.append(loc)
        #print (value[loc])
        i = i + 1
        totalR = totalR + reward[loc]
        val.append(reward[loc])
        tolR.append(totalR)

    return dec , val, tolR


def Draw_Graph(data,title,xname,yname,name,csvname):
    all = np.asarray(data)
    y = np.mean(all,axis=0)
    err = np.std(all,axis=0)
    x = np.arange(1,y.shape[0]+1)
    fig = plt.figure()
    plt.errorbar(x, y, yerr=err,fmt='.-')
    plt.xlabel(xname, fontsize=16)
    plt.ylabel(yname, fontsize=16)
    plt.title(title)
    fig.savefig(name+".png")
    plt.close()
    np.savetxt(csvname+"_ave.csv", y, delimiter=',')
    np.savetxt(csvname+"_std.csv", err, delimiter=',')

data = np.asarray([[1,5],[1.5,1],[2,1],[2,2],[1.75,10]])
for j in range(1):

    a = round (0.05 * (j + 1),3)
    i = 0
    terT = 100
    decA = []
    valA = []
    tolRA = []
    while i < 10000:
        AB = ArmBanbit(data)
        dec , val, tolR = Greedy_Algorithm(terT,AB,a)
        decA.append(dec)
        valA.append(val)
        tolRA.append(tolR)
        i = i +1

    title = "Greedy_" + str(a) + "alpha"
    name = "Graph\\"+title+ "_run_" + str(terT) + "times_average_reward"
    # true = np.ones(np.asarray(valA).shape[1]) * 2.0
    csvname = "Graph\\Info\\"+title+ "_run_" + str(terT) + "times_average_reward"
    Draw_Graph(valA,title,"times","average_reward",name,csvname)


    name = "Graph\\"+title+ "_run_" + str(terT) + "times_total_reward"
    # true = np.arange(1,np.asarray(valA).shape[1]+1) * 2.0
    csvname = "Graph\\Info\\" + title + "_run_" + str(terT) + "times_total_reward"
    Draw_Graph(tolRA,title,"times","total_reward",name,csvname)
    print(a)


# value = np.asarray([10,5,10,6,8,10])
# [loc] = np.asarray(np.where(value==value.max()))
# print (loc)
# print (random.choice(loc))