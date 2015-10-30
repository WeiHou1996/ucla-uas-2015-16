import sys
import cv2
import numpy as np

infile = raw_input('Filename 1: ')

img1 = cv2.imread(infile, 0)
if img1 is None:
    print('File not found.')
    sys.exit(404)

###########################

infile = raw_input('Filename 2: ')

img2 = cv2.imread(infile, 0)
if img2 is None:
    print('File not found.')
    sys.exit(404)

#Write code here###########

#imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #set gray

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print ret
