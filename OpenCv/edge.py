

# Convolution Filter
# 수직 필터
# -1  0  1
# -2  0  2
# -1  0  1

# 수평필터
# 1   2  1
# 0   0  0
# -1 -2 -1

import cv2
src = cv2.imread("/Users/triplet_dev/Python_openCV/OpenCV/image/test1.jpeg")

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 가장 많이 사용
canny = cv2.Canny(src, 100, 255)

# 윤곽선을 파란색으로 만들기
# 이미지에서 같은 레벨의 것들을 골라줌
contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    cv2.drawContours(src, [cnt], 0, (255, 0, 0), 3)


# y, x 축을 선택할수 있다.
# sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
# sobel2 = cv2.Sobel(gray, cv2.CV_8U, 0, 1, 3)
# sobel3 = cv2.Sobel(gray, cv2.CV_8U, 1, 1, 3)

# 외각선 보다는 선명도 구분시 많이 사용 (흔들림)
# lapacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

cv2.imshow("src", src)
# cv2.imshow("canny", canny)
# cv2.imshow("sobel", sobel)
# cv2.imshow("sobel2", sobel2)
# cv2.imshow("sobel3", sobel3)
# cv2.imshow("lapacian", lapacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
