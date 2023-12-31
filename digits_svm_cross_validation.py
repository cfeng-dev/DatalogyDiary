import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import learning_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC

digits = load_digits()
X = digits.data
y = digits.target

# SVM classifier
train_sizes, train_loss, test_loss = learning_curve(SVC(gamma=0.001), X, y, cv=10, scoring='neg_mean_squared_error',
                                                    train_sizes=[0.1, 0.25, 0.5, 0.75, 1])
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

plt.plot(train_sizes, train_loss_mean, 'o-',color='r',label='training')
plt.plot(train_sizes, test_loss_mean, 'o-',color='g',label='cross validation')
plt.xlabel("Training examples")
plt.ylabel("Loss")
plt.legend(loc="best")
plt.show()
