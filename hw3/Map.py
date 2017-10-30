# Up, Right, Down, Left,Stay
import numpy as np
import random
class Map():
    def __init__(self, info):
        self.data = info
        self.value = np.zeros(self.data.shape)

    def Get_Reward(self,pos):
        reward = []
        repos = []
        (y,x) = self.data.shape

        if pos[0] > 0: #UP
            reward.append(self.data[pos[0] - 1][pos[1]])
        else:
            reward.append(-10)
        repos.append([pos[0] - 1,pos[1]])

        if pos[1] < x-1: #RIGHT
            reward.append(self.data[pos[0]][pos[1]+1])
        else:
            reward.append(-10)
        repos.append([pos[0], pos[1]+1])

        if pos[0] < y-1:#DOWN
            reward.append(self.data[pos[0] + 1][pos[1]])
        else:
            reward.append(-10)
        repos.append([pos[0] + 1,pos[1]])

        if pos[1] > 0:
            reward.append(self.data[pos[0]][pos[1] - 1])
        else:
            reward.append(-10)
        repos.append([pos[0], pos[1] - 1])

        reward.append(self.data[pos[0]][pos[1]])
        repos.append([pos[0],pos[1]])

        return reward,repos

    def UpdateMap(self,info):
        self.data = info