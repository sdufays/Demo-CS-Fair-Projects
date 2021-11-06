import cv2
import argparse
import numpy as np
import math

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
im = args["image"]
img = cv2.imread(im)
img_og = img.copy()

if im == "front.jpg":
    pt1 = (1540, 500)
    pt2 = (-450, 2000)
    pt3 = (3445, 2000)


fill_color = [173, 182, 185]
mask_value = 255

contours = [ np.array( [pt1, pt2, pt3] )]

stencil = np.zeros(img.shape[:-1]).astype(np.uint8)
cv2.fillPoly(stencil, contours, mask_value)

sel = stencil != mask_value 
img[sel] = fill_color           


# gets the center of the triangle
centroid = ((pt1[0]+pt2[0]+pt3[0])//3, (pt1[1]+pt2[1]+pt3[1])//3)
x_coor = (pt1[0]+pt2[0]+pt3[0])//3
y_coor = (pt1[1]+pt2[1]+pt3[1])//3

# this is to detect the lines within the masked area
img_2 = img.copy()
gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
lines = cv2.HoughLinesP(edges, 1, np.pi/380, 30, maxLineGap=400)

ZY = 0
ZX = 0

XY = 10000
XX = 0

# # print(lines)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img_2, (x1, y1), (x2, y2), (0, 0, 225), 5)
    if ZY < y2:  # This is bottom right point
        ZY = y2
        ZX = x2
    if XY > y2:
        XY = y2
        XX = x2
    MidX = (ZX - XX) / 2 + XX
    MidX2 = math.floor(MidX)
    MidY = (XY - ZY) / 2 + ZY
    MidY2 = math.floor(MidY)
# cv2.circle(img_og, centroid, 20, (0, 0, 0))

if im == "front.jpg":
    up_point = y_coor + 115
    down_point = y_coor - 600
    x_coor2 = x_coor

image = cv2.arrowedLine(img_og, (x_coor,up_point), (x_coor2,down_point), (0, 0, 0), 20)

cv2.imshow("lines", np.hstack([img, image]))
cv2.waitKey(0)

