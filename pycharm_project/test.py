import pytesseract
import cv2
import time
import os

def get_text(filename):
    # load the example image and convert it to grayscale
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the
    # image
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    # gray = cv2.medianBlur(gray, 5)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    temp = time.time()
    text = pytesseract.image_to_string(gray)
    print(filename + " >>> " + str(time.time() - temp))
    print(text)
    print()

    # show the output images
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