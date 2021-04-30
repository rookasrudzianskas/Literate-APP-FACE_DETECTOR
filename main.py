import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# choosing an image, and calling the opecv imread function
img = cv2.imread('rokas.png')

cv2.imshow('ROkas!', img)
cv2.waitKey()
















print("WORKING!")