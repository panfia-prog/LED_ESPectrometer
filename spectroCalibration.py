import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

url = 'http://192.168.4.1:81/stream'
im=None

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-r", "--radius", type = int, help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', help='path to the image file')
ap.add_argument(
    '-r',
    '--radius',
    type=int,
    default=15,
    help='radius of Gaussian blur; must be odd',
)

def main():
    cap = cv2.VideoCapture(url)
    # Retrieve radius, defaulting to 15 if missing or <= 0
    radius = args.get("radius") or 15
    if radius <= 0:
        radius = 15

    # Ensure the radius is an odd number
    if radius % 2 == 0:
        radius += 1

    roi_selected = False

    while (True):
        ret, frame = cap.read()

        k = cv2.waitKey(1)

        if k & 0xFF == ord('1') and roi_selected:
            # 1. Crop to the selected ROI
            x, y, w, h = int(r[0]), int(r[1]), int(r[2]), int(r[3])
            cropped = frame[y: y + h, x: x + w]

            # Safety check to ensure valid ROI selection
            if cropped.size > 0:
                orig = cropped.copy()
                gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

                # 2. Apply Gaussian blur with the validated radius
                gray = cv2.GaussianBlur(gray, (radius, radius), 0)
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

                # 3. Draw circle on brightest spot in the ROI
                cv2.circle(orig, maxLoc, radius, (255, 0, 0), 2)

                print(f"ROI Minimum value: {minVal}")
                print(f"ROI Maximum value: {maxVal}")
                cv2.imshow("Brightest Spot in ROI", orig)
                cv2.waitKey(0)

        elif k & 0xFF == ord('r'):
            r = cv2.selectROI(frame)
            roi_selected = True

        elif k & 0xFF == ord('q'):
            break

        else:
            if roi_selected:
                cropped = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
                cv2.imshow('roi', cropped)
            else:
                cv2.imshow('ESP-32 Cam Stream', frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

#all white led
#concentrated red
# ROI Minimum value: 18.0
# ROI Maximum value: 163.0

#non concentrated red
# ROI Minimum value: 20.0
# ROI Maximum value: 173.0

#no sample
# ROI Minimum value: 21.0
# ROI Maximum value: 211.0