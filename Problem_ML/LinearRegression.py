'''
    Problem [Easy]
     Machine Challenge

     In the Python file, write a script that will perform a linear regression on the data
     in data.txt and then calculate the coefficient of determination of the prediction.

     The first line in data.txt represents the X column, and the second line represents the Y column. \
     Your output should be in the following format:

        coefficient: 0.353412...

'''

from sklearn.linear_model import LinearRegression
import numpy as np
# import torch

data = np.loadtxt('data.txt', dtype=int)
X = data[0].reshape(-1,1)
Y = data[1]
lr = LinearRegression()
lr.fit(X,Y)
result = lr.score(X,Y)

print('coefficient: ' + str(result))

