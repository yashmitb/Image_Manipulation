import cv2

image1 = cv2.imread("Image_Manipulation/stock-mountain-sunrise.jpg")
grayImage = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
cv2.imshow("Sunrise Gray", grayImage)
cv2.waitKey(0)
