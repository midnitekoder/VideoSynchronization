import numpy as np
import cv2


#manually change from findRegions.py or differentFindRegions.py
removeFramesList1=[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
removeFramesList2=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



cap1 = cv2.VideoCapture('testVideo5.mp4')


# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
out1 = cv2.VideoWriter('testVideoRemove5.avi', fourcc, 25, (720,480),True)


frameNumber=0
while cap1.isOpened():
	try:
		    ret1, frame1 = cap1.read()
		   
		    if ret1==True:
		        #frame = cv2.flip(frame,0)
		        
		        # write the flipped frame
		        if removeFramesList1[frameNumber]==0:
		        	out1.write(frame1)
		        
		        #addWeighted( frame1, alpha, temp, beta, 0.0, avg);
		       
		        
		      
		        frameNumber=frameNumber+1
		      #  print 'working'


		        #cv2.imshow('frame',frame)
		        #if cv2.waitKey(1) & 0xFF == ord('q'):
		  
	

		    #cv2.imshow('frame',frame)
		    #if cv2.waitKey(1) & 0xFF == ord('q'):
		    #	break
		    #else:
		     #   break

		
#		    	break
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	except(Exception):
		break



# Release everything if job is finished
cap1.release()

out1.release()


cap2 = cv2.VideoCapture('testVideo6.mp4')


# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
out2 = cv2.VideoWriter('testVideoRemove6.avi', fourcc, 25, (720,480),True)


frameNumber=0
while cap2.isOpened():
	try:
		    ret2, frame2 = cap2.read()
		   
		    if ret2==True:
		        #frame = cv2.flip(frame,0)
		        
		        # write the flipped frame
		        if removeFramesList2[frameNumber]==0:
		        	out2.write(frame2)
		        
		        #addWeighted( frame1, alpha, temp, beta, 0.0, avg);
		        """
		        avg=(lab_image+temp)/2;
		        avgBGR=cv2.cvtColor(avg,cv2.COLOR_LAB2BGR)
		        """
		        
		      
		        frameNumber=frameNumber+1
		        print frameNumber
		      #  print 'working'


		        #cv2.imshow('frame',frame)
		        #if cv2.waitKey(1) & 0xFF == ord('q'):
		  
	

		    #cv2.imshow('frame',frame)
		    #if cv2.waitKey(1) & 0xFF == ord('q'):
		    #	break
		    #else:
		     #   break

		
#		    	break
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	except(Exception):
		break




# Release everything if job is finished
cap2.release()

out2.release()




cv2.destroyAllWindows()

