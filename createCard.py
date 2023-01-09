import cv2

image1 = cv2.imread("Image_Manipulation/stock-mountain-sunset.jpg")

canvas = image1[0:612, 0:100]
image1[0:612, 100:200] = canvas
string = "Happy ___"
cv2.putText(image1, string, (0, 20), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1, color=(255, 255, 255))
cv2.imshow("greeting", image1)

cv2.imwrite("greeting.jpg", image1)

cv2.waitKey(0)
