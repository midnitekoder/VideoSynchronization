import numpy as np
import cv2
from matplotlib import pyplot as plt
from kdTreeNNeighbors import createM


orb = cv2.ORB()
cap = cv2.VideoCapture('testVideo3.mp4')
keypointsVideo1=[]
frameNumber=1
while(cap.isOpened()):
	try:
		ret, frame = cap.read()
		#print frame
		kp = orb.detect(frame,None)
		#print kp
		kp, des1 = orb.compute(frame, kp)
		for each in kp:
			feature={}
			feature['kp']=each
			feature['frame']=frameNumber
			keypointsVideo1.append(feature)

		img2 = cv2.drawKeypoints(frame,kp,color=(0,255,0), flags=0)
		#print "img2 created"
		#cv2.imshow('img2',img2)
		#print "img2"
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		frameNumber=frameNumber+1
	except(Exception):
		break 
cap.release()
numberOfFramesVideo1=frameNumber
#print keypointsVideo1
print "Done till video1"
cap2 = cv2.VideoCapture('testVideo4.mp4')#changed
keypointsVideo2=[]
frameNumber=1
while(cap2.isOpened()):
	try:

		ret, frame = cap2.read()
		#print frame
		orb = cv2.ORB()
		kp = orb.detect(frame,None)
		#print kp
		kp, des2 = orb.compute(frame, kp)
		for each in kp:
			feature={}
			feature['kp']=each
			feature['frame']=frameNumber
			keypointsVideo2.append(feature)
		img2 = cv2.drawKeypoints(frame,kp,color=(0,255,0), flags=0)
		#print "img2 created"
		#cv2.imshow('img2',img2)#changed
		#print "img2"
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		frameNumber=frameNumber+1
	except(Exception):
		break

cap2.release()
numberOfFramesVideo2=frameNumber




cv2.destroyAllWindows()

#print keypointsVideo2
print "Done page1"



createM(keypointsVideo1,keypointsVideo2,numberOfFramesVideo1,numberOfFramesVideo2, des1, des2)