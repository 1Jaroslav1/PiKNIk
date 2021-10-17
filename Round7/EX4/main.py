import numpy as np
import cv2

img2 = cv2.imread('image.png')
img = cv2.imread('image.png', 0)

cv2.imshow("Original", img2)


result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 95, 8)
cv2.imshow("contur", result)

for i in range(70, 255, 70):
    for j in range(70, 255, 70):
        for n in range(70, 255, 70):
            hsv_min = np.array((i-70, j-70, n-70), np.uint8)
            hsv_max = np.array((i, j, n), np.uint8)

            color = (0, 0, 0)

            hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
            thresh = cv2.inRange(hsv, hsv_min, hsv_max)

            moments = cv2.moments(thresh, 1)
            dM01 = moments['m01']
            dM10 = moments['m10']
            dArea = moments['m00']

            if dArea > 100:
                x = int(dM10 / dArea)
                y = int(dM01 / dArea)
                # print(round(int(dM10)/1000),int(dM01), int(dArea))
                cv2.circle(result, (x, y), 3, color, 2)
                cv2.putText(result, "%d,%d,%d" % (i, j, n), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

cv2.imshow('oznaczenie kolorow nie pracuje :( )', result)
cv2.waitKey()
