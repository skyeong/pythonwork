import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import multivariate_normal, permutation
import pandas as pd
from pandas import DataFrame, Series

import sys
sys.path.append('/Users/skyeong/pythonwork/delirium')
import TF4Neuro

neuro = TF4Neuro()
neuro.insert_data('/Users/skyeong/data/delirium/Results/delirium_network_n116.csv')

# a=pd.read_csv('/Users/skyeong/data/delirium/Results/CSV_matrix/roi_n116/rest2/network_N01_LYK.csv', sep=',')

# df0 = generate_datablock(15, [7,7],   22, 0)
# df1 = generate_datablock(15, [22,7],  22, 0)
# df2 = generate_datablock(15, [7,22],  22, 0)
# df3 = generate_datablock(15, [20,20], 22, 1)

# df = pd.concat([df0, df1, df2, df3], ignore_index=True)
# train_set = df.reindex(permutation(df.index)).reset_index(drop=True)

# train_x = train_set[['x1','x2']].as_matrix()
# train_t = train_set['t'].as_matrix().reshape([len(train_set),1])

# num_units = 2  # define number of nodes in hidden layer
# mult = train_x.flatten().mean()

# x = tf.placeholder(tf.float32, [None, 2])

# w1 = tf.Variable(tf.truncated_normal([2, num_units]))  # initialize using random normal distribution
# b1 = tf.Variable(tf.zeros([num_units]))
# hidden1 = tf.nn.tanh(tf.matmul(x,w1) + b1*mult)  # *mult is to boost speed

# w0 = tf.Variable(tf.zeros([num_units, 1]))
# b0 = tf.Variable(tf.zeros([1]))
# p = tf.nn.sigmoid(tf.matmul(x,w1)+b0*mult)


# # Error function
# t = tf.placeholder(tf.float32, [None,1])
# loss = -tf.reduce_sum(t*tf.log(p) + (1-t)*tf.log(1-p))
# train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
# correct_prediction = tf.equal(tf.sign(p-0.5), tf.sign(t-0.5))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# sess = tf.InteractiveSession()
# sess.run(tf.global_variables_initializer())


# # Training Step
# i=0
# for _ in range(1000):
#     i += 1
#     sess.run(train_step, feed_dict={x:train_x, t:train_t})
#     if i% 100 == 0:
#         loss_val, acc_val = sess.run([loss,accuracy], feed_dict={x:train_x, t:train_t})
#         print('Step: %d, Loss: %f, Accuracy: %f' % (i, loss_val, acc_val) )
