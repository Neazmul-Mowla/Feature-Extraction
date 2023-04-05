import cv2
img = cv2.imread('input_image8.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()
kp, des = orb.detectAndCompute(gray, None)
img = cv2.drawKeypoints(img, kp, None)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
