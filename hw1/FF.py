from __future__ import division
from __future__ import print_function
import sys

import numpy as np
import random
import csv

class LinearTransform(object):
    def forward(self, x, W):
        return x.dot(W)  # the dimension is different so that I do not need to do transpose

    # DEFINE forward function

    # grad_output is dz3, x is z2
    def backwardW(self, dz2, z1, old_dW, W, learning_rate, momentum, l2_penalty):
        grad = (z1.T).dot(dz2)
        dW = momentum * old_dW - learning_rate * (grad + l2_penalty * W)
        return dW

    def backwardz(self, dz2, W):
        dz1 = (dz2).dot(W.T)
        return dz1
        # DEFINE backward function
        # ADD other operations in LinearTransform if needed

# This is a class for a sigmoid layer followed by a cross entropy layer, the reason
# this is put into a single layer is because it has a simple gradient form
class Sigmoid(object):

    def forward(self, z1):
        z2 = 1.0 / (1.0 + np.exp(-z1))
        return z2

    # DEFINE forward function

    def backward(self,e, y):
        yN = np.multiply(y,(1.0 - y.astype(float)))
        dz = np.multiply(e,yN)
        return dz
        # DEFINE backward function
        # ADD other operations and data entries in SigmoidCrossEntropy if needed

class Error(object):
    def forward (self,y,z):
        return y - z

    def backward(self,z):
        return -1*z

class MSE(object):
    def forward(self,z):
        return np.sum(np.square(z))


class MLP(object):
    def train(self, x_batch, y_batch, learning_rate, momentum, l2_penalty, model, model_old):
        #	For initiate the W and b
        W1, W2 = model['W1'], model['W2']
        old_dW1, old_dW2 = model_old['dW1'], model_old['dW2']

        lt1 = LinearTransform()
        sce1 = Sigmoid()
        lt2 = LinearTransform()
        err = Error()
        mse = MSE()
        z1 = lt1.forward(x_batch,W1)
        z2 = lt2.forward(z1, W2)
        z3 = sce1.forward(z2)
        z4 = err.forward(y_batch,z3)
        z5 = mse.forward(z4)

        dz5 = z4
        dz4 = err.backward(dz5)
        dz3 = sce1.backward(dz4,z3)
        dW2 = lt2.backwardW(dz3, z1, old_dW2, W2, learning_rate, momentum, l2_penalty)
        dz2 = lt2.backwardz(dz3,W2)
        dW1 = lt1.backwardW(dz2, x_batch, old_dW1, W1, learning_rate, momentum, l2_penalty)

        W1 = W1 + dW1
        W2 = W2 + dW2

        model_out = {'W1': W1, 'W2': W2}
        model_old_out = {'dW1': dW1, 'dW2': dW2}

        return z5, model_out, model_old_out

    # INSERT CODE for training the network

    def evaluate(self, x, y, model):
        W1, W2 = model['W1'], model['W2']
        lt1 = LinearTransform()
        sce1 = Sigmoid()
        lt2 = LinearTransform()
#        err = Error()

        z1 = lt1.forward(x,W1)
        z2 = lt2.forward(z1, W2)
        z3 = sce1.forward(z2)


        result = (z3 > 0.5).astype(float)
        actual = (y > 0.5).astype(float)
        err = np.absolute(result - actual).astype(float)

        return np.sum(err) / len(err)
def print_matrix(data, name):
	with open( name +".csv", "w") as t:
		writer = csv.writer(t)
		writer.writerows(data)

if __name__ == '__main__':

    trainName = ['train1','train2']
    testName = ['test1','test2','test3']
    for tr in trainName:
        train = np.genfromtxt(tr+'.csv', delimiter=',')
        #    train2 = np.genfromtxt('train2.csv',delimiter=',')
        #    train = np.append(train1,train2,axis=0)
        train_x = train[:, :5]
        train_y = train[:, 5:6]
        print (train)

        # add the constant term 'b' into train set
        b = np.ones(len(train_x), dtype=np.float64).reshape(len(train_x), 1)
        train_in_x = np.append(train_x, b, 1) / 255.0

        for t in testName:
            test = np.genfromtxt(t+'.csv', delimiter=',')
            test_x = test[:, :5]
            test_y = test[:, 5:6]
            # add the constant term 'b' into test set
            b = np.ones(len(test_x)).reshape(len(test_x), 1)
            test_in_x = np.append(test_x, b, 1) / 255.0

            data_train = []  # putting data
            data_test = []
            for mo in range(10):  # use this to test on different variable (batch size, hidden units, etc)
                ep_train = []  # epoch count
                ep_test = []  # epoch count

                hidden_units = 50

                # create space to store W1 and dW (for momentum)
                num_examples, input_dims = train_in_x.shape

                W1 = np.random.randn(input_dims, hidden_units) / 10.0
                W2 = np.random.randn(hidden_units, 1) / 10.0

                model = {'W1': W1, 'W2': W2}

                dW1 = np.zeros_like(W1, dtype=np.float64)
                dW2 = np.zeros_like(W2, dtype=np.float64)

                model_old = {'dW1': dW1, 'dW2': dW2}

                # # INSERT YOUR CODE HERE
                # # YOU CAN CHANGE num_epochs AND num_batches TO YOUR DESIRED VALUES
                num_epochs = 500  # 10
                num_batches = 1000
                batches_size = 100
                learning_rate = 0.0008
                momentum = 0.7
                l2_penalty = 0.0002 * mo
                mlp = MLP()
                helper = np.concatenate((train_in_x, train_y), axis=1)

                np.random.shuffle(helper)

                for epoch in range(num_epochs):
                    # # INSERT YOUR CODE FOR EACH EPOCH HERE

                    for b in range(num_batches):
                        # MINI BATCH
                        k = random.randint(0, num_examples - batches_size - 1)

                        batches = helper[range(k, k + batches_size)]
                        x_batch = batches[:, range(input_dims)]
                        y_batch = batches[:, input_dims].reshape(batches_size, 1)

                        total_loss = 0.0

                        mse, model, model_old = mlp.train(x_batch, y_batch, learning_rate, momentum, l2_penalty, model, model_old)

                    if epoch%10 == 0:
                        print(
                            '\r[Epoch {}, mb {}]    MSE = {:.3f}'.format(
                                epoch + 1,
                                b + 1,
                                mse,
                            ),
                            end='',
                        )
                        sys.stdout.flush()

                        #acc = (1.0 - mlp.evaluate(train_in_x, train_y, model)) * 100.0
                        #ep_train.append(acc)

                        acc = (1.0 - mlp.evaluate(test_in_x, test_y, model)) * 100.0
                        ep_test.append(acc)
                        sys.stdout.flush()

                data_train.append(ep_train)
                data_test.append(ep_test)

                print ("Done")
                #print_matrix(data_train, "result_for_train_set_"+tr+"_HU_"+str(hidden_units)+"_LR_"+str(learning_rate)+"_MOM_"+str(momentum)+"_L2P_"+str(l2_penalty))
                print_matrix(data_test, "result_"+t+"_in_train_"+tr+"_HU_"+str(hidden_units)+"_LR_"+str(learning_rate)+"_MOM_"+str(momentum)+"_L2P_"+str(l2_penalty))

