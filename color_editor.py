import cv2 as cv;
import numpy as np;

# Functions

def nothing(x):
    pass


# Runner
if __name__ == "__main__":
    cv.namedWindow('Image')

    # Create trackbars for color change
    cv.createTrackbar("R", 'Image', 0, 100, nothing)
    cv.createTrackbar("G", 'Image', 0, 100, nothing)
    cv.createTrackbar("B", 'Image', 0, 100, nothing)
    cv.createTrackbar("Brightness", 'Image', 0, 100, nothing)
    cv.createTrackbar("Contrast", 'Image', 0, 100, nothing)

    # Image to be edited
    img = cv.imread('diavel.jpg')
    cv.imshow('Image', img)
    
    # Initial values
    cv.setTrackbarPos("R", 'Image', 50)
    cv.setTrackbarPos("G", 'Image', 50)
    cv.setTrackbarPos("B", 'Image', 50)
    cv.setTrackbarPos("Brightness", 'Image', 50)
    cv.setTrackbarPos("Contrast", 'Image', 50)
    while True:
        if cv.waitKey(5) & 0xFF == ord('q'):
            break

        r = cv.getTrackbarPos("R", 'Image')
        g = cv.getTrackbarPos("G", 'Image')
        b = cv.getTrackbarPos("B", 'Image')
        brightness = cv.getTrackbarPos("Brightness", 'Image')
        contrast = cv.getTrackbarPos("Contrast", 'Image')

        imgAdjusted = img.copy()
        
        imgAdjusted[:,:,0] = cv.multiply(img[:,:,0], b/50)
        imgAdjusted[:,:,1] = cv.multiply(img[:,:,1], g/50)
        imgAdjusted[:,:,2] = cv.multiply(img[:,:,2], r/50)
        imgAdjusted = cv.add(imgAdjusted, np.array([brightness-50]))
        imgAdjusted = cv.add(imgAdjusted, np.array([contrast-50]))
        cv.imshow("Image", imgAdjusted)

    cv.waitKey(1) & 0xFF
    cv.destroyAllWindows()