import numpy as np
import  random
from Map import Map

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
            [locs] = np.asarray(np.where(reward == reward.max()))
        else:
            [locs] = np.asarray(np.where(reward != reward.max() & np.asarray(reR) > -100))
        loc = random.choice(locs)
        print (loc)
        print (reR[loc])
        print (dir[loc])
        st = dir[loc]

        dec.append(loc)
        i = i + 1
        #totalR = totalR + reward[loc]
        #val.append(reward[loc])
        #tolR.append(totalR)
    #return dec, val, tolR
    return dec

map =  np.genfromtxt('Map.csv', dtype=float, delimiter=',')
print (map)
M = Map(map)
#re, pos = M.Get_Reward([4,9]) #[y,x]
termT = 20
e = 0.01
a = 0.2
st = [3,3]
print (E_Greedy_Algorithm(termT, M, a, e,st))
#
# print (re)
# print (pos)