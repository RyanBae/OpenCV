import cv2

src = cv2.imread("/Users/triplet_dev/Python/image/test.png", cv2.IMREAD_COLOR)

# dst = src.copy()


# 행렬 다루기 src[100:600, 200:700]
#                행(y)    렬(x)
# 행렬은 index 값
# x = [1,2,3,4,5]
# y = x[1:3]
# y = x[1:]  = 1 ~ 끝까지

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
dst3 = src[0:500, 0:500]

# 4번 문제
dst4 = src[600:, 580:]

# 5번 문제
dst5 = src[250:650, 250:650]

cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
# cv2.imshow("dst3", dst3)
# cv2.imshow("dst4", dst4)
# cv2.imshow("dst5", dst5)
cv2.waitKey(0)
cv2.destroyAllWindows()
