'''
爱生活，爱......
-- coding: UTF-8  --
@Time : 2022/2/19 14:31
@Author : Xianyang
@Email : xy_mts@163.com
@File : Train_Model.py
@Software: PyCharm
♡♡♡---Beauty is about to begin...
'''
# %% 导入相关库

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import numpy as np
import cv2
from sklearn.utils import shuffle

# %% 读取Dataset中训练集图像

loadedImages = []
for i in range(0, 1000):
    image = cv2.imread('Dataset/Zero_Train/zero_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    loadedImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 1000):
    image = cv2.imread('Dataset/One_Train/one_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    loadedImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 1000):
    image = cv2.imread('Dataset/Two_Train/two_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    loadedImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 1000):
    image = cv2.imread('Dataset/Three_Train/three_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    loadedImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 1000):
    image = cv2.imread('Dataset/Four_Train/four_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    loadedImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 1000):
    image = cv2.imread('Dataset/Five_Train/five_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    loadedImages.append(gray_image.reshape(89, 100, 1))
# %% 创建输出向量

outputVectors = []
for i in range(0, 1000):
    outputVectors.append([1, 0, 0, 0, 0, 0])

for i in range(0, 1000):
    outputVectors.append([0, 1, 0, 0, 0, 0])

for i in range(0, 1000):
    outputVectors.append([0, 0, 1, 0, 0, 0])

for i in range(0, 1000):
    outputVectors.append([0, 0, 0, 1, 0, 0])

for i in range(0, 1000):
    outputVectors.append([0, 0, 0, 0, 1, 0])

for i in range(0, 1000):
    outputVectors.append([0, 0, 0, 0, 0, 1])

# %% 读取Dataset中测试集图像

testImages = []
for i in range(0, 100):
    image = cv2.imread('Dataset/Zero_Test/zero_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    testImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 100):
    image = cv2.imread('Dataset/One_Test/one_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    testImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 100):
    image = cv2.imread('Dataset/Two_Test/two_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    testImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 100):
    image = cv2.imread('Dataset/Three_Test/three_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    testImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 100):
    image = cv2.imread('Dataset/Four_Test/four_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    testImages.append(gray_image.reshape(89, 100, 1))

for i in range(0, 100):
    image = cv2.imread('Dataset/Five_Test/five_' + str(i) + '.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    testImages.append(gray_image.reshape(89, 100, 1))
# %% 创建测试集标签

testLabels = []
for i in range(0, 100):
    testLabels.append([1, 0, 0, 0, 0, 0])

for i in range(0, 100):
    testLabels.append([0, 1, 0, 0, 0, 0])

for i in range(0, 100):
    testLabels.append([0, 0, 1, 0, 0, 0])

for i in range(0, 100):
    testLabels.append([0, 0, 0, 1, 0, 0])

for i in range(0, 100):
    testLabels.append([0, 0, 0, 0, 1, 0])

for i in range(0, 100):
    testLabels.append([0, 0, 0, 0, 0, 1])

# %% 定义一个cnn网络
'''使用9层的卷积网络,卷积核大小为2，激活层为relu，每个卷积层后接maxpool层，最后设置两层全连接层'''
tf.reset_default_graph()
x = input_data(shape=[None, 89, 100, 1], name='input')

conv1 = conv_2d(x, 32, 2, activation='relu')
pool1 = max_pool_2d(conv1, 2)

conv2 = conv_2d(pool1, 64, 2, activation='relu')
pool2 = max_pool_2d(conv2, 2)

conv3 = conv_2d(pool2, 128, 2, activation='relu')
pool3 = max_pool_2d(conv3, 2)

conv4 = conv_2d(pool3, 256, 2, activation='relu')
pool4 = max_pool_2d(conv4, 2)

conv5 = conv_2d(pool4, 256, 2, activation='relu')
pool5 = max_pool_2d(conv5, 2)

conv6 = conv_2d(pool5, 128, 2, activation='relu')
pool6 = max_pool_2d(conv6, 2)

conv7 = conv_2d(pool6, 64, 2, activation='relu')
pool7 = max_pool_2d(conv7, 2)

full1 = fully_connected(pool7, 1000, activation='relu')
convnet = dropout(full1, 0.75)

full2 = fully_connected(convnet, 6, activation='softmax')
convnet = regression(full2, optimizer='adam', learning_rate=0.001, loss='categorical_crossentropy', name='regression')


model = tflearn.DNN(convnet, tensorboard_verbose=0)


# %% 打乱训练集次序
loadedImages, outputVectors = shuffle(loadedImages, outputVectors, random_state=0)

# %% 训练
model.fit(loadedImages, outputVectors, n_epoch=50,
          validation_set=(testImages, testLabels),
          snapshot_step=100, show_metric=True, run_id='convnet_coursera')

# %% 保存模型
model.save("TrainedModel/GestureRecogModel.tfl")



