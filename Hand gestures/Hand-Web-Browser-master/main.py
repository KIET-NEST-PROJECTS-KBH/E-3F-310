import cv2
import numpy as np
import math
import webbrowser as wb
import os

print ("Enter full website for")

print ("\n2 fingers")
fingers2=input()

print ("\n3 fingers")
fingers3=input()

print ("\n4 fingers")
fingers4=input()

# Initialize counters
counters = {
    fingers2: 0,
    fingers3: 0,
    fingers4: 0
}

tabs = 0
count = 0
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # read image
    ret, img = cap.read()

    # ... (Rest of your code)

    # Convert grayscale image to binary
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Find contour with max area
    cnt = max(contours, key=lambda x: cv2.contourArea(x))

    # Create bounding rectangle around the contour (can skip below two lines)
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

    # Finding convex hull
    hull = cv2.convexHull(cnt)

    # Drawing contours
    drawing = np.zeros(crop_img.shape, np.uint8)
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 0)

    # Finding convex hull
    hull = cv2.convexHull(cnt, returnPoints=False)  # return point false to find convexity defects

    # Finding convexity defects
    defects = cv2.convexityDefects(cnt, hull)

    # Initialize count_defects
    count_defects = 0

    # Loop over defects and calculate count_defects
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]  # [start point, end point, farthest point, approximate distance to farthest point]

        # ... (Rest of your code)

    # ... (Rest of your code)

    # Display counters
    y_offset = 200
    for website, counter in counters.items():
        cv2.putText(img, f"{website}: {counter} times", (50, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        y_offset += 50

    # ... (Rest of your code)

    # show appropriate images in windows
    cv2.imshow('Gesture', img)
    all_img = np.hstack((drawing, crop_img))
    # not necessary to show contours and can be skipped
    cv2.imshow('Contours', all_img)

    k = cv2.waitKey(10)
    if k == 27:
        break
