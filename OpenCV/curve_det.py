import numpy as np
import cv2
from collections import defaultdict
import sys
import argparse
import math


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
im = args["image"]
img = cv2.imread(im)
og = img.copy()
clean = img.copy()


def intersection(line1, line2):
  rho1, theta1 = line1[0]
  rho2, theta2 = line2[0]
  A = np.array([[np.cos(theta1), np.sin(theta1)],
                [np.cos(theta2), np.sin(theta2)]])
  b = np.array([[rho1], [rho2]])
  x0, y0 = np.linalg.solve(A, b)
  x0, y0 = int(np.round(x0)), int(np.round(y0))
  return [[x0, y0]]


def segmented_intersections(lines):
  intersections = []
  for i, group in enumerate(lines[:-1]):
      for next_group in lines[i+1:]:
          for line1 in group:
              for line2 in next_group:
                  intersections.append(intersection(line1, line2))
  return intersections

def segment_by_angle_kmeans(lines, k=2, **kwargs):
  default_criteria_type = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
  criteria = kwargs.get('criteria', (default_criteria_type, 10, 1.0))
  flags = kwargs.get('flags', cv2.KMEANS_RANDOM_CENTERS)
  attempts = kwargs.get('attempts', 10)
  # Get angles in [0, pi] radians
  angles = np.array([line[0][1] for line in lines])
  # Multiply the angles by two and find coordinates of that angle on the Unit Circle
  pts = np.array([[np.cos(2*angle), np.sin(2*angle)] for angle in angles], dtype=np.float32)
  labels, centers = cv2.kmeans(pts, k, None, criteria, attempts, flags)[1:]
  labels = labels.reshape(-1) # Transpose to row vector
  # Segment lines based on their label of 0 or 1
  segmented = defaultdict(list)
  for i, line in zip(range(len(lines)), lines):
      segmented[labels[i]].append(line)
  segmented = list(segmented.values())
  print("Segmented lines into two groups: %d, %d" % (len(segmented[0]), len(segmented[1])))
  return segmented

def drawLines(img, lines, color=(0,0,255)):
  for line in lines:
      for rho,theta in line:
          a = np.cos(theta)
          b = np.sin(theta)
          x0 = a*rho
          y0 = b*rho
          x1 = int(x0 + 1000*(-b))
          y1 = int(y0 + 1000*(a))
          x2 = int(x0 - 1000*(-b))
          y2 = int(y0 - 1000*(a))
          cv2.line(img, (x1,y1), (x2,y2), color, 1)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
edges = cv2.Canny(blur, 100, 200)
adapt_type = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
thresh_type = cv2.THRESH_BINARY_INV
bin_img = cv2.adaptiveThreshold(blur, 255, adapt_type, thresh_type, 11, 2)
cv2.imshow("binary", bin_img)
# cv2.imshow("binary", clean)
cv2.waitKey()


# Detect lines
rho = 2
theta = np.pi/180
thresh = 350
lines = cv2.HoughLines(bin_img, rho, theta, thresh)

print("Found lines: %d" % (len(lines)))

# Draw all Hough lines in red
img_with_all_lines = np.copy(img)
drawLines(img_with_all_lines, lines)
# cv2.imshow("Hough lines", img_with_all_lines)
cv2.waitKey()
cv2.imwrite("all_lines.jpg", img_with_all_lines)

# Cluster line angles into 2 groups (vertical and horizontal)
segmented = segment_by_angle_kmeans(lines, 2)

# Find the intersections of each vertical line with each horizontal line
intersections = segmented_intersections(segmented)

img_with_segmented_lines = np.copy(img)

# Draw vertical lines in green
vertical_lines = segmented[1]
img_with_vertical_lines = np.copy(img)
drawLines(img_with_segmented_lines, vertical_lines, (147, 168, 50))

# Draw horizontal lines in peach
horizontal_lines = segmented[0]
img_with_horizontal_lines = np.copy(img)
drawLines(img_with_segmented_lines, horizontal_lines, (118, 190, 245))

# Draw intersection points in magenta
for point in intersections:
  pt = (point[0][0], point[0][1])
  length = 5
  cv2.line(img_with_segmented_lines, (pt[0], pt[1]-length), (pt[0], pt[1]+length), (201, 68, 146), 1) # vertical line
  cv2.line(img_with_segmented_lines, (pt[0]-length, pt[1]), (pt[0]+length, pt[1]), (201, 68, 146), 1)

xpt = []
ypt = []
for point in intersections:
  pt = (point[0][0], point[0][1])
  xpt.append(point[0][0])
  ypt.append(point[0][1])

def Average(lst):
 return sum(lst) / len(lst)

average_x = int(Average(xpt))
average_y = int(Average(ypt))

print(average_x)
length = 5
cv2.line(img_with_segmented_lines, (average_x, average_y-length), (average_x, average_y+length), (255, 0, 255), 1) # center
cv2.line(img_with_segmented_lines, (average_x-length, average_y), (average_x+length, average_y), (255, 0, 255), 1)

height, width, channels = img.shape
upper_left = (width // 4, height // 4)
bottom_right = (width * 3 // 4, height * 3 // 4)
# draw in the image
half = width//2
if half >= average_x:
  cv2.arrowedLine(og, (average_x, average_y + 4 * average_y), (average_x, average_y), (128, 140, 255), 5)
  cv2.arrowedLine(og, (average_x, average_y), (width-10, average_y), (128, 140, 255), 6)
else:
  cv2.arrowedLine(og, (average_x, average_y + 4 * average_y), (average_x, average_y), (128, 140, 255), 5)
  cv2.arrowedLine(og, (average_x, average_y), (0, average_y), (128, 140, 255), 6)

#cv2.line(img_with_segmented_lines, (width//2, height//2-length), (width//2, height//2+length), (255, 0, 255), 1) # vertical line
#cv2.line(img_with_segmented_lines, (width//2-length, height//2), (width//2+length, height//2), (255, 0, 255), 1)

cv2.imshow("Segmented lines", img_with_segmented_lines)
cv2.waitKey()
cv2.imwrite("intersection_points.jpg", img_with_segmented_lines)
cv2.waitKey()
cv2.imshow("End result", og)
cv2.waitKey()


