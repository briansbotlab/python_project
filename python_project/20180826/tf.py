# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 21:06:07 2018

@author: superuser
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
 
if __name__ == "__main__":
    #设置参数
    #设置梯度下降算法的学习率
    learning_rate = 0.1
    #设置迭代次数
    max_steps = 1000
    #每迭代100次输出一次loss
    show_step = 100
    # 模拟训练数据
    train_X = np.asarray([3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
                             7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1])
    train_Y = np.asarray([1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221,
                             2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3])
    #获取训练数据的大小
    n_samples = train_X.shape[0]
    #定义输入变量,变量只有一个特征
    X = tf.placeholder(dtype=tf.float32)
    #定义输出变量,输出只有一个值
    Y = tf.placeholder(dtype=tf.float32)
 
    #设计模型
    #定义权重
    rng = np.random
    W = tf.Variable(rng.randn(),name="weight")
    #定义偏置
    b = tf.Variable(rng.randn(),name="bias")
    #计算预测值
    pred = tf.add(tf.multiply(X,W),b)
 
    #定义损失函数
    loss = 0.5 * tf.reduce_sum(tf.pow(pred-Y,2)) / n_samples
    #使用梯度下降算法来优化损失函数
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
 
    #创建一个会话
    with tf.Session() as sess:
        # 初始化所有变量
        initialize = tf.global_variables_initializer().run()
        #迭代训练
        for step in range(max_steps):
            for (x,y) in zip(train_X,train_Y):
                sess.run(train_step,feed_dict={X:x,Y:y})
            if step % show_step == 0:
                #计算模型在数据集上的损失
                step_loss = sess.run([loss],feed_dict={X:train_X,Y:train_Y})
                print("step:",step,"-step loss:%.4f",step_loss)
        #计算最终的Loss
        train_loss = sess.run([loss],feed_dict={X:train_X,Y:train_Y})
        print("train loss:%.4f",train_loss)
        #输出参数
        print("weights:",sess.run(W),"-bias:",sess.run(b))
        plt.plot(train_X,train_Y,"ro",label="original data")
        plt.plot(train_X,sess.run(pred,feed_dict={X:train_X}),label="predict data")
        plt.legend(loc="upper left")
        plt.show()
 
        #测试数据
        test_X = np.asarray([0.8,1.2,8,1.3,1.1,0.6])
        test_Y = np.asarray([3,2.5,0.2,2.8,2.7,3.5])
        #计算回归模型在测试数据上的loss
        print("test loss:%.4f",sess.run(loss,feed_dict={X:test_X,Y:test_Y}))
        #绘图
        plt.plot(test_X,test_Y,"bo",label="test data")
        plt.plot(test_X,sess.run(pred,feed_dict={X:test_X}),label="predict test")
        plt.legend(loc="upper left")
        plt.show()
