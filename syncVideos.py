import numpy as np
from scipy.linalg import norm
import cv2
import heapq


#cutpoints=[{'frame2': 2, 'frame1': 2}, {'frame2': 2, 'frame1': 3}, {'frame2': 4, 'frame1': 3}]
#coordinateList=[{'frame1':1, 'frame2':1},{'frame1':2, 'frame2':1},{'frame1':2, 'frame2':2},{'frame1':3, 'frame2':2},{'frame1':3, 'frame2':3},{'frame1':3, 'frame2':4},{'frame1':4, 'frame2':5},{'frame1':5, 'frame2':6},{'frame1':6, 'frame2':6},{'frame1':7, 'frame2':6}]

#cutpoints=[{'frame2': 2, 'frame1': 4}, {'frame2': 6, 'frame1': 8}, {'frame2': 6, 'frame1': 9}, {'frame2': 7, 'frame1': 10}, {'frame2': 7, 'frame1': 13}, {'frame2': 10, 'frame1': 16}, {'frame2': 10, 'frame1': 17}, {'frame2': 11, 'frame1': 18}, {'frame2': 11, 'frame1': 19}, {'frame2': 14, 'frame1': 22}, {'frame2': 14, 'frame1': 31}, {'frame2': 15, 'frame1': 32}, {'frame2': 15, 'frame1': 33}, {'frame2': 16, 'frame1': 34}, {'frame2': 16, 'frame1': 35}, {'frame2': 19, 'frame1': 37}, {'frame2': 23, 'frame1': 41}, {'frame2': 24, 'frame1': 41}, {'frame2': 26, 'frame1': 43}, {'frame2': 27, 'frame1': 43}, {'frame2': 30, 'frame1': 46}, {'frame2': 32, 'frame1': 46}, {'frame2': 37, 'frame1': 51}, {'frame2': 38, 'frame1': 51}, {'frame2': 39, 'frame1': 52}, {'frame2': 40, 'frame1': 52}, {'frame2': 41, 'frame1': 53}, {'frame2': 42, 'frame1': 53}, {'frame2': 57, 'frame1': 68}, {'frame2': 58, 'frame1': 68}, {'frame2': 59, 'frame1': 69}, {'frame2': 60, 'frame1': 69}, {'frame2': 61, 'frame1': 70}, {'frame2': 64, 'frame1': 70}, {'frame2': 67, 'frame1': 73}, {'frame2': 68, 'frame1': 73}, {'frame2': 73, 'frame1': 78}, {'frame2': 75, 'frame1': 78}, {'frame2': 78, 'frame1': 81}, {'frame2': 80, 'frame1': 81}, {'frame2': 81, 'frame1': 82}, {'frame2': 83, 'frame1': 82}, {'frame2': 100, 'frame1': 99}, {'frame2': 112, 'frame1': 99}, {'frame2': 124, 'frame1': 134}, {'frame2': 125, 'frame1': 135}, {'frame2': 125, 'frame1': 139}, {'frame2': 130, 'frame1': 144}, {'frame2': 130, 'frame1': 145}, {'frame2': 131, 'frame1': 146}, {'frame2': 131, 'frame1': 154}, {'frame2': 132, 'frame1': 155}, {'frame2': 132, 'frame1': 159}, {'frame2': 133, 'frame1': 160}, {'frame2': 133, 'frame1': 161}, {'frame2': 134, 'frame1': 162}, {'frame2': 134, 'frame1': 172}, {'frame2': 135, 'frame1': 173}, {'frame2': 135, 'frame1': 181}, {'frame2': 136, 'frame1': 182}, {'frame2': 136, 'frame1': 184}, {'frame2': 137, 'frame1': 185}, {'frame2': 137, 'frame1': 188}, {'frame2': 138, 'frame1': 189}, {'frame2': 138, 'frame1': 197}, {'frame2': 150, 'frame1': 208}, {'frame2': 156, 'frame1': 214}, {'frame2': 158, 'frame1': 214}, {'frame2': 160, 'frame1': 216}, {'frame2': 161, 'frame1': 216}]

#cutpoints=[{'frame2': 18, 'frame1': 37}, {'frame2': 124, 'frame1': 111}, {'frame2': 149, 'frame1': 208}]
#coordinateList=[{'frame2': 1, 'frame1': 1}, {'frame2': 2, 'frame1': 2}, {'frame2': 2, 'frame1': 3}, {'frame2': 2, 'frame1': 4}, {'frame2': 3, 'frame1': 5}, {'frame2': 4, 'frame1': 6}, {'frame2': 5, 'frame1': 7}, {'frame2': 6, 'frame1': 8}, {'frame2': 6, 'frame1': 9}, {'frame2': 7, 'frame1': 10}, {'frame2': 7, 'frame1': 11}, {'frame2': 7, 'frame1': 12}, {'frame2': 7, 'frame1': 13}, {'frame2': 8, 'frame1': 14}, {'frame2': 9, 'frame1': 15}, {'frame2': 10, 'frame1': 16}, {'frame2': 10, 'frame1': 17}, {'frame2': 11, 'frame1': 18}, {'frame2': 11, 'frame1': 19}, {'frame2': 12, 'frame1': 20}, {'frame2': 13, 'frame1': 21}, {'frame2': 14, 'frame1': 22}, {'frame2': 14, 'frame1': 23}, {'frame2': 14, 'frame1': 24}, {'frame2': 14, 'frame1': 25}, {'frame2': 14, 'frame1': 26}, {'frame2': 14, 'frame1': 27}, {'frame2': 14, 'frame1': 28}, {'frame2': 14, 'frame1': 29}, {'frame2': 14, 'frame1': 30}, {'frame2': 14, 'frame1': 31}, {'frame2': 15, 'frame1': 32}, {'frame2': 15, 'frame1': 33}, {'frame2': 16, 'frame1': 34}, {'frame2': 16, 'frame1': 35}, {'frame2': 17, 'frame1': 36}, {'frame2': 18, 'frame1': 37}, {'frame2': 19, 'frame1': 37}, {'frame2': 20, 'frame1': 38}, {'frame2': 21, 'frame1': 39}, {'frame2': 22, 'frame1': 40}, {'frame2': 23, 'frame1': 41}, {'frame2': 24, 'frame1': 41}, {'frame2': 25, 'frame1': 42}, {'frame2': 26, 'frame1': 43}, {'frame2': 27, 'frame1': 43}, {'frame2': 28, 'frame1': 44}, {'frame2': 29, 'frame1': 45}, {'frame2': 30, 'frame1': 46}, {'frame2': 31, 'frame1': 46}, {'frame2': 32, 'frame1': 46}, {'frame2': 33, 'frame1': 47}, {'frame2': 34, 'frame1': 48}, {'frame2': 35, 'frame1': 49}, {'frame2': 36, 'frame1': 50}, {'frame2': 37, 'frame1': 51}, {'frame2': 38, 'frame1': 51}, {'frame2': 39, 'frame1': 52}, {'frame2': 40, 'frame1': 52}, {'frame2': 41, 'frame1': 53}, {'frame2': 42, 'frame1': 53}, {'frame2': 43, 'frame1': 54}, {'frame2': 44, 'frame1': 55}, {'frame2': 45, 'frame1': 56}, {'frame2': 46, 'frame1': 57}, {'frame2': 47, 'frame1': 58}, {'frame2': 48, 'frame1': 59}, {'frame2': 49, 'frame1': 60}, {'frame2': 50, 'frame1': 61}, {'frame2': 51, 'frame1': 62}, {'frame2': 52, 'frame1': 63}, {'frame2': 53, 'frame1': 64}, {'frame2': 54, 'frame1': 65}, {'frame2': 55, 'frame1': 66}, {'frame2': 56, 'frame1': 67}, {'frame2': 57, 'frame1': 68}, {'frame2': 58, 'frame1': 68}, {'frame2': 59, 'frame1': 69}, {'frame2': 60, 'frame1': 69}, {'frame2': 61, 'frame1': 70}, {'frame2': 62, 'frame1': 70}, {'frame2': 63, 'frame1': 70}, {'frame2': 64, 'frame1': 70}, {'frame2': 65, 'frame1': 71}, {'frame2': 66, 'frame1': 72}, {'frame2': 67, 'frame1': 73}, {'frame2': 68, 'frame1': 73}, {'frame2': 69, 'frame1': 74}, {'frame2': 70, 'frame1': 75}, {'frame2': 71, 'frame1': 76}, {'frame2': 72, 'frame1': 77}, {'frame2': 73, 'frame1': 78}, {'frame2': 74, 'frame1': 78}, {'frame2': 75, 'frame1': 78}, {'frame2': 76, 'frame1': 79}, {'frame2': 77, 'frame1': 80}, {'frame2': 78, 'frame1': 81}, {'frame2': 79, 'frame1': 81}, {'frame2': 80, 'frame1': 81}, {'frame2': 81, 'frame1': 82}, {'frame2': 82, 'frame1': 82}, {'frame2': 83, 'frame1': 82}, {'frame2': 84, 'frame1': 83}, {'frame2': 85, 'frame1': 84}, {'frame2': 86, 'frame1': 85}, {'frame2': 87, 'frame1': 86}, {'frame2': 88, 'frame1': 87}, {'frame2': 89, 'frame1': 88}, {'frame2': 90, 'frame1': 89}, {'frame2': 91, 'frame1': 90}, {'frame2': 92, 'frame1': 91}, {'frame2': 93, 'frame1': 92}, {'frame2': 94, 'frame1': 93}, {'frame2': 95, 'frame1': 94}, {'frame2': 96, 'frame1': 95}, {'frame2': 97, 'frame1': 96}, {'frame2': 98, 'frame1': 97}, {'frame2': 99, 'frame1': 98}, {'frame2': 100, 'frame1': 99}, {'frame2': 101, 'frame1': 99}, {'frame2': 102, 'frame1': 99}, {'frame2': 103, 'frame1': 99}, {'frame2': 104, 'frame1': 99}, {'frame2': 105, 'frame1': 99}, {'frame2': 106, 'frame1': 99}, {'frame2': 107, 'frame1': 99}, {'frame2': 108, 'frame1': 99}, {'frame2': 109, 'frame1': 99}, {'frame2': 110, 'frame1': 99}, {'frame2': 111, 'frame1': 99}, {'frame2': 112, 'frame1': 99}, {'frame2': 113, 'frame1': 100}, {'frame2': 114, 'frame1': 101}, {'frame2': 115, 'frame1': 102}, {'frame2': 116, 'frame1': 103}, {'frame2': 117, 'frame1': 104}, {'frame2': 118, 'frame1': 105}, {'frame2': 119, 'frame1': 106}, {'frame2': 120, 'frame1': 107}, {'frame2': 121, 'frame1': 108}, {'frame2': 122, 'frame1': 109}, {'frame2': 123, 'frame1': 110}, {'frame2': 124, 'frame1': 111}, {'frame2': 124, 'frame1': 112}, {'frame2': 124, 'frame1': 113}, {'frame2': 124, 'frame1': 114}, {'frame2': 124, 'frame1': 115}, {'frame2': 124, 'frame1': 116}, {'frame2': 124, 'frame1': 117}, {'frame2': 124, 'frame1': 118}, {'frame2': 124, 'frame1': 119}, {'frame2': 124, 'frame1': 120}, {'frame2': 124, 'frame1': 121}, {'frame2': 124, 'frame1': 122}, {'frame2': 124, 'frame1': 123}, {'frame2': 124, 'frame1': 124}, {'frame2': 124, 'frame1': 125}, {'frame2': 124, 'frame1': 126}, {'frame2': 124, 'frame1': 127}, {'frame2': 124, 'frame1': 128}, {'frame2': 124, 'frame1': 129}, {'frame2': 124, 'frame1': 130}, {'frame2': 124, 'frame1': 131}, {'frame2': 124, 'frame1': 132}, {'frame2': 124, 'frame1': 133}, {'frame2': 124, 'frame1': 134}, {'frame2': 125, 'frame1': 135}, {'frame2': 125, 'frame1': 136}, {'frame2': 125, 'frame1': 137}, {'frame2': 125, 'frame1': 138}, {'frame2': 125, 'frame1': 139}, {'frame2': 126, 'frame1': 140}, {'frame2': 127, 'frame1': 141}, {'frame2': 128, 'frame1': 142}, {'frame2': 129, 'frame1': 143}, {'frame2': 130, 'frame1': 144}, {'frame2': 130, 'frame1': 145}, {'frame2': 131, 'frame1': 146}, {'frame2': 131, 'frame1': 147}, {'frame2': 131, 'frame1': 148}, {'frame2': 131, 'frame1': 149}, {'frame2': 131, 'frame1': 150}, {'frame2': 131, 'frame1': 151}, {'frame2': 131, 'frame1': 152}, {'frame2': 131, 'frame1': 153}, {'frame2': 131, 'frame1': 154}, {'frame2': 132, 'frame1': 155}, {'frame2': 132, 'frame1': 156}, {'frame2': 132, 'frame1': 157}, {'frame2': 132, 'frame1': 158}, {'frame2': 132, 'frame1': 159}, {'frame2': 133, 'frame1': 160}, {'frame2': 133, 'frame1': 161}, {'frame2': 134, 'frame1': 162}, {'frame2': 134, 'frame1': 163}, {'frame2': 134, 'frame1': 164}, {'frame2': 134, 'frame1': 165}, {'frame2': 134, 'frame1': 166}, {'frame2': 134, 'frame1': 167}, {'frame2': 134, 'frame1': 168}, {'frame2': 134, 'frame1': 169}, {'frame2': 134, 'frame1': 170}, {'frame2': 134, 'frame1': 171}, {'frame2': 134, 'frame1': 172}, {'frame2': 135, 'frame1': 173}, {'frame2': 135, 'frame1': 174}, {'frame2': 135, 'frame1': 175}, {'frame2': 135, 'frame1': 176}, {'frame2': 135, 'frame1': 177}, {'frame2': 135, 'frame1': 178}, {'frame2': 135, 'frame1': 179}, {'frame2': 135, 'frame1': 180}, {'frame2': 135, 'frame1': 181}, {'frame2': 136, 'frame1': 182}, {'frame2': 136, 'frame1': 183}, {'frame2': 136, 'frame1': 184}, {'frame2': 137, 'frame1': 185}, {'frame2': 137, 'frame1': 186}, {'frame2': 137, 'frame1': 187}, {'frame2': 137, 'frame1': 188}, {'frame2': 138, 'frame1': 189}, {'frame2': 138, 'frame1': 190}, {'frame2': 138, 'frame1': 191}, {'frame2': 138, 'frame1': 192}, {'frame2': 138, 'frame1': 193}, {'frame2': 138, 'frame1': 194}, {'frame2': 138, 'frame1': 195}, {'frame2': 138, 'frame1': 196}, {'frame2': 138, 'frame1': 197}, {'frame2': 139, 'frame1': 198}, {'frame2': 140, 'frame1': 199}, {'frame2': 141, 'frame1': 200}, {'frame2': 142, 'frame1': 201}, {'frame2': 143, 'frame1': 202}, {'frame2': 144, 'frame1': 203}, {'frame2': 145, 'frame1': 204}, {'frame2': 146, 'frame1': 205}, {'frame2': 147, 'frame1': 206}, {'frame2': 148, 'frame1': 207}, {'frame2': 149, 'frame1': 208}, {'frame2': 150, 'frame1': 208}, {'frame2': 151, 'frame1': 209}, {'frame2': 152, 'frame1': 210}, {'frame2': 153, 'frame1': 211}, {'frame2': 154, 'frame1': 212}, {'frame2': 155, 'frame1': 213}, {'frame2': 156, 'frame1': 214}, {'frame2': 157, 'frame1': 214}, {'frame2': 158, 'frame1': 214}, {'frame2': 159, 'frame1': 215}, {'frame2': 160, 'frame1': 216}, {'frame2': 161, 'frame1': 216}, {'frame2': 162, 'frame1': 217}, {'frame2': 163, 'frame1': 218}, {'frame2': 164, 'frame1': 219}, {'frame2': 165, 'frame1': 220}]
video1remove=[]
video2remove=[]


def adjustClip(coordinateList,begin,last):
	if (last['frame1']-begin['frame1']-1<0):
		countFramesVideo1=0
	else:
		countFramesVideo1=(last['frame1']-begin['frame1']-1)
	if (last['frame2']-begin['frame2']-1<0):
		countFramesVideo2=0
	else:
		countFramesVideo2=(last['frame2']-begin['frame2']-1)
	if countFramesVideo1>countFramesVideo2:
		dict1={}
		dict1['begin']=begin['frame1']
		dict1['last']=last['frame1']
		dict1['remove']=countFramesVideo1-countFramesVideo2
		video1remove.append(dict1)
	elif countFramesVideo1<countFramesVideo2:
		dict1={}
		dict1['begin']=begin['frame2']
		dict1['last']=last['frame2']
		dict1['remove']=countFramesVideo2-countFramesVideo1
		video2remove.append(dict1)

def syncVideos(coordinateList,cutpoints):
	begin=coordinateList[0]
	for each in cutpoints:
		last=each
		adjustClip(coordinateList,begin,last)
		begin=last
	adjustClip(coordinateList,begin,coordinateList[-1])
	#print video1remove
	#print video2remove


	cap = cv2.VideoCapture('testVideo5.mp4')

	flag=0;
	allStandardDeviation1=[]
	frameNumber=0
	while(cap.isOpened()):
		try:
			ret, frame = cap.read()
			#print frame
			if flag==0:
				temp=frame
			flag=1
			diff=temp-frame
			#print diff
			temp=frame
			np.asarray(diff)
			#avgPixelImage = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY);
			normImage=norm(diff.ravel(),None);
			standardDeviation=float(normImage)/(len(frame)*len(frame[0]))
			dictStandardDeviation={}
			dictStandardDeviation['standardDeviation']=standardDeviation
			dictStandardDeviation['frame']=frameNumber
			allStandardDeviation1.append(dictStandardDeviation)
		#print "img2 created"
			#cv2.imshow('img2',img2)#changed
			#print "img2"
			frameNumber=frameNumber+1
					#print "img2 created"
			cv2.imshow('img2',frame)
			#print "img2"
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		except(Exception):
			break 
	cap.release()
	framesInVideo1=frameNumber
	print framesInVideo1
	#print keypointsVideo1
	print "Done till video11"
	cap2 = cv2.VideoCapture('testVideo6.mp4')#changed
	keypointsVideo2=[]
	frameNumber=0
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
	#		print diff
			temp=frame;
			np.asarray(diff)
			#avgPixelImage = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY);
			normImage=norm(diff.ravel(),None)
			standardDeviation=float(normImage)/(len(frame)*len(frame[0]))
			dictStandardDeviation={}
			dictStandardDeviation['standardDeviation']=standardDeviation
			dictStandardDeviation['frame']=frameNumber
			allStandardDeviation2.append(dictStandardDeviation)
		#print "img2 created"
			#cv2.imshow('img2',img2)#changed
			#print "img2"
			frameNumber=frameNumber+1
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		except(Exception):
			break

	cap2.release()
	framesInVideo2=frameNumber
	print framesInVideo2
	removeFramesList1=[]
	#print allStandardDeviation2
	for i in range(0,framesInVideo1):
		removeFramesList1.append(0)
	for each in video1remove:
		subarray=allStandardDeviation1[each['begin']+1:each['last']]
		removeFrames = heapq.nsmallest(each['remove'], subarray, key=lambda s: s['standardDeviation'])
		for eachFrameEntry in removeFrames:
			removeFramesList1[eachFrameEntry['frame']]=1
	print removeFramesList1

	removeFramesList2=[]
	for i in range(0,framesInVideo2):
		removeFramesList2.append(0)
	for each in video2remove:
		subarray=allStandardDeviation2[each['begin']+1:each['last']]
		removeFrames = heapq.nsmallest(each['remove'], subarray, key=lambda s: s['standardDeviation'])
		for eachFrameEntry in removeFrames:
			removeFramesList2[eachFrameEntry['frame']]=1
	print removeFramesList2
