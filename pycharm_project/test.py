import pytesseract
import cv2
import time
import os

def get_text(filename):
    # load the example image and convert it to grayscale
    image = cv2.imread(filename)
    image = cv2.resize(image, None, fx=19, fy=19, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #low_green = (0, 0, 0)
    #high_green = (360, 255, 160)
    #gray = cv2.inRange(gray, low_green, high_green)

    #gray = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)

    temp = time.time()

    config = ("-l rus --oem 2 --psm 7")
    text = pytesseract.image_to_string(gray, config=config)
    print(filename + " >>> " + str(time.time() - temp))
    print(text)
    print()

    # show the output images
    cv2.namedWindow("Output"+filename, cv2.WINDOW_NORMAL)
    cv2.imshow("Output"+filename, gray)

path = 'images/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    get_text(f)

cv2.waitKey(0)
cv2.destroyAllWindows()
