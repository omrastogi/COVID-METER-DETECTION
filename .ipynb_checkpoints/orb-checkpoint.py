import numpy as np
import cv2
from matplotlib import pyplot as plt

print(1)
def view(tag,img):
	cv2.imshow(tag,img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

img = cv2.imread('WA3.jpeg',0)
print (2)
# Initiate STAR detector
orb = cv2.ORB_create()
print (3)
view('img',img)
# find the keypoints with ORB
kp = orb.detect(img,None)
print (4)
# compute the descriptors with ORB
# print (kp)
kp, des = orb.compute(img, kp)
print (5)
# print (kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,outImage=img,color=(0,255,0), flags=0)
# plt.imshow(img2),plt.show()

view('img',img2)