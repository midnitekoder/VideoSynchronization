import numpy as np
import cv2

cap1 = cv2.VideoCapture('testVideo.mp4')
cap2 = cv2.VideoCapture('testVideo2.mp4')

fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
out1 = cv2.VideoWriter('outputTempVideo1.avi', fourcc, 24, (1280,720), True)
out2 = cv2.VideoWriter('outputTempVideo4.avi', fourcc, 24, (1280,720), True)

count=0
while(cap1.isOpened()):
	if count<100:
		ret1,frame11=cap1.read()
		count=count+1
		print count
	else:
		break
if(cap1.isOpened()):
	ret1, frame11=cap1.read()
cap1.release()

if(cap2.isOpened()):
	ret2, frame12 = cap2.read()
cap2.release()

for j in range(2):
	for i in range(24):
		out1.write(frame11)
	for i in range(24):
		out1.write(frame12)

for j in range(2):
	for i in range(48):
		out2.write(frame11)
	for i in range(48):
		out2.write(frame12)



out1.release()
out2.release()
cv2.destroyAllWindows()
