import numpy as np

class ArmBanbit():
    def __init__(self,data):
        self.info = np.asarray(data)
    def Get_Reward(self):
        value = np.zeros(self.info.shape[0])
        for i in range (self.info.shape[0]):
            value[i] = np.random.normal(self.info[i][0], self.info[i][1])
        return value

