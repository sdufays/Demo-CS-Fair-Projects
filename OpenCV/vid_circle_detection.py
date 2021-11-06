import numpy as np

global size

cap = cv2.VideoCapture('/Users/sarahdufays/PycharmProjects/circle_detection/mov_4.MOV')

while True:
    wtv, img1 = cap.read()
    ret, img2 = cap.read()
    if img1 is None:
        break
    else:
        gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        detected_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 250, param1=90, param2=100, minRadius=100,
                                            maxRadius=200)
        if detected_circles is not None:
            detected_circles = np.uint16(np.around(detected_circles))
            for pt in detected_circles[0]:
                a, b, r = pt[0], pt[1], pt[2]
                thickness = 8
                thickness_2 = 24
                red = 255
                green = 255
                blue = 0
                cv2.circle(img2, (a, b), r, (red, green, blue), thickness)
                cv2.circle(img2, (a, b), r - thickness, (0, 0, 0), thickness+2)
                cv2.circle(img2, (a, b), 1, (255, 255, 255), 8)
        cv2.imshow("circle", np.hstack([img1, img2]))

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
