import sys
import cv2
import numpy as np

## Loading test images ############

img0 = cv2.imread('0.png', 0)
img1 = cv2.imread('1.png', 0)
img2 = cv2.imread('2.png', 0)
img3 = cv2.imread('3.png', 0)
img4 = cv2.imread('4.png', 0)
img5 = cv2.imread('5.png', 0)
img6 = cv2.imread('6.png', 0)
img7 = cv2.imread('7.png', 0)
img8 = cv2.imread('8.png', 0)
img9 = cv2.imread('9.png', 0)
img10 = cv2.imread('10.png', 0)

## Find countours of test images ##

ret, thresh0 = cv2.threshold(img0, 127, 255,0)
ret, thresh1 = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
ret, thresh3 = cv2.threshold(img3, 127, 255,0)
ret, thresh4 = cv2.threshold(img4, 127, 255,0)
ret, thresh5 = cv2.threshold(img5, 127, 255,0)
ret, thresh6 = cv2.threshold(img6, 127, 255,0)
ret, thresh7 = cv2.threshold(img7, 127, 255,0)
ret, thresh8 = cv2.threshold(img8, 127, 255,0)
ret, thresh9 = cv2.threshold(img9, 127, 255,0)
ret, thresh10 = cv2.threshold(img10, 127, 255,0)

contours,hierarchy = cv2.findContours(thresh0,2,1)
cnt0 = contours[0]
contours,hierarchy = cv2.findContours(thresh1,2,1)
cnt1 = contours[0]
contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]
contours,hierarchy = cv2.findContours(thresh3,2,1)
cnt3 = contours[0]
contours,hierarchy = cv2.findContours(thresh4,2,1)
cnt4 = contours[0]
contours,hierarchy = cv2.findContours(thresh5,2,1)
cnt5 = contours[0]
contours,hierarchy = cv2.findContours(thresh6,2,1)
cnt6 = contours[0]
contours,hierarchy = cv2.findContours(thresh7,2,1)
cnt7 = contours[0]
contours,hierarchy = cv2.findContours(thresh8,2,1)
cnt8 = contours[0]
contours,hierarchy = cv2.findContours(thresh9,2,1)
cnt9 = contours[0]
contours,hierarchy = cv2.findContours(thresh10,2,1)
cnt10 = contours[0]

## Now match shapes ###############

while (0 == 0):
    infile = raw_input('Filename: ')
    if infile == 'QUIT':
        break
    img = cv2.imread(infile, 0)
    if img is None:
        print('File not found.')
        continue
    #imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #set gray
    edges = cv2.Canny(img, 125, 3*125) #canny edge
    ret, thresh = cv2.threshold(edges, 127, 255,0)
    contours,hierarchy = cv2.findContours(thresh,2,1)
    if len(contours) == 0:
        ret, thresh = cv2.threshold(img, 127, 255,0)
        contours,hierarchy = cv2.findContours(thresh,2,1)
    cnt = contours[0]
    ret = cv2.matchShapes(cnt,cnt0,1,0.0)
    retmain = ret
    shapebest = 'circle'
    ret = cv2.matchShapes(cnt,cnt1,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'cross'
    ret = cv2.matchShapes(cnt,cnt2,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'diamond'
    ret = cv2.matchShapes(cnt,cnt3,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'hexagon'
    ret = cv2.matchShapes(cnt,cnt4,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'parallelogram'
    ret = cv2.matchShapes(cnt,cnt5,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'rhombus'
    ret = cv2.matchShapes(cnt,cnt6,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'semicircle'
    ret = cv2.matchShapes(cnt,cnt7,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'square'
    ret = cv2.matchShapes(cnt,cnt8,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'star'
    ret = cv2.matchShapes(cnt,cnt9,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'trapezoid'
    ret = cv2.matchShapes(cnt,cnt10,1,0.0)
    if ret < retmain:
        retmain = ret
        shapebest = 'triangle'
    print retmain
    print shapebest
