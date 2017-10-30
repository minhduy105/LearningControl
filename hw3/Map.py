# Up, Right, Down, Left,Stay
import numpy as np

class Map():
    def __init__(self, info):
        self.data = np.asarray(info)
        self.value = np.zeros(self.data.shape)

    def Get_Reward(self,pos):
        reward = []
        repos = []
        (y,x) = self.data.shape
        self.value[pos[0]][pos[1]] =+ 1

        if pos[0] > 0: #UP
            reward.append(self.data[pos[0] - 1],[pos[1]])
        else:
            reward.append(-1000)
        repos.append([pos[0] - 1,pos[1]])

        if pos[1] < x-1: #RIGHT
            reward.append(self.data[pos[0],[pos[1]+1]])
        else:
            reward.append(-1000)
        repos.append([pos[0], pos[1]+1])

        if pos[0] < y-1:#DOWN
            reward.append([pos[0] + 1,pos[1]])
        else:
            reward.append(-1000)
        repos.append([pos[0] + 1,pos[1]])

        if pos[1] > 0:
            reward.append(self.data[pos[0], [pos[1] - 1]])
        else:
            reward.append(-1000)
        repos.append([pos[0], [pos[1] - 1]])

        reward.append(self.data[pos[0],pos[1]])
        repos.append(pos[0],pos[1])

        return reward,repos

    def Do_Action(self,e,pos):
        re,repos = self.Get_Reward(pos)

        return