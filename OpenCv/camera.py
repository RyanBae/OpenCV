import cv2


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    k = cv2.waitKey(0)
    print(k)
    if k > 0:
        break
    # waitKey(0) :: 키 입력을 기다림
    # (0) 은 무한히 기다림
    # if cv2.waitKey(0) > 0:
       # break

capture.release()
cv2.destroyAllWindows()
