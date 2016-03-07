import numpy as np
from sklearn.neighbors import KDTree
import ast

def kdTree():
	fp=open('videosOrb.txt','r')
	list1=[]
	list1=fp.read().split('\n')
	#print list1
	createM(list1[0],list1[1],395,179)


def createM(keypointsVideo1,keypointsVideo2,numberOfFramesVideo1,numberOfFramesVideo2,des1,des2):
	#X=np.array([[1, 4], [3, 4], [5, 4], [7, 4]])
	#X=np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6], [4, 7, 8]])
	"""keypointsList2=[]
	#list=keypointsVideo2.split(',')
	#print list
	#j=json.loads(keypointsVideo2)
	#print j
	s=keypointsVideo2
	flag=0
	dicString=""
	for each in keypointsVideo2:
		#print each
		#print type(each)
		if flag==1:
			dicString+=str(each)
			#print "dicString", dicString
			flag=1
		elif each is "{":
			dicString+=str(each)
			#print "dicString", dicString
			flag=1
		if(each=="}"):
			#print dicString
			keypointsList2.append(dicString)
			dicString=""
			flag=0



	print list
	dict = list[1]"""
	
	#for each in keypointsVideo2:
	#	print each['frame']
	#	list.append(each['kp'])

	X=np.array(des2);
	tree = KDTree(X, leaf_size=2,metric='euclidean')
	for each in des1:
		dist, ind = tree.query(each, k=numberOfFramesVideo2)
		print ind
	


if __name__ == "__main__":
    kdTree()