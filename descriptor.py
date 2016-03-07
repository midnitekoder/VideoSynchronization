import numpy as np
import cv2
from sklearn.neighbors import KDTree
from kdTreeNNeighbors import createM

orb=cv2.ORB()
frame = cv2.imread('dp.png')
kp = orb.detect(frame,None)

kp, des1 = orb.compute(frame, kp)

frame=cv2.imread('dp2.png')
kp=orb.detect(frame, None)

kp, des2=orb.compute(frame, kp)

X=np.array(des2);
tree = KDTree(X, leaf_size=2,metric='euclidean')
for each in des1:
		dist, ind = tree.query(each, k=size(X))
		print ind
	


