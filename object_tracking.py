## This code is used to track an object in a video stream using OpenCV HSV sliders. 
## The code uses the webcam to capture the video stream and uses the HSV sliders to track the object in the video stream.
## The code uses the cv2 library to capture the video stream and uses the numpy library to create the HSV sliders.

import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap = cv.VideoCapture(1)
cv.namedWindow('Trackers')
cv.createTrackbar("LH", 'Trackers', 0, 255, nothing)
cv.createTrackbar("LS", 'Trackers', 0, 255, nothing)
cv.createTrackbar("LV", 'Trackers', 0, 255, nothing)
cv.createTrackbar("UH", 'Trackers', 255, 255, nothing)
cv.createTrackbar("US", 'Trackers', 255, 255, nothing)
cv.createTrackbar("UV", 'Trackers', 255, 255, nothing)


while True:
    # frame = cv.imread("drawing.jpg")

    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("LH", 'Trackers')
    l_s = cv.getTrackbarPos("LS", 'Trackers')
    l_v = cv.getTrackbarPos("LV", 'Trackers')
    u_h = cv.getTrackbarPos("UH", 'Trackers')
    u_s = cv.getTrackbarPos("US", 'Trackers')
    u_v = cv.getTrackbarPos("UV", 'Trackers')

    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, lower, upper)
    result = cv.bitwise_and(frame, mask=mask)

    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
    cv.imshow("Result", result)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


     