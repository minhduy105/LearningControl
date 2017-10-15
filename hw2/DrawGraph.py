
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    t0 = 1000000
    tmin = 0.1**(15)
    alpha = 0.95
    st = 1
    name = '15cities.csv'
    data = np.genfromtxt(name, delimiter=',')
    data = np.delete(data, (0), axis=0)

    data =np.append(data,data[0].reshape((1, 2)),axis=0)
    x = data[:, 0]
    y = data[:, 1]
    plt.figure()
    plt.plot(x, y,'ro-')
    plt.show()