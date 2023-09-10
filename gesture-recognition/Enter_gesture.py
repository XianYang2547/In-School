'''
爱生活，爱......
-- coding: UTF-8  --
@Time : 2022/2/17 20:30
@Author : Xianyang
@Email : xy_mts@163.com
@File : Enter_gesture.py
@Software: PyCharm
♡♡♡---Beauty is about to begin...
'''

import cv2
import imutils
from PIL import Image

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


# 开启摄像头
camera = cv2.VideoCapture(0)


def main():
    # 参数设置
    # 初始化运行平均值的权重
    aWeight = 0.5
    # 设置roi区域
    top, right, bottom, left = 10, 350, 225, 590
    # 初始化帧数和图片数量
    num_frames, image_num = 0, 0
    start_recording = False

    while (True):
        # 获取当前帧
        (grabbed, frame) = camera.read()
        if (grabbed == True):
            # 调整帧大小
            frame = imutils.resize(frame, width=700)
            # 调整显示，不然的话是镜像显示
            frame = cv2.flip(frame, 1)
            # 克隆一下
            clone = frame.copy()
            # # 得到帧的高宽
            # (height, width) = frame.shape[:2]
            # 取ROI
            roi = frame[top:bottom, right:left]
            # 将roi区域灰度化和模糊
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)

            if num_frames < 30:
                run_avg(gray, aWeight)
            else:
                # 分割手部区域
                hand = segment(gray)
                # 检查手部区域是否被分割
                if hand is not None:
                    # 如果是，解包阈值图像和分割区域
                    (thresholded, segmented) = hand
                    # 绘制分段区域并显示框架
                    cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
                    if start_recording:
                        imageName = "Dataset/Zero_Test/zero_" + str(image_num) + '.png'
                        cv2.imwrite(imageName, thresholded)  # 储存
                        resizeImage(imageName)  # 再resize
                        image_num += 1
                    cv2.imshow("Thesholded", thresholded)

            # 绘出分割图
            cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)

            # 帧数+1
            num_frames += 1

            # 显示
            cv2.imshow("Video Feed", clone)

            # 响应按键
            keypress = cv2.waitKey(1) & 0xFF

            # q退出，s开始
            if keypress == ord("q") or image_num > 99:
                break

            if keypress == ord("s"):
                start_recording = True

        else:
            print("camera broken")
            break


main()

# 释放摄像头、关闭窗口
camera.release()
cv2.destroyAllWindows()
