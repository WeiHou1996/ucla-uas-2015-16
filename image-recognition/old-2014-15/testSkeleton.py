import sys
import cv2
import numpy as np

infile = raw_input('Filename: ')

img = cv2.imread(infile)
if img is None:
    print('File not found.')
    sys.exit(404)

#Write code here###########

#Try to use a color threshhold here first just to see what happens?
#thresh = 125 #canny thresh
#imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #set gray
#edges = cv2.Canny(img, 125, 3*125) #canny edge
#ret,thresh = cv2.threshold(imgray,127,255,0) #contour threshold

#contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours
#cv2.drawContours(imgray, contours, -1, (255,0,0), 3) #draws contours

###########################
    
#cv2.imshow('Picture',edges) #Change img to whatever image you want displayed.
#cv2.waitKey(0)
#cv2.destroyAllWindows()

###########################

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #set gray
ret,thresh = cv2.threshold(imgray,127,255,0) #contour threshold
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #find contours
cv2.drawContours(imgray, contours, -1, (255,0,0), 3) #draws contours
print str(contours)[1:-1]
