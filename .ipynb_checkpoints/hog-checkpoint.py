import numpy as np
import cv2
from matplotlib import pyplot as plt

def view(tag,img):
	cv2.imshow(tag,img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

im = cv2.imread('WA3.jpeg')
im = np.float32(im) / 255.0
# Calculate gradient

im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
gx = cv2.Sobel(im, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(im, cv2.CV_32F, 0, 1, ksize=1)
mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)

view('img',mag)