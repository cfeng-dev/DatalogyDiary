from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.datasets._samples_generator import make_classification
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt


# Example of scaling data with numpy
# a = np.array([[10, 2.7, 3.6], [-100, 5, -2], [120, 20, 40]], dtype=np.float64)
# print(a)
# print(preprocessing.scale(a))

X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2, random_state=22,
                           n_clusters_per_class=1, scale=100)
# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()

X = preprocessing.scale(X)  # Normalization (Standard)
# X = preprocessing.minmax_scale(X, feature_range=(-1,1))  # Normalization (Alternative)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = SVC()
clf.fit(X_train, y_train)  # Train Support Vector Machine classifier

print(f"Accuracy of the classifier after Normalization: {clf.score(X_test, y_test)}")
