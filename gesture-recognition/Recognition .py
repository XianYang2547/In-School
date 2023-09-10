'''
爱生活，爱......
-- coding: UTF-8  --
@Time : 2022/2/20 20:30
@Author : Xianyang
@Email : xy_mts@163.com
@File : Recognition.py
@Software: PyCharm
♡♡♡---Beauty is about to begin...
'''
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import numpy as np
from PIL import Image
import cv2
import imutils

bg = None


def resizeImage(imageName):
    # 原录入图片是240*215，转为100*89
    basewidth = 100
    img = Image.open(imageName)
    wpercent = (basewidth / float(img.size[0]))  # 100/240=0.417
    hsize = int((float(img.size[1]) * float(wpercent)))  # 215*0.417=89
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)  # resize(100,89)
    img.save(imageName)


def run_avg(image, aWeight):
    global bg
    # 初始化背景
    if bg is None:
        bg = image.copy().astype("float")
        return

    cv2.accumulateWeighted(image, bg, aWeight)


def segment(image, threshold=8):
    global bg
    # 找到背景和当前帧之间的绝对差异
    diff = cv2.absdiff(bg.astype("uint8"), image)

    # 阈值差异图像，以便我们获得前景
    thresholded = cv2.threshold(diff,
                                threshold,
                                255,
                                cv2.THRESH_BINARY)[1]

    # 获取阈值图像中的轮廓
    (cnts, _) = cv2.findContours(thresholded.copy(),
                                 cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) == 0:
        return
    else:
        # 根据轮廓面积，得到最大轮廓
        segmented = max(cnts, key=cv2.contourArea)
        return (thresholded, segmented)


# 实时手势识别，依赖训练好的模型，上面三个函数必须在Recognition.py中定义存在，
# 而不能从Enter_gesture.py中调用，否则会出现运行bug，造成卡顿。


def getPredictedClass():
    "预测"
    image = cv2.imread('Temp.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    prediction = model.predict([gray_image.reshape(89, 100, 1)])
    return np.argmax(prediction), (np.amax(prediction) / (
                prediction[0][0] + prediction[0][1] + prediction[0][2] + prediction[0][3] + prediction[0][4] +
                prediction[0][5]))


def showStatistics(predictedClass, confidence):
    "识别判断和窗口文字显示"
    textImage = np.zeros((300, 512, 3), np.uint8)
    className = ""
    # 识别判断
    if predictedClass == 0:
        className = "This is Zero"
    elif predictedClass == 1:
        className = "This is One"
    elif predictedClass == 2:
        className = "This is Two"
    elif predictedClass == 3:
        className = "This is Three"
    elif predictedClass == 4:
        className = "This is Four"
    elif predictedClass == 5:
        className = "This is Five"

    # 窗口文字显示
    cv2.putText(textImage, "Pedicted Class : " + className,
                (30, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2)

    cv2.putText(textImage, "Confidence : " + str(confidence * 100) + '%',
                (30, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2)

    cv2.putText(textImage, "Hi Fuck Man",
                (180, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2)
    cv2.putText(textImage, "Look Here",
                (200, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2)
    cv2.imshow("Windows", textImage)


def main():
    # 初始化运行平均值的权重
    aWeight = 0.5
    # 调用摄像头
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # 设置roi区域
    top, right, bottom, left = 10, 350, 225, 590
    # 初始化帧数
    num_frames = 0
    # 开始标志
    start_recording = False

    while (True):
        # 获取当前帧
        (grabbed, frame) = camera.read()
        # 调整帧大小
        frame = imutils.resize(frame, width=700)
        # 调整显示，不然的话是镜像显示
        frame = cv2.flip(frame, 1)
        # 克隆一下
        clone = frame.copy()
        # 得到帧的高宽
        (height, width) = frame.shape[:2]
        # 取ROI
        roi = frame[top:bottom, right:left]
        # 将roi区域灰度化和模糊
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        if num_frames < 30:
            run_avg(gray, aWeight)  # 调用Enter_gesture在的run_avg函数
        else:
            # 分割手部区域
            hand = segment(gray)

            # 检查手部区域是否被分割
            if hand is not None:
                # 如果是，解包阈值图像和分割区域
                (thresholded, segmented) = hand
                cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
                if start_recording:
                    cv2.imwrite('Temp.png', thresholded)
                    resizeImage('Temp.png')
                    predictedClass, confidence = getPredictedClass()  # 调用预测函数，返回的值传入
                    showStatistics(predictedClass, confidence)  # showStatistics来进行识别判断和窗口文字显示
                cv2.imshow("Thesholded", thresholded)

        # 绘出分割图
        cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)

        # 帧数+1
        num_frames += 1

        # 显示
        cv2.imshow("Video Feed", clone)

        # 响应按键
        keypress = cv2.waitKey(1) & 0xFF

        if keypress == ord("q"):
            break
        if keypress == ord("s"):
            start_recording = True


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

# 加载模型
model.load("TrainedModel/GestureRecogModel.tfl")

main()
