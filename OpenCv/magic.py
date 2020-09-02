import cv2
import numpy as np

img = cv2.imread("/Users/triplet_dev/Python_openCV/OpenCV/image/test1.jpeg")
# callback 함수


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        color = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv = color[y, x, :]
        # h, s, v = cv2.split(color)
        # print(hsv)
        h = hsv[0]
        # numpy array 에 담아서 inRange 에 넣기
        lower = np.array([h-5])
        upper = np.array([h+5])

        # lower <= x <= upper
        mask = cv2.inRange(color[:, :, 0], lower, upper)
        result = cv2.bitwise_and(color, color, mask=mask)
        result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
        cv2.imshow("result", result)
        # 흰색 잡기


cv2.namedWindow('image')  # 창 지정
cv2.setMouseCallback('image', click_event)  # 어떤 창에다가 마우스 이벤트를 지정

while(1):
    cv2.imshow('image', img)

    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
