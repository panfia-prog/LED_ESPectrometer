import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import math

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
    # constants
    redWavelength = 640
    greenWavelength = 565
    blueWavelength = 466
    yellowWavelength = 587
    orangeWavelength = 635
    infraredWavelength = 940

    redIncidentLight = 202
    greenIncidentLight = 215
    blueIncidentLight = 192
    yellowIncidentLight = 171
    orangeIncidentLight = 151

    global redTransmittedLight
    global greenTransmittedLight
    global blueTransmittedLight
    global yellowTransmittedLight
    global orangeTransmittedLight

    global redAbsorption
    global greenAbsorption
    global blueAbsorption
    global yellowAbsorption
    global orangeAbsorption

    # cap = cv2.VideoCapture(0)
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
                (minVal, redTransmittedLight, minLoc, maxLoc) = cv2.minMaxLoc(gray)

                # 3. Draw circle on brightest spot in the ROI
                cv2.circle(orig, maxLoc, radius, (255, 0, 0), 2)
                redAbsorption = -(math.log((redTransmittedLight/redIncidentLight),10))*100

                print("-----------------------------------------------")
                print(f"Red Incident Value (T0): {redIncidentLight}")
                print(f"Red Transmitted Value (T): {redTransmittedLight}")
                print(f"Red Absorbance Value: {redAbsorption}")
                print("-----------------------------------------------")

                cv2.imshow("Brightest Spot in ROI", orig)
                cv2.waitKey(1)

        if k & 0xFF == ord('2') and roi_selected:
            # 1. Crop to the selected ROI
            x, y, w, h = int(r[0]), int(r[1]), int(r[2]), int(r[3])
            cropped = frame[y: y + h, x: x + w]

            # Safety check to ensure valid ROI selection
            if cropped.size > 0:
                orig = cropped.copy()
                gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

                # 2. Apply Gaussian blur with the validated radius
                gray = cv2.GaussianBlur(gray, (radius, radius), 0)
                (minVal, greenTransmittedLight, minLoc, maxLoc) = cv2.minMaxLoc(gray)

                # 3. Draw circle on brightest spot in the ROI
                cv2.circle(orig, maxLoc, radius, (255, 0, 0), 2)
                greenAbsorption = -(math.log((greenTransmittedLight / greenIncidentLight), 10))*100

                print("-----------------------------------------------")
                print(f"Green Incident Value (T0): {greenIncidentLight}")
                print(f"Green Transmitted Value (T): {greenTransmittedLight}")
                print(f"Green Absorbance Value: {greenAbsorption}")
                print("-----------------------------------------------")

                cv2.imshow("Brightest Spot in ROI", orig)
                cv2.waitKey(1)

        if k & 0xFF == ord('3') and roi_selected:
            # 1. Crop to the selected ROI
            x, y, w, h = int(r[0]), int(r[1]), int(r[2]), int(r[3])
            cropped = frame[y: y + h, x: x + w]

            # Safety check to ensure valid ROI selection
            if cropped.size > 0:
                orig = cropped.copy()
                gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

                # 2. Apply Gaussian blur with the validated radius
                gray = cv2.GaussianBlur(gray, (radius, radius), 0)
                (minVal, blueTransmittedLight, minLoc, maxLoc) = cv2.minMaxLoc(gray)

                # 3. Draw circle on brightest spot in the ROI
                cv2.circle(orig, maxLoc, radius, (255, 0, 0), 2)
                blueAbsorption = -(math.log((blueTransmittedLight / blueIncidentLight), 10))*100

                print("-----------------------------------------------")
                print(f"Blue Incident Value (T0): {blueIncidentLight}")
                print(f"Blue Transmitted Value (T): {blueTransmittedLight}")
                print(f"Blue Absorbance Value: {blueAbsorption}")
                print("-----------------------------------------------")

                cv2.imshow("Brightest Spot in ROI", orig)
                cv2.waitKey(1)

        if k & 0xFF == ord('4') and roi_selected:
            # 1. Crop to the selected ROI
            x, y, w, h = int(r[0]), int(r[1]), int(r[2]), int(r[3])
            cropped = frame[y: y + h, x: x + w]

            # Safety check to ensure valid ROI selection
            if cropped.size > 0:
                orig = cropped.copy()
                gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

                # 2. Apply Gaussian blur with the validated radius
                gray = cv2.GaussianBlur(gray, (radius, radius), 0)
                (minVal, yellowTransmittedLight, minLoc, maxLoc) = cv2.minMaxLoc(gray)

                # 3. Draw circle on brightest spot in the ROI
                cv2.circle(orig, maxLoc, radius, (255, 0, 0), 2)
                yellowAbsorption = -(math.log((yellowTransmittedLight / yellowIncidentLight), 10))*100

                print("-----------------------------------------------")
                print(f"Yellow Incident Value (T0): {yellowIncidentLight}")
                print(f"Yellow Transmitted Value (T): {yellowTransmittedLight}")
                print(f"Yellow Absorbance Value: {yellowAbsorption}")
                print("-----------------------------------------------")

                cv2.imshow("Brightest Spot in ROI", orig)
                cv2.waitKey(1)

        if k & 0xFF == ord('5') and roi_selected:
            # 1. Crop to the selected ROI
            x, y, w, h = int(r[0]), int(r[1]), int(r[2]), int(r[3])
            cropped = frame[y: y + h, x: x + w]


            # Safety check to ensure valid ROI selection
            if cropped.size > 0:
                orig = cropped.copy()
                gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

                # 2. Apply Gaussian blur with the validated radius
                gray = cv2.GaussianBlur(gray, (radius, radius), 0)
                (minVal, orangeTransmittedLight, minLoc, maxLoc) = cv2.minMaxLoc(gray)

                # 3. Draw circle on brightest spot in the ROI
                cv2.circle(orig, maxLoc, radius, (255, 0, 0), 2)
                orangeAbsorption = -(math.log((orangeTransmittedLight / orangeIncidentLight), 10))*100

                print("-----------------------------------------------")
                print(f"Orange Incident Value (T0): {orangeIncidentLight}")
                print(f"Orange Transmitted Value (T): {orangeTransmittedLight}")
                print(f"Orange Absorbance Value: {orangeAbsorption}")
                print("-----------------------------------------------")

                cv2.imshow("Brightest Spot in ROI", orig)
                cv2.waitKey(1)

        if k & 0xFF == ord('s') and roi_selected:
            # 1. Crop to the selected ROI
            x, y, w, h = int(r[0]), int(r[1]), int(r[2]), int(r[3])
            cropped = frame[y: y + h, x: x + w]
            cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)

            # Safety check to ensure valid ROI selection
            if cropped.size > 0:
                print("-----------------------------------------------")
                print("Summarized List of Wavelength and Absorbances")
                print(f"Blue (466nm): {blueAbsorption}%")
                print(f"Green (565nm): {greenAbsorption}%")
                print(f"Yellow (587nm): {yellowAbsorption}%")
                print(f"Orange (635nm): {orangeAbsorption}%")
                print(f"Red (640nm): {redAbsorption}%")
                print("-----------------------------------------------")

                plt.subplot(3, 1, 1)
                plt.xticks([])
                plt.yticks([])
                plt.title('Full Spectrum (from White LED)')
                plt.imshow(cropped_rgb)

                plt.subplot(3,1,2)
                wavelengthList= [blueWavelength,greenWavelength,yellowWavelength,orangeWavelength,redWavelength]
                absorbanceAxis = [blueAbsorption,greenAbsorption,yellowAbsorption,orangeAbsorption,redAbsorption]
                barColors = ['blue', 'green', 'yellow', 'orange', 'red']
                wavelengthAxis = [f"{w} nm" for w in wavelengthList]
                plt.bar(wavelengthAxis, absorbanceAxis, color=barColors)

                plt.title('Absorbance VS Wavelength Graph')
                plt.xlabel('Wavelength (nm)')
                plt.ylabel('Absorbance (%)')

                plt.subplot(3, 1, 3)
                wavelengthList = [blueWavelength, greenWavelength, yellowWavelength, orangeWavelength, redWavelength]
                intensityAxis = [blueTransmittedLight, greenTransmittedLight, yellowTransmittedLight, orangeTransmittedLight, redTransmittedLight]
                barColors = ['blue', 'green', 'yellow', 'orange', 'red']
                wavelengthAxis = [f"{w} nm" for w in wavelengthList]
                plt.bar(wavelengthAxis, intensityAxis, color=barColors)

                plt.title('Intensity VS Wavelength Graph')
                plt.xlabel('Wavelength (nm)')
                plt.ylabel('Intensity')

                plt.tight_layout()
                plt.show()

            cv2.waitKey(1)

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