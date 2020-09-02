import cv2

# callback Fun


img = cv2.imread("/Users/triplet_dev/Python_openCV/OpenCV/image/test1.jpeg")


# 마우스 이벤트 callback
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        color = img[y, x, :]
        # print(color)

        #cv2.merge(r, g, b)

        # 1. 원본 이미지를 b,g,r 로 나누어서 변수에 담음.

        blue = img[:, :, 0]
        green = img[:, :, 1]
        red = img[:, :, 2]

        # 2. 블루에 대한 0, 255의 값 구하기

        # 0
        ret, blue1 = cv2.threshold(blue, color[0]-10, 255, cv2.THRESH_BINARY)
        # 255
        ret, blue2 = cv2.threshold(
            blue, color[0]+10, 255, cv2.THRESH_BINARY_INV)
        rb = cv2.bitwise_and(blue1, blue2)

        # 3.그린에 대한 0, 255의 값 구하기

        # 0
        ret, green1 = cv2.threshold(green, color[1]-10, 255, cv2.THRESH_BINARY)
        # 255
        ret, green2 = cv2.threshold(
            green, color[1]+10, 255, cv2.THRESH_BINARY_INV)
        rg = cv2.bitwise_and(green1, green2)

        # 4.레드에 대한 0, 255의 값 구하기

        # 0
        ret, red1 = cv2.threshold(red, color[2]-10, 255, cv2.THRESH_BINARY)
        # 255
        ret, red2 = cv2.threshold(red, color[2]+10, 255, cv2.THRESH_BINARY_INV)
        rr = cv2.bitwise_and(red1, red2)

        result = cv2.merge((rr, rg, rb))

        print(result)
        cv2.imshow('result', result)

# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(y, x)
#         color = img[y, x, :]
#         # color = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
#         # th1 = cv2.threshold(img, 100, 255, cv2.B)
#         print(color)


# 창 지정
cv2.namedWindow('image')
# 어떤 창에다가 마우스를 지정할 것인지
cv2.setMouseCallback('image', click_event)
cv2.imshow('image', img)

while(1):
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
