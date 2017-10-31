import numpy as np
import  random
import matplotlib.pyplot as plt
from Map import Map

def Get_Q(sta,pos): #update the surrounding and get Q action
    (z,y,x) = sta.shape

    reward = []
    repos = []

    if pos[0] > 0:  # UP
        sta[0][pos[0]][pos[1]] = sta[4][pos[0] - 1][pos[1]]
    else:
        sta[0][pos[0]][pos[1]] = -10000
    reward.append(sta[0][pos[0]][pos[1]])
    repos.append([pos[0] - 1, pos[1]])

    if pos[1] < x - 1:  # RIGHT
        sta[1][pos[0]][pos[1]] = sta[4][pos[0]][pos[1] + 1]
    else:
        sta[1][pos[0]][pos[1]] = -10000
    reward.append(sta[1][pos[0]][pos[1]])
    repos.append([pos[0], pos[1] + 1])

    if pos[0] < y - 1:  # DOWN
        sta[2][pos[0]][pos[1]] = sta[4][pos[0] + 1][pos[1]]
    else:
        sta[2][pos[0]][pos[1]] = -10000
    reward.append(sta[2][pos[0]][pos[1]])
    repos.append([pos[0] + 1, pos[1]])

    if pos[1] > 0:
        sta[3][pos[0]][pos[1]] = sta[4][pos[0]][pos[1] - 1]
    else:
        sta[3][pos[0]][pos[1]] = -10000
    reward.append(sta[3][pos[0]][pos[1]])
    repos.append([pos[0], pos[1] - 1])

    reward.append(sta[4][pos[0]][pos[1]])
    repos.append([pos[0], pos[1]])

    return sta, reward, repos


def Update_Q(sta,loc,map,y,a):
    sta, Qset, xyCor = Get_Q(sta,loc)
    dif = a* (map[loc[0]][loc[1]] + y * np.max(np.asarray(Qset)) - sta[4][loc[0]][loc[1]])
    sta[4][loc[0]][loc[1]] = sta[4][loc[0]][loc[1]] + dif
    return sta

def Q_Learning(map,loc,y,a,e,ite):
    M = Map(map)
    i = 0
    (x1, x2) = map.shape
    sta = np.zeros((5, x1, x2))
    while i < ite:
        sta = Update_Q(sta,loc,map,y,a)
        loc = Take_Action(sta,loc,e)
        i = i + 1
        print (sta[4,:,:])
    return sta

def Take_Action(sta,loc,e):
    sta, reward, xyCor = Get_Q(sta,loc)
    [TF] = random.choices([True, False], weights=[1.0 - e, e])
    if TF:
        goodV = np.asarray(np.where(np.asarray(reward) == np.asarray(reward).max()))
        errV = np.asarray(np.where(np.asarray(reward) > -1000))
        locs = np.intersect1d(goodV, errV)
        if locs.size == 0:
            [locs] = errV
    else:
        badV = np.asarray(np.where(np.asarray(reward) != np.asarray(reward).max()))
        errV = np.asarray(np.where(np.asarray(reward) > -1000))
        locs = np.intersect1d(badV, errV)
        if locs.size == 0:
            [locs] = errV

    loc = random.choice(locs)
    return xyCor[loc]

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
st = [random.randint(0,y-1),random.randint(0,x-1)]
y1 = 0.9
a = 0.1
ite = 100
e = 0.001
state = Q_Learning(map,st,y1,a,e,ite)

#
# st = [random.randint(0, y - 1), random.randint(0, x - 1)]
# for j in range(10):
#
#     # re, pos = M.Get_Reward([4,9]) #[y,x]
#     termT = 20
#     e = round (0.02 * (j + 1),3)
#     a = 0.1
#     i = 0
#     terT = 10000
#     decA = []
#     valA = []
#     tolRA = []
#     raw = np.zeros(map.shape)
#     while i < terT:
#         M = Map(map)
#         #st = [random.randint(0, y - 1), random.randint(0, x - 1)]
#         dec, val, tolR = E_Greedy_Algorithm(termT, M, a, e, st)
#         decA.append(dec)
#         valA.append(val)
#         tolRA.append(tolR)
#         for j in dec:
#             raw[j[0]][j[1]] =+ 1.0
#         i = i +1
#
#
#     title = "E_Greedy_" + str(a) + "alpha_" + str(e) + "e_stable_at_" + str(st[0])+"," + str(st[1])
#     name = "Graph\\"+title+ "_run_" + str(terT) + "times_average_reward"
#     csvname = "Graph\\Info\\"+title+ "_run_" + str(terT) + "times_average_reward"
#     Draw_Graph(valA,title,"times","average_reward",name,csvname)
#
#     name = "Graph\\" + title + "_run_" + str(terT) + "times_total_reward"
#     csvname = "Graph\\Info\\" + title + "_run_" + str(terT) + "times_total_reward"
#     Draw_Graph(tolRA,title,"times","total_reward",name,csvname)
#     print(e)
