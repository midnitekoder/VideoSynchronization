import numpy as np
import cv2




cap1 = cv2.VideoCapture('testVideo5.mp4')


# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
out1 = cv2.VideoWriter('testVideoPad5.avi', fourcc, 25, (720,480),True)

print 'yo'
prevPair={'frame1':0,'frame2':0}

flag=0
count=0;
me = 0
while cap1.isOpened():
		    ret1, frame1 = cap1.read()
		   
		    if ret1==True:
		        #frame = cv2.flip(frame,0)
		        lab_image = cv2.cvtColor(frame1, cv2.COLOR_BGR2LAB)
		        if flag==0:
		    		temp=frame1
		    	flag=1
		        if count<4:
		        	count=count+1
		        else:
		        	count=0
		        # write the flipped frame
		        out1.write(frame1)
		        alpha=0.5
		        beta=1-alpha
		        if count==4:
		        	avg = cv2.addWeighted(frame1,0.7,temp,0.3,0)
		        	out1.write(avg)
		        #addWeighted( frame1, alpha, temp, beta, 0.0, avg);
		        """
		        avg=(lab_image+temp)/2;
		        avgBGR=cv2.cvtColor(avg,cv2.COLOR_LAB2BGR)
		        """
		        
		      
		        temp=frame1
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




# Release everything if job is finished
cap1.release()

out1.release()


cv2.destroyAllWindows()

