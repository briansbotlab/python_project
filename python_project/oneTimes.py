import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))

y = W * x_data + b

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.2)

train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()

sess.run(init)

for step in range(301):
    sess.run(train)
    
    if step % 10 == 0:
        print(step, sess.run(W), sess.run(b))
        
        plt.plot(x_data, y_data, 'ro', label = 'Original data')
        
        plt.plot(x_data, sess.run(W) * x_data + sess.run(b), label = 'Fitted line')
        
        plt.legend()
        
        plt.show()