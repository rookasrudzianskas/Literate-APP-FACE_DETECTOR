import cv2
from random import randrange

# trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# # choosing an image, and calling the opecv imread function
# img = cv2.imread('twins.jpg')
#
# # changing to greyscale
# # rgb is replaced to BGR because turns in the another way
# grayscailed_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Detect faces, using data from the trained faces data. It is looking for the composition and detects all the cases
# # return the coordinates
# # finds the face, gets location coordinates, and returns them
# face_coordinates = trained_face_data.detectMultiScale(grayscailed_image)
#
# # draw rectangles
# # two coordinates, color, and the thickness of rectangle
# # two coordinates and width and height
# # (x, y, w, h) = face_coordinates[2]
# # For the image
#
# # looping per all fa
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 256), randrange(256), randrange(256)), 2)
#
# print(face_coordinates)
#
# # end of image
# #  video
#
#
#
#
# #  shows the image
# cv2.imshow('Rokas!', img)
# cv2.waitKey()
#
# print("WORKING!")


trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# capturing the video from webcam, the default camera 0 is
# 0 is default camera
# first frame, now we need a loop
webcam = cv2.VideoCapture(0)

while True:
    #  Read the current frame from webcam
    #  true or false, and the frame is the current frame returned
    successful_frame_read, frame = webcam.read()

    # converting to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(128, 256), randrange(256), randrange(256)), 2)

    cv2.imshow("Rokas", frame)
    # it is waiting for the key to press to go to the next layer
    # without waitkey you cannot display anything
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

# key = cv2.waitKey(1)


# print("WORKING!")
