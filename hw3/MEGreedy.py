import numpy as np
import  random
import matplotlib.pyplot as plt
from Map import Map
from PIL import Image


def E_Greedy_Algorithm(termT, obj, alpha, e,start):
    i = 0
    dec = []  # index or the decision make
    val = []  # get the value reward overtime
    tolR = []
    totalR = 0
    st = start
    re, dir = obj.Get_Reward(st)
    #reward = np.ones(np.asarray(re).shape[0]) * random.randint(-15, 15)
    reward = np.zeros(np.asarray(re).shape[0])
    while i < termT:
        reR, dir = obj.Get_Reward(st)
        reward = reward + alpha * (reR - reward)
        [TF] = random.choices([True, False], weights=[1.0 - e, e])
        if TF:
            goodV = np.asarray(np.where(reward == reward.max()))
            errV = np.asarray(np.where(np.asarray(reR) > -8))
            locs = np.intersect1d(goodV,errV)
            if locs.size == 0:
                [locs] = errV
        else:
            badV = np.asarray(np.where(reward != reward.max()))
            errV = np.asarray(np.where(np.asarray(reR) > -8))
            locs = np.intersect1d(badV,errV)
            if locs.size == 0:
                [locs] = errV

        loc = random.choice(locs)
        dec.append(st)
        i = i + 1
        st = dir[loc]
        totalR = totalR + reward[loc]
        val.append(reward[loc])
        tolR.append(totalR)
    return dec, val, tolR

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


map =  np.genfromtxt('Map.csv', dtype=float, delimiter=',')
(y,x) = map.shape
valAllAve = []
valAllStd = []
tolAllAve = []
tolAllStd = []
# st = [random.randint(0,y-1),random.randint(0,x-1)]
# print (st)
# st = [random.randint(0, y - 1), random.randint(0, x - 1)]
for j in range(10):

    # re, pos = M.Get_Reward([4,9]) #[y,x]
    termT = 100
    e = round (0.02 * (j + 1),3)
    a = 0.1
    i = 0
    terT = 10000
    decA = []
    valA = []
    tolRA = []
    raw = np.zeros(map.shape)
    while i < terT:
        M = Map(map)
        st = [random.randint(0, y - 1), random.randint(0, x - 1)]
        dec, val, tolR = E_Greedy_Algorithm(termT, M, a, e, st)
        decA.append(dec)
        valA.append(val)
        tolRA.append(tolR)
        for j in dec:
            raw[j[0]][j[1]] =+ 1.0
        i = i +1


    title = "E_Greedy_" + str(a) + "alpha_" + str(e) + "e_random" + str(st[0])+"," + str(st[1])
    name = "Graph\\"+title+ "_run_" + str(terT) + "times_average_reward"
    csvname = "Graph\\Info\\"+title+ "_run_" + str(terT) + "times_average_reward"
    Draw_Graph(valA,title,"times","average_reward",name,csvname)

    name = "Graph\\" + title + "_run_" + str(terT) + "times_total_reward"
    csvname = "Graph\\Info\\" + title + "_run_" + str(terT) + "times_total_reward"
    Draw_Graph(tolRA,title,"times","total_reward",name,csvname)
    print(e)

    # imageName = "Graph\\" + title + "pic.jpeg"
    # raw = raw/raw.max()*255.0
    # print(raw)
    # im = Image.fromarray(raw)
    # im.save(imageName)
    # # plt.imsave(imageName,raw,cmap='gray')




# print (re)
# print (pos)