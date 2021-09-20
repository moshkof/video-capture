#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def run_analysis():
    # cap = cv2.VideoCapture('https://camera.rt.ru/66ca723a-c024-4877-b279-f7db9189931d')
    # font_size=14
    # font_color=(0,0,0)
    # unicode_font = ImageFont.truetype("Arial.ttf", font_size)
    unicode_text = u'перекресток маршала Говорова и Балтийская'
    cap = cv2.VideoCapture()
    cap.open('rtsp://admin:P123456i@192.168.18.21')
    # cap.open('rtsp://admin:P54321k@192.168.18.38')

    if not cap.isOpened():
        print("Error opening video")

    while(cap.isOpened()):
        status, frame = cap.read()
        if status:
            cv2.imshow(unicode_text, frame)
            # draw  =  ImageDraw.Draw ( cap )
            # draw.text ( (10,10), unicode_text, font=unicode_font, fill=font_color )
            # do_stuff_with_frame(frame)
        key = cv2.waitKey(25)
        if key == ord('q'):
            break

run_analysis()
