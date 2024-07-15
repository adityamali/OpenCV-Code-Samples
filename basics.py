import cv2 as cv

cap = cv.VideoCapture(2)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv.FONT_HERSHEY_SIMPLEX
        text = "Width: " + str(cap.get(3)) + ", Height: " + str(cap.get(4))
        flip = cv.flip(frame, 1)
        cv.putText(flip, text, (10,50), font, 1, (0,0,255), 1, cv.LINE_AA)
        cv.imshow('Video Capture', flip)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
