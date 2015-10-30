import sys
import cv2
import numpy as np

infile = raw_input('Filename 1: ')

cnt1 = np.loadtxt(infile)
if cnt1 is None:
    print('File not found.')
    sys.exit(404)

###########################

infile = raw_input('Filename 2: ')

cnt2 = np.loadtxt(infile)
if cnt2 is None:
    print('File not found.')
    sys.exit(404)

#Write code here###########

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print ret
