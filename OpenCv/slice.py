import cv2
import numpy as np

src = cv2.imread(
    "/Users/triplet_dev/Python_openCV/OpenCV/image/test.png", cv2.IMREAD_COLOR)

# dst = src.copy()


# 행렬 다루기 src[100:600, 200:700]
#                행(y)    렬(x)
# 행렬은 index 값
# x = [1,2,3,4,5]
# y = x[1:3]
# y = x[1:]  = 1 ~ 끝까지

print(src.shape[:3])

height, width = src.shape[:2]
print(height, width)


# 1번 문제
w1 = round(width / 2)
print(w1)
dst1 = src[0:, 0:w1]

# 2번 문제
h2 = round(height/2)
dst2 = src[0:h2, 0:]

# 3번 문제
w3 = round(width/2)
h3 = round(height/2)
dst3 = src[0:h3, 0:w3]

# 4번 문제
w4 = round((width/3)*2)
h4 = round((height/3)*2)
dst4 = src[h4:, w4:]

# 5번 문제
w5 = round((width/4))
h5 = round((height/4))
w6 = w5*2
h6 = h5*2

print(h5, w5)
print(h6, w6)
dst5 = src[h5:h6, w5:w6]

# 채널 ===========================================

# RGB 별로 추출 하여 표현 (데이터상 BGR 임)
# 채널별로 뽑기
# BGR
B = src[:, :, 0]
G = src[:, :, 1]
R = src[:, :, 2]

# gray color 로 바꾸기
# gray color change 안됨
# gray = R * 0.3 + G * 0.59 + B*0.11

# 방법 1
gray1 = (R + G + B) / 3
# gray1 = src[:, :, gray1]


#  방법 2
# gray2 = ((0.299 * R) + (0.587 * G) + (0.114 * B))
# numpy 의 배열로 바꾸는것 .astype(uint8)   언사인트 인티저 8bit
# gray2 = gray2.astype(np.uint8)

# 방법 3
# cv2 함수 이용 방법
# cvt :: 컨버터
gray3 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# gray4 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# gray5 = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)


# 이진화 =>
# threshold 스레쉬홀드 :: 임계값
# 예제상 100 이 임계값
ret, dst7 = cv2.threshold(gray3, 100, 255, cv2.THRESH_BINARY)
print("=====> ret?")
print(ret)
cv2.imshow("src", src)
# cv2.imshow("dst1", dst1)
# cv2.imshow("dst2", dst2)
# cv2.imshow("dst3", dst3)
# cv2.imshow("dst4", dst4)
# cv2.imshow("dst5", dst5)

# ========================= color
# cv2.imshow("B", B)
# cv2.imshow("G", G)
# cv2.imshow("R", R)
# cv2.imshow("gray1", gray1)
# cv2.imshow("gray2", gray2)
# cv2.imshow("gray3", gray3)
# cv2.imshow("gray4", gray4)
# cv2.imshow("gray5", gray5)
cv2.imshow("dst7", dst7)

cv2.waitKey(0)
cv2.destroyAllWindows()
