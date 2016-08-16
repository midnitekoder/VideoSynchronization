import numpy as np
import cv2
from matplotlib import pyplot as plt
from kdTreeNNeighbors import createM


orb = cv2.ORB()
cap = cv2.VideoCapture('testVideo3.mp4')
keypointsVideo1=[]
frameNumber=1
featureCount=1
tim=0
temp=[]
while(cap.isOpened()):
	try:
		ret, frame = cap.read()
		#print frame
		kp = orb.detect(frame,None)
		#print kp
		kp, des1 = orb.compute(frame, kp)
		if tim<3:
			temp.append(kp)
			tim=tim+1

		for each, despeach in zip(kp, des1):
			feature={}
			feature['kp']=each
			feature['frame']=frameNumber
			feature['desc']=despeach
			feature['featureCount']=featureCount
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
featureCount=1
while(cap2.isOpened()):
	try:

		ret, frame = cap2.read()
		#print frame
		orb = cv2.ORB()
		kp = orb.detect(frame,None)
		#print kp
		kp, des2 = orb.compute(frame, kp)
		for each, despeach in zip(kp,des2):
			feature={}
			feature['kp']=each
			feature['frame']=frameNumber
			feature['desc']=despeach
			feature['featureCount']=featureCount
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
count=0
"""print des1
for eachDesc in des1:
	for eachDesc2 in des1:
		print eachDesc




		'''
		for each in eachDesc:
			for each2 in eachDesc2:
				if each ==each2:
					print eachDesc
					count=count+1
print count, len(des1)
'''
"""
"""
list=[]
for each in keypointsVideo2:
	list.append(each['kp'])
set1=set(list)
print len(set1), len(list)
		
			#print each['desc'], each2['desc']

"""
#print temp
#print keypointsVideo2
print "Done page1"

#print keypointsVideo1
print "numberOfFramesVideo1", numberOfFramesVideo1
print "numberOfFramesVideo2", numberOfFramesVideo2
matchMatrix=createM(keypointsVideo1,keypointsVideo2,numberOfFramesVideo1,numberOfFramesVideo2)
print matchMatrix