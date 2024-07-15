import cv2 as cv
import matplotlib.pyplot as plt

def nothing(x):
    pass

img = cv.imread("drawing.jpg")

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()