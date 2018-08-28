# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:55:04 2018

@author: superuser
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

iris = datasets.load_iris()

X = iris.data[:,:2]

y = iris.target

model = svm.SVC(kernel='rbf', C =1 ,gamma =1)

model.fit(X,y)


x_min, x_max =X[:, 0].min() - 1,X[:,0].max() + 1
y_min, y_max =X[:, 1].min() - 1,X[:,1].max() + 1


xx,yy = np.meshgrid(np.arange(x_min, x_max,1),
                    np.arange(y_min, y_max,1))

plt.subplot(1,1,1)

Z = model.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

plt.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.Paired)
plt.xlabel("Sepal length")
plt.ylabel('Sepal width')
plt.xlim(xx.min(),xx.max())
plt.title('SVC with linear kernel')
plt.show()


