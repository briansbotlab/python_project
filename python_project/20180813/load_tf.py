# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:10:18 2018

@author: admin
"""

import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays


import numpy as np
import matplotlib.pyplot as plt

from keras.models import model_from_json

mnist = tf.keras.datasets.mnist  # mnist is a dataset of 28x28 images of handwritten digits and their labels
(x_train, y_train),(x_test, y_test) = mnist.load_data()  # unpacks images to x_train/x_test and labels to y_train/y_test

x_test = tf.keras.utils.normalize(x_test, axis=1)  # scales data between 0 and 1
x_train = tf.keras.utils.normalize(x_train, axis=1)  # scales data between 0 and 1   

model = tf.keras.models.Sequential()  # a basic feed-forward model
'''
model.add(tf.keras.layers.Flatten())  # takes our 28x28 and makes it 1x784
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # our output layer. 10 units for 10 classes. Softmax for probability distribution
'''


model.load_weights('test.h5',by_name=True)
json_string = model.to_json()
new_model = model_from_json(json_string)


    
#new_model = tf.keras.models.load_model('epic_num_reader.h5')
    
  
predictions = new_model.predict(x_test)

#print(predictions)

print(np.argmax(predictions[0]))

plt.imshow(x_test[0],cmap = plt.cm.binary)
plt.show()

