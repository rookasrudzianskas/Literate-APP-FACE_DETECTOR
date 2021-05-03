import cv2

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# choosing an image, and calling the opecv imread function
img = cv2.imread('detection.jpg')

# changing to greyscale
# rgb is replaced to BGR because turns in the another way
grayscailed_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces, using data from the trained faces data. It is looking for the composition and detects all the cases
# return the coordinates
# finds the face, gets location coordinates, and returns them
face_coordinates = trained_face_data.detectMultiScale(grayscailed_image)

print(face_coordinates)

#  shows the image
# cv2.imshow('Rokas!', grayscailed_image)
# cv2.waitKey()

print("WORKING!")
