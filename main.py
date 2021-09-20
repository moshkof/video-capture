#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2


def run_analysis():
    # cap = cv2.VideoCapture('https://camera.rt.ru/66ca723a-c024-4877-b279-f7db9189931d')
    cap = cv2.VideoCapture()
    cap.open('rtsp://admin:P123456i@192.168.18.21')

    if not cap.isOpened():
        print("Error opening video")

    while(cap.isOpened()):
        status, frame = cap.read()
        if status:
            cv2.imshow('перекресток маршала Говорова и Балтийская', frame)
            # do_stuff_with_frame(frame)
        key = cv2.waitKey(25)
        if key == ord('q'):
            break


run_analysis()
