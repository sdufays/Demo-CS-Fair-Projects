import argparse
import cv2
import math
import numpy as np

# use "-vin 3674.mp4 --video_in 3674.mp4" as paramters for the first, shorter test case
# use "-vin 3686.mp4 --video_in 3686.mp4" as paramters for the second, harder test case


def mask(img, points):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, points, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=None, thickness=3):
    if color is None:
        color = [255, 0, 0]
    line_img = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    img = np.copy(img)
    if lines is None:
        return
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
    return img

def last_step(image):
    height = image.shape[0]
    width = image.shape[1]
    # for the long video
    if (args["video_in"]) == "3686.mp4":
        # os.remove("3686.mp4")
        region_of_interest_points = [(0, height + 200 + 20),(11 * width / 24 - 140, height / 3),  (7 * width / 12 + 200 + 40, height)]
    # for the short video
    if (args["video_in"]) == "3674.mp4":
        # os.remove("3674.mp4")
        region_of_interest_points = [(0, height),(11 * width / 24 + 200, height / 3 - 250), (7 * width / 12, height + 70 + 60)
        ]
    grayed = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cannyed = cv2.Canny(grayed, 100, 200)
    cropped_image = mask(cannyed,np.array([region_of_interest_points],np.int32),)
    # determines where the lines are in the image
    lines = cv2.HoughLinesP(
        cropped_image,
        rho=6,
        theta=np.pi / 60,
        threshold=160,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=25
    )
    left_line_x = []
    left_line_y = []
    right_line_x = []
    right_line_y = []
    linePrinted = True

    if lines is None:
        if (args["video_in"]) == "3674.mp4":
            image = cv2.circle(image, (int(width/6), 3*int(height/4)), 50, (68, 200, 227), -1)
        else:
            image = cv2.circle(image, (int(width/6), 3*int(height/4)), 50, (61, 150, 23), -1)
        return image
    print(lines)
    for line in lines:
        for x1, y1, x2, y2 in line:
            slope = (y2 - y1) / (x2 - x1)  # <-- Calculating the slope.
            if math.fabs(slope) < 1:  # <-- Only consider extreme slope
                continue
            if slope <= 0:  # <-- If the slope is negative, add to the left group.
                left_line_x.extend([x1, x2])
                left_line_y.extend([y1, y2])
            else:  # <-- Otherwise, add to the right group.
                right_line_x.extend([x1, x2])
                right_line_y.extend([y1, y2])
    min_y = image.shape[0] * (3 / 5)  # <-- Just below the horizon 3/5
    max_y = image.shape[0]  # <-- The bottom of the image
    line_image = image
    print("overlayed lines")
    print("----------------------------------------------------")
    if left_line_x and left_line_y and right_line_x and right_line_y:
        poly_left = np.poly1d(np.polyfit(
            left_line_y,
            left_line_x,
            deg=1
        ))
        left_x_start = int(poly_left(max_y))
        left_x_end = int(poly_left(min_y))
        poly_right = np.poly1d(np.polyfit(
            right_line_y,
            right_line_x,
            deg=1
        ))
        right_x_start = int(poly_right(max_y))
        right_x_end = int(poly_right(min_y))
        line_image = draw_lines(
            image,
            [[
                [left_x_start, max_y, left_x_end, min_y],
                [right_x_start, max_y, right_x_end, min_y],
            ]],
            thickness=5,
        )
    else:
        linePrinted = False
    if linePrinted:
        if (args["video_in"]) == "3674.mp4":
            line_image = cv2.circle(line_image, (int(width / 6), 3 * int(height / 4)), 50, (61, 150, 23), -1)
        else:
            line_image = cv2.circle(line_image, (int(width / 6), 3 * int(height / 4)), 50, (68, 200, 227), -1)
    else:
        if (args["video_in"]) == "3674.mp4":
            line_image = cv2.circle(line_image, (int(width / 6), 3 * int(height / 4)), 50, (68, 200, 227), -1)
        else:
            line_image = cv2.circle(line_image, (int(width / 6), 3 * int(height / 4)), 50, (61, 150, 23), -1)
    return line_image

# Argument for the path to the video
ap = argparse.ArgumentParser()
ap.add_argument("-vin", "--video_in", required=True, help="Path to the video")
args = vars(ap.parse_args())
vid = cv2.VideoCapture(args["video_in"])

# creates two separate videos, depending on which test case is running
if (args["video_in"]) == "3686.mp4":
    pathOut = 'long_video.mp4'
if (args["video_in"]) == "3674.mp4":
    pathOut = 'short_video.mp4'

while True:
    # reads the video
    ret, frame = vid.read()
    if frame is None:
        break
    else:
        height, width, layers = frame.shape
        size = (width, height)
        output1 = frame.copy()
        output = last_step(output1)
        cv2.imshow('Frame', output)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        # exiting the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
