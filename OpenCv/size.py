import cv2

src = cv2.imread("/Users/triplet_dev/Python/image/test.png")


# interpolation = 복원법
# fx, fy = 비율
# dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
dst = cv2.resize(src, (360, 360))
cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
