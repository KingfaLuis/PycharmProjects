import cv2 as cv

img = cv.imread("C:/Users/my/Desktop/IMG_9604",cv.IMREAD_COLOR)
cv.imshow("opencv_demo",img)
cv.waitKey(0)
cv.destroyAllWindows()