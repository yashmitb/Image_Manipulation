import cv2

image1 = cv2.imread("Image_Manipulation/landscape.png")

tree = image1[161:430, 68:251]
# 368:551
image1[161:430, 368:551] = tree
cv2.putText(image1, "Good Morning!", (230, 160),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255))

cv2.imshow("tree", image1)
cv2.waitKey(0)
