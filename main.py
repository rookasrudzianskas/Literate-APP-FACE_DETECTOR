import cv2

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# choosing an image, and calling the opecv imread function
img = cv2.imread('twins.jpg')

# changing to greyscale
# rgb is replaced to BGR because turns in the another way
grayscailed_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces, using data from the trained faces data. It is looking for the composition and detects all the cases
# return the coordinates
# finds the face, gets location coordinates, and returns them
face_coordinates = trained_face_data.detectMultiScale(grayscailed_image)

# draw rectangles
# two coordinates, color, and the thickness of rectangle
(x, y, w, h) = face_coordinates[2]
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

print(face_coordinates)

#  shows the image
cv2.imshow('Rokas!', img)
cv2.waitKey()

print("WORKING!")
