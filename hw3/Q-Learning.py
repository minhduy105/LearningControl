import numpy as np
import random

class QLearning():
    def __init__(self, info):
        self.data = np.asarray(info)
        self.value = np.zeros(self.data.shape)

    def Policy (self,data,prev,reward):
        [TF] = random.choices([True, False], weights=[1.0 - e, e])
        if TF:
            [locs] = np.asarray(np.where(reward == reward.max()))
        else:
            [locs] = np.asarray(np.where(reward != reward.max()))
