
import numpy as np

def Get_Distance (A,B): #get distance between two points
    return np.sqrt(np.square(np.abs(A[0] - B[0])) + np.square(np.abs(A[1] - B[1])))

def Get_Total_Distance(Cities):# get total distance from a path
    total_distance = 0
    num_cities = Cities.shape[0]
    for i in range (num_cities - 1):
        total_distance = total_distance + Get_Distance(Cities[i],Cities[i+1])
    total_distance = total_distance + Get_Distance(Cities[0],Cities[num_cities - 1])
    return total_distance