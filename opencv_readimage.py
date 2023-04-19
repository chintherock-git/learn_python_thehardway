import cv2 as cv

img = cv.imread("Photos/Krishna.jpg",1)
img = cv.resize(img,(0,0), fx=0.5,fy=0.5)
img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
cv.imwrite("rotated.jpg", img)
cv.imshow('photo',img)
cv.waitKey(0)
cv.destroyAllWindows()