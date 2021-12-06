import cv2
import time

# Capturing video through webcam
webcam = cv2.VideoCapture(0)


TIMER = int(20)
# Start a while loop
while (1):
    # Reading the video from the
    # webcam in image frames
    #_, imageFrame = webcam.read()
    ret, frame = webcam.read()
    cv2.imshow('img1', frame)
    k = cv2.waitKey(125)
    if k == ord('p'):
        prev = time.time()

        while TIMER >= 0:
                ret, frame = webcam.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(TIMER),
                            (200, 250), font,
                            7, (0, 255, 255),
                            4, cv2.LINE_AA)
                cv2.imshow('img1', frame)
                cv2.waitKey(125)

                cur = time.time()

                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1
                else:
                    ret, frame = webcam.read()
                    cv2.imshow('img1', frame)
                    cv2.waitKey(2000)

                    cv2.imwrite('strip.jpg', frame)
    elif k == 27:
        break
webcam.release()

cv2.destroyAllWindows()
