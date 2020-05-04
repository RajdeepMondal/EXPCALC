import cv2
import random
import imutils
from dnn_softmax import *
import pickle

a = ""
b = 0
dig_count = 0
drawing = False
cursor = -100


file = "parameters.pkl"
inpf = open(file, "rb")
parameters = pickle.load(inpf)
inpf.close()
num = random.randint(0, 9)
font1 = cv2.FONT_HERSHEY_SIMPLEX
drawing = False
window_name = 'CHILD MODE'
cv2.namedWindow(window_name)
img = np.zeros((1012, 1012, 3), np.uint8)
img1 = np.zeros((1012, 1012, 3), np.uint8)
img3 = np.zeros((1012, 1012, 3), np.uint8)
img3 = img3 + 255
cv2.rectangle(img, (0, 720), (1012, 1012), (255, 255, 255), -1)
cv2.rectangle(img, (0, 0), (1012, 110), (0, 128, 255), -1)


def draw(event, x, y, flags, param):
    global drawing
    global font1
    global num
    global cursor
    global a
    global dig_count
    global b
    global img
    cv2.rectangle(img, (0, 110), (253, 200), (0, 255, 255), -1)
    cv2.rectangle(img, (0, 0), (1012, 110), (0, 128, 255), -1)
    cv2.rectangle(img, (759, 110), (1012, 200), (0, 255, 255), -1)
    cv2.putText(img, 'WRITE ' + str(num), (290, 90), font1, 2, (0, 0, 0), 2, cv2.LINE_AA)

    if (x > 0 and x < 253 and y > 100 and y < 200):
        cv2.rectangle(img, (0, 110), (253, 200), (0, 0, 255), -1)
        if event == cv2.EVENT_LBUTTONDOWN:
            img10 = img[250:650, 0:1012]
            img10 = cv2.resize(img10, (700, 200))
            grayimg = cv2.cvtColor(img10, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(grayimg, (5, 5), 0)
            ret, thresh = cv2.threshold(blur, 25, 200, 0)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
            # contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE )
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            # cv2.drawContours(img3,contours,-1,(0,0,0),15)
            i = 0
            # print(sizeof(cnts))
            ans3 = 0
            for c in cnts:
                (x, y, w, h) = cv2.boundingRect(c)
                dig = thresh[y:y + h, x:x + w]
                dig = cv2.resize(dig, (28, 28))
                dig = np.pad(dig, ((12, 12),), 'constant', constant_values=(0,))
                dig = cv2.resize(dig, (28, 28))
                dig = np.array(dig)
                dig = dig.flatten()
                dig = dig.reshape(dig.shape[0], 1)
                AL, _ = L_layer_forward(dig, parameters)
                ans3 = ans3 * 10 + np.argmax(AL)
                # img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                # img=cv2.putText(img,str(ans3),(x-5,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,255,0),2)
                i = i + 1
            # cv2.imshow("frame",img)
            # cv2.imwrite("digrec.jpg",img)
            print(ans3)

            # img4 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
            # img4 = cv2.GaussianBlur(img4,(5,5),0)
            # img4 = cv2.resize(img4,(28,28))
            # img4 = np.pad(img4,((12,12),),'constant',constant_values=(255,))
            # img4 = cv2.resize(img4,(28,28))
            # img4=255-img4
            # x = img4.reshape(784,1).astype('float32') / 255
            # AL,_=L_layer_forward(x,parameters)
            if b * 10 + np.argmax(AL) == num:
                cv2.putText(img, str(b * 10 + np.argmax(AL)) + "     CORRECT", (cursor + 100, 820), font1, 4,
                            (0, 255, 0), 10, cv2.LINE_AA)
            else:
                cv2.putText(img, str(b * 10 + np.argmax(AL)) + "       WRONG", (cursor + 100, 820), font1, 4,
                            (0, 0, 255), 10, cv2.LINE_AA)
            if dig_count > 2:
                cursor = cursor + 50 * (dig_count + 1)
            else:
                cursor = cursor + 75 * (dig_count + 1)
            a = a + str(b * 10 + np.argmax(AL))
            drawing = False
            img[200:690, 0:1012, ...] = 0
            img3[img3 != 255] = 255
            b = 0
    cv2.putText(img, 'SUBMIT', (10, 175), font1, 2, (0, 165, 255), 2, cv2.LINE_AA)
    cv2.putText(img, 'NEW', (790, 175), font1, 2, (0, 165, 255), 2, cv2.LINE_AA)
    if (x > 759 and x < 1012 and y > 100 and y < 200):
        cv2.rectangle(img, (759, 110), (1012, 200), (0, 0, 255), -1)
        if event == cv2.EVENT_LBUTTONDOWN:
            cursor = -100
            cv2.rectangle(img, (0, 700), (1012, 1012), (255, 255, 255), -1)
            img[200:690, 0:1012, ...] = 0
            img3[img3 != 255] = 255
            num = random.randint(0, 9)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True;

    elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
        cv2.circle(img, (x, y), 8, (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


cv2.setMouseCallback(window_name, draw)


def main():
    global contours
    global font1
    global num
    while (True):
        cv2.imshow(window_name, img)
        if cv2.waitKey(20) == 27:
            break
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
