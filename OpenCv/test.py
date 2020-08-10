import cv2


image = cv2.imread("/Users/triplet_dev/Python/image/test.png")
print(image)
cv2.imshow("Moon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
