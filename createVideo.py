import numpy as np
import cv2



def createVideos(coordinateList,video1rows,video2columns):

	cap1 = cv2.VideoCapture('testVideo5.mp4')
	cap2 = cv2.VideoCapture('testVideo6.mp4')

	# Define the codec and create VideoWriter object
	fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
	out1 = cv2.VideoWriter('outputTestVideo3.avi', fourcc, 25, (720,480),True)
	out2 = cv2.VideoWriter('outputTestVideo4.avi', fourcc, 25, (720,480),True)

	prevPair={'frame1':0,'frame2':0}
	for eachPair in coordinateList:
		if(cap1.isOpened() and cap2.isOpened()):
			print "Prev",prevPair, "each",eachPair
			if prevPair['frame1'] != eachPair['frame1']:

			    ret1, frame1 = cap1.read()
			    if ret1==True:
			        #frame = cv2.flip(frame,0)

			        # write the flipped frame
			        out1.write(frame1)

			        #cv2.imshow('frame',frame)
			        #if cv2.waitKey(1) & 0xFF == ord('q'):
			         #   break
			    #else:
			     #   break
			else:
				out1.write(frame1)

			    #cv2.imshow('frame',frame)
			    #if cv2.waitKey(1) & 0xFF == ord('q'):
			    #	break
			    #else:
			     #   break

			if prevPair['frame2'] != eachPair['frame2']:

			    ret2, frame2 = cap2.read()
			    if ret2==True:
			        #frame = cv2.flip(frame,0)

			        # write the flipped frame
			        out2.write(frame2)

			        #cv2.imshow('frame',frame)
			        #if cv2.waitKey(1) & 0xFF == ord('q'):
			         #   break
			    #else:
			     #   break
			else:
				out2.write(frame2)

			    #cv2.imshow('frame',frame)
			    #if cv2.waitKey(1) & 0xFF == ord('q'):
			    #	break
			    #else:
			     #   break
		cv2.imshow('frame',frame1)
		cv2.waitKey(1)

		prevPair=eachPair

	# Release everything if job is finished
	cap1.release()
	cap2.release()
	out1.release()
	out2.release()

	cv2.destroyAllWindows()










	"""
	import cv2
	import numpy as np
	#def createVideo():
	list1=[]
	cap = cv2.VideoCapture('testVideo3.mp4')
	length1 = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
	print length1
	while(cap.isOpened()):
		try:
			length1=length1-1
			if length1<=0:
				break
			ret, frame = cap.read()
			list1.append(frame)
			print "Yo"
			print frame
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		except(Exception):
			break

	cap.release()
	print list1

	list2=[]
	cap = cv2.VideoCapture('testVideo4.mp4')
	length2 = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
	print length2
	while(cap.isOpened()):
		try:
			length2=length2-1
			if length2<=0:
				break
			ret, frame = cap.read()
			list2.append(frame)
			print frame
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		except(Exception):
			break

	cap.release()
	print list2[1]
	print len(list1), "yo"
	print list1[1]

	writer = cv2.VideoWriter('/home/ankit/Documents/6th sem/computer graphics/researchPaper/test1.avi', cv2.cv.CV_FOURCC(*'PIM1'), 25, (640, 480), True)
	for i in range(25):
			x = np.array(list1[i][1])
			writer.write(x)
	"""

		
