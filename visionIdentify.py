import cv2 as cv
import numpy as np

testImageURL = "./testImg.png"

def main():
    #read the testimg
    img = cv.imread("testImg.png")
    img2 = img.copy()

    # Convert to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Define the color range
    lower = np.array([0, 0, 0])
    upper = np.array([50, 51, 255])

    # Create a mask for similar colors
    mask = cv.inRange(hsv, lower, upper)

    # Find contours in the mask
    contours, hierarchy = cv.findContours(
        mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )

    con2 = []

    #remove small contours
    for con in contours:
        x, y, w, h = cv.boundingRect(con)
        if ((w * h) > 5000):
            con2.append(con)

    #Biggest contours first
    con2 = sorted(con2, key=cv.contourArea, reverse=True)

    x = 0
    while (True):
        cv.drawContours(img, con2, x, (0, 255, 0), 3)
        cv.imshow("disp", img)
        x += 1
        img = img2.copy()
        if cv.waitKey() == 27:
            break;


main()

#NOTES
# This can create contours around the casting useing its HSV values. However, some areas of their enviroment also falll under the color ranger. It leads to bounding boxes bigger than intended. 
# I will need additional data to procced with making the boxes more accurate.
