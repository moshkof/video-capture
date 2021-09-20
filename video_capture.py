#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def run_analysis():
    unicode_text = u'перекресток маршала Говорова и Балтийская'
    cap = cv2.VideoCapture()
    # cap.open('rtsp://admin:P123456i@192.168.18.89:554')
    cap.open('http://94.72.19.56/mjpg/video.mjpg')
    # cap.open('https://youtu.be/NyygAOnP5nY')
    # print(cap.isOpened())
    if not cap.isOpened():
        print("Error opening video")

    while(cap.isOpened()):
        status, frame = cap.read()
        if status:
            cv2.imshow(unicode_text, frame)
        key = cv2.waitKey(25)
        if key == ord('q'):
            break


run_analysis()
