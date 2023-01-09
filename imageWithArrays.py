import cv2
import numpy as np

canvas = np.zeros([600, 600])
canvas[250:350, 250:350] = 1

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
