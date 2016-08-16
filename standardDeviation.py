import numpy as np
import cv2
from matplotlib import pyplot as plt
from kdTreeNNeighbors import createM
from scipy.linalg import norm






cap = cv2.VideoCapture('testVideo3.mp4')
keypointsVideo1=[]
frameNumber=1
featureCount=1
tim=0
flag=0;
allStandardDeviation1=[]
while(cap.isOpened()):
	try:
		ret, frame = cap.read()
		#print frame
		if flag==0:
			temp=frame
		flag=1
		diff=temp-frame;
		print diff
		temp=frame;
		np.asarray(diff)
		#avgPixelImage = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY);
		normImage=norm(diff.ravel(),0);
		standardDeviation=float(normImage)/(len(frame)*len(frame[0]))
		allStandardDeviation1.append(standardDeviation)
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
flag=0
allStandardDeviation2=[]
while(cap2.isOpened()):
	try:

		ret, frame = cap2.read()
		#print frame
	
		#print frame
		if flag==0:
			temp=frame
		flag=1
		diff=temp-frame;
		print diff
		temp=frame;
		np.asarray(diff)
		#avgPixelImage = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY);
		normImage=norm(diff.ravel(),0);
		standardDeviation=float(normImage)/(len(frame)*len(frame[0]))
		allStandardDeviation2.append(standardDeviation)
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
print 'here'
plt.plot(allStandardDeviation1,'r')  
plt.plot(allStandardDeviation2,'b') 

plt.show()




#print temp
#print keypointsVideo2
print "Done page1"

#print keypointsVideo1
#print "numberOfFramesVideo1", numberOfFramesVideo1
#print "numberOfFramesVideo2", numberOfFramesVideo2
#matchMatrix=createM(keypointsVideo1,keypointsVideo2,numberOfFramesVideo1,numberOfFramesVideo2)
#print matchMatrix