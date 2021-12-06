import numpy as np
import cv2

# Capturing video through webcam
webcam = cv2.VideoCapture(0)

# Start a while loop
while (1):
    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()

    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # set range for LEAD ppb0 = (222, 130, 108)
    lead_lower = np.array([222, 130, 108], np.uint8)
    # lead_safe safe range ppb15 = (230, 168, 136)
    lead_safe = np.array([230, 168, 136], np.uint8)
    # lead unsafe unsafe range  ppb30 = (214, 131, 124)
    lead_unsafe = np.array([214, 131, 124], np.uint8)
    # ppb50 = (211, 115, 137)
    lead_upper = np.array([211, 115, 137], np.uint8)

    #lead_mask = cv2.inRange(hsvFrame, lead_lower, lead_upper)
    unsafe_mask = cv2.inRange(hsvFrame, lead_unsafe,lead_upper)
    safe_mask = cv2.inRange(hsvFrame, lead_lower,lead_safe)

    kernel = np.ones((5, 5), "uint8")

    unsafe_mask = cv2.dilate(unsafe_mask, kernel)
    res_lead = cv2.bitwise_and(imageFrame, imageFrame, mask=unsafe_mask)

    contours, hierarchy = cv2.findContours(unsafe_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        #unsafe zone
        if (area > 300):
            x,y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 255,0), 2)
            cv2.putText(imageFrame, "LEAD DETECTED: UNSAFE", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 0, 255))

   #safe zone

    safe_mask = cv2.dilate(safe_mask, kernel)
    res_safe = cv2.bitwise_and(imageFrame, imageFrame, mask=safe_mask)

    contours, hierarchy = cv2.findContours(safe_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        # unsafe zone
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imageFrame, "LEAD DETECTED: SAFE", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 0, 255))
    cv2.imshow("Real Time Lead Detection", imageFrame)
    if cv2.waitKey(10) & 0xFF == 27:
        cv2.destroyAllWindows()
        break
