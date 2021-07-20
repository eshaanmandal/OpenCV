import cv2 as cv


img = cv.imread('Images\pexels-nikita-kurmachev-8667139.jpg')
cv.imshow("Girl", mat=img)
cv.waitKey(0)