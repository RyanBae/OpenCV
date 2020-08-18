import cv2
import numpy as np

src = cv2.imread(
    "/Users/triplet_dev/Python_openCV/OpenCV/image/test1.jpeg", cv2.IMREAD_COLOR)

B = src[:, :, 0]
G = src[:, :, 1]
R = src[:, :, 2]


# blue = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)


# BGR을 HSV 색공간으로 변경함
# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# HSV 에서 BGR로 가정할 범위를 정함
# lower_blue = np.array([110, 100, 100])
# upper_blue = np.array([130, 255, 255])

# HSV 이미지에서 위에 정해놓은 범위를 추출함
# blue = cv2.inRange(hsv, lower_blue, upper_blue)

# 마스트 이미지와 원본이미지를 비트 연산함
# blue = cv2.threshold(src, 100, 255, cv2.Th)
# res1 = cv2.bitwise_and(src, src, mask=blue)

# B
ret1, re1 = cv2.threshold(B, 95, 255, cv2.THRESH_BINARY)
ret2, re2 = cv2.threshold(R, 60, 255, cv2.THRESH_BINARY_INV)
res1 = cv2.bitwise_and(re1, re2)
res2 = cv2.cvtColor(res1, cv2.COLOR_BAYER_BG2BGR)
blue = cv2.bitwise_and(res2, src)
# res1 = cv2.bitwise_and(src, src, mask=blue)


# G
gret, gres1 = cv2.threshold(G, 50, 255, cv2.THRESH_BINARY)
gret, gres2 = cv2.threshold(R, 75, 255, cv2.THRESH_BINARY_INV)
gres3 = cv2.bitwise_and(gres1, gres2)


cv2.imshow("src", src)
# cv2.imshow("re1", re1)
# cv2.imshow("re2", re2)
# cv2.imshow("blue", blue)
# cv2.imshow("res1", res1)
# cv2.imshow("blue", blue)
cv2.imshow("GREEN", gres1)
cv2.imshow("GREEN2", gres2)
cv2.imshow("GREEN3", gres3)
# cv2.imshow("re1", re1)
# cv2.imshow("B", B)
# cv2.imshow("G", G)
# cv2.imshow("R", R)

cv2.waitKey(0)
cv2.destroyAllWindows()
