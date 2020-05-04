import numpy as np
import cv2
import sys
import imutils
from imutils import contours

sys.path.insert(0, "E:\\project")
from dnn_softmax import *
from calculator import *
import pickle

font1 = cv2.FONT_HERSHEY_SIMPLEX
file = "parameters.pkl"
inpf = open(file, "rb")
parameters = pickle.load(inpf)
inpf.close()
a = ""
b = 0
stack = []
dig_count = 0
drawing = False
window_name = 'CALCULATOR MODE'
cv2.namedWindow(window_name)
img = np.zeros((1012, 1012, 3), np.uint8)
img3 = np.zeros((1012, 1012, 3), np.uint8)
img3 = img3 + 255
cv2.rectangle(img, (0, 720), (1012, 1012), (255, 255, 255), -1)
cursor = -100


def draw(event, x, y, flags, param):
    global drawing
    global cursor
    global font1
    global a
    global dig_count
    global b
    global stack
    cv2.rectangle(img, (0, 0), (1012, 100), (0, 255, 255), -1)
    cv2.rectangle(img, (253, 100), (759, 200), (0, 255, 255), -1)
    cv2.rectangle(img, (0, 100), (253, 200), (0, 255, 255), -1)
    cv2.rectangle(img, (759, 100), (1012, 200), (0, 255, 255), -1)
    cv2.line(img, (0, 100), (1012, 100), (0, 0, 255), 3)
    cv2.line(img, (0, 200), (1012, 200), (0, 0, 255), 3)
    cv2.line(img, (759, 200), (1012, 200), (0, 0, 255), 3)
    cv2.line(img, (0, 0), (1012, 0), (0, 0, 255), 3)
    cv2.line(img, (253, 100), (253, 200), (0, 0, 255), 3)
    cv2.line(img, (759, 100), (759, 200), (0, 0, 255), 3)
    cv2.line(img, (0, 0), (0, 200), (0, 0, 255), 3)
    cv2.line(img, (1010, 0), (1012, 200), (0, 0, 255), 3)

    if (x > 0 and x < 253 and y > 0 and y < 100):
        cv2.rectangle(img, (0, 0), (253, 100), (0, 0, 255), -1)
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.putText(img, '+', (cursor + 100, 800), font1, 4, (146, 21, 126), 10, cv2.LINE_AA)
            cursor = cursor + 100
            a = a + " + "
    if (x > 253 and x < 506 and y > 0 and y < 100):
        cv2.rectangle(img, (253, 0), (506, 100), (0, 0, 255), -1)
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.putText(img, '-', (cursor + 100, 800), font1, 4, (146, 21, 126), 10, cv2.LINE_AA)
            cursor = cursor + 100
            a = a + " - "
    if (x > 506 and x < 759 and y > 0 and y < 100):
        cv2.rectangle(img, (506, 0), (759, 100), (0, 0, 255), -1)
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.putText(img, '*', (cursor + 150, 800), font1, 4, (146, 21, 126), 10, cv2.LINE_AA)
            cursor = cursor + 100
            a = a + " * "
    if 759 < x < 1012 and 0 < y < 100:
        cv2.rectangle(img, (759, 0), (1012, 100), (0, 0, 255), -1)
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.putText(img, '/', (cursor + 100, 820), font1, 4, (146, 21, 126), 10, cv2.LINE_AA)
            cursor = cursor + 100
            a = a + " / "
    if 759 < x < 1012 and 100 < y < 200:
        cv2.rectangle(img, (759, 100), (1012, 200), (0, 0, 255), -1)
        if event == cv2.EVENT_LBUTTONDOWN:
            cursor = -100
            cv2.rectangle(img, (0, 700), (1012, 1012), (255, 255, 255), -1)
            img[200:690, 0:1012, ...] = 0
            a = ""
            img3[img3 != 255] = 255

    if 253 < x < 759 and 100 < y < 200:
        cv2.rectangle(img, (253, 100), (759, 200), (0, 0, 255), -1)
        if event == cv2.EVENT_LBUTTONDOWN:
            result = calculator(a)
            cv2.rectangle(img, (0, 700), (1012, 1012), (255, 255, 255), -1)
            cursor = -100
            a = ""
            cv2.putText(img, str(result), (cursor + 100, 820), font1, 4, (146, 21, 126), 10, cv2.LINE_AA)

    if 0 < x < 253 and 100 < y < 200:
        cv2.rectangle(img, (0, 100), (253, 200), (0, 0, 255), -1)
        if event == cv2.EVENT_LBUTTONDOWN:
            img10 = img[250:650, 0:1012]
            # img10=cv2.resize(img10,(700,200))
            grayimg = cv2.cvtColor(img10, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(grayimg, (5, 5), 0)
            ret, thresh = cv2.threshold(blur, 25, 200, 0)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
            thresh[thresh != 0] = 255
            print(thresh.shape)
            # cv2.imshow("man",thresh)
            # contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE )
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            print(len(cnts))
            # cv2.drawContours(img3,contours,-1,(0,0,0),15)
            i = 0
            # print(sizeof(cnts))
            ans3 = 0
            cnts = contours.sort_contours(cnts, method="left-to-right")[0]
            # print(digitCnts[0].shape)
            for c in cnts:
                (x, y, w, h) = cv2.boundingRect(c)
                dig = thresh[y:y + h, x:x + w]
                if dig.shape[1] > dig.shape[0]:
                    pad = (dig.shape[1] - dig.shape[0]) // 2
                    dig = np.pad(dig, ((pad, pad), (0, 0)), 'constant', constant_values=(0,))
                else:
                    pad = (dig.shape[0] - dig.shape[1]) // 2
                    dig = np.pad(dig, ((0, 0), (pad, pad)), 'constant', constant_values=(0,))
                dig = cv2.resize(dig, (28, 28))
                dig = np.pad(dig, ((12, 12),), 'constant', constant_values=(0,))
                dig = cv2.resize(dig, (28, 28))
                # cv2.imshow("frame",dig)
                # cv2.waitKey(0)
                dig = np.array(dig)
                dig = dig.flatten()
                dig = dig.reshape(dig.shape[0], 1)
                AL, _ = L_layer_forward(dig, parameters)
                ans3 = ans3 * 10 + np.argmax(AL)
                print(ans3)
                # img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                # img=cv2.putText(img,str(ans3),(x-5,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,255,0),2)
                i = i + 1
            # cv2.imshow("frame",img)
            # cv2.imwrite("digrec.jpg",img)
            # print(ans3)
            cv2.putText(img, str(ans3), (cursor + 100, 820), font1, 4, (0, 0, 255), 10, cv2.LINE_AA)
            if i > 2:
                cursor = cursor + 75 * (i)
            else:
                cursor = cursor + 75 * (i)
            a = a + str(ans3)
            drawing = False
            img[200:690, 0:1012, ...] = 0
            img3[img3 != 255] = 255
            b = 0
            i = 0

    cv2.line(img, (253, 0), (253, 100), (0, 0, 255), 3)
    cv2.line(img, (506, 0), (506, 100), (0, 0, 255), 3)
    cv2.line(img, (759, 0), (759, 100), (0, 0, 255), 3)
    cv2.putText(img, '=', (500, 175), font1, 2, (0, 165, 255), 2, cv2.LINE_AA)
    cv2.putText(img, 'CLEAR', (790, 175), font1, 2, (0, 165, 255), 2, cv2.LINE_AA)
    cv2.putText(img, 'SUBMIT', (10, 175), font1, 2, (0, 165, 255), 2, cv2.LINE_AA)
    cv2.putText(img, '+', (90, 90), font1, 4, (146, 21, 126), 2, cv2.LINE_AA)
    cv2.putText(img, '-', (333, 90), font1, 4, (146, 21, 126), 2, cv2.LINE_AA)
    cv2.putText(img, '*', (586, 90), font1, 4, (146, 21, 126), 2, cv2.LINE_AA)
    cv2.putText(img, '/', (820, 50), font1, 4, (146, 21, 126), 2, cv2.LINE_AA)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True;

    elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
        cv2.circle(img, (x, y), 8, (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


cv2.setMouseCallback(window_name, draw)


def main():
    global contours
    global cursor
    global font1
    global a

    while (True):
        cv2.imshow(window_name, img)

        if cv2.waitKey(20) == 27:
            break
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    b = 0
    c = 0
    print(a)


if __name__ == "__main__":
    main()
