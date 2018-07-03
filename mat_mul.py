import numpy as np
import cv2
import time
import psutil

# img = cv2.imread('/home/anuj/Desktop/IMG_20170916_192211.jpg')
# print img.dtype
# print img.shape

rs = np.random.RandomState(2)
arr = rs.randint(low=0, high=255, size=(100000, 10000), dtype=np.int64)
# print arr.dtype
# print arr.shape

# # print img
# cv2.imshow("asd0", arr)
# cv2.imwrite('random.jpg', arr)
# cv2.waitKey()


# img = cv2.imread('random.jpg')
# cv2.imshow("adsa", np.multiply(img, img))
# cv2.waitKey()

# for i in range(100000):
print np.multiply(arr, arr)


# in_gb = 1024*1024*1024

# for i in range(1000):
	# mem = psutil.virtual_memory()
	# print (mem[1])/(in_gb)