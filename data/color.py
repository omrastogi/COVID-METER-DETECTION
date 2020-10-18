import cv2
import numpy as np
def view(tag,img):
	cv2.imshow(tag,img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



image=cv2.imread("WA3.jpeg")   #read in the image
print(image.shape)
image=cv2.resize(image,(360,640)) #resizing because opencv does not work well with bigger images
orig=image.copy()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

minval = np.array([120,0,0])
maxval = np.array([150,161,179])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, minval, maxval)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(image,image, mask= mask)

view('img', mask)
view('img', res)