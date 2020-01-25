import pytesseract
import cv2

IS_DEBUG = True

dataset = {}
def read_dataset():
    description = open("mask/description.txt", "r+")
    line = description.readline()
    number = 0
    while (line == "---\n"):
        lines = []
        for i in range(2):
            lines.append(description.readline().strip())
        dataset[lines[1]] = {}
        gray = cv2.cvtColor(cv2.imread("mask/" + lines[0]), cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        (x, y, w, h) = cv2.boundingRect(contours[0])
        dataset[lines[1]]['xywh'] = (x, y, w, h)
        dataset[lines[1]]['order'] = number
        number += 1
        line = description.readline()
    description.close()

def parse_data(filename):
    data = cv2.imread("images/" + filename)
    parsed = {}
    for name in dataset:
        parsed[name] = {}
        (x,y,w,h) = dataset[name]['xywh']
        image = data[y:(y+h), x:(x+w)]
        image = cv2.resize(image, None, fx=7, fy=7, interpolation=cv2.INTER_CUBIC)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255,
                                 cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        #gray = cv2.medianBlur(gray, 3)
        config = ("-l rus --oem 2 --psm 7")
        text = pytesseract.image_to_string(gray, config=config)
        parsed[name] = text

        if (IS_DEBUG):
            cv2.namedWindow(name, cv2.WINDOW_NORMAL)
            cv2.imshow(name, image)
            cv2.imshow(name+"_gray", gray)
    if (IS_DEBUG):
        print_ordered(parsed)
        print("\nwaiting for key \'q\' to continue")
        key = cv2.waitKey(0)
        while (key != ord('q')):
            key = cv2.waitKey(0)
    return parsed

def print_ordered(parsed):
    ordered = [None]*len(dataset)
    for data in dataset:
        ordered[dataset[data]['order']] = data
    print()
    for i in range(len(ordered)):
        print(ordered[i] + " >>> " + parsed[ordered[i]])

def main():
    read_dataset()
    parsed = parse_data("data.png")
    print_ordered(parsed)

if __name__ == "__main__":
    main()