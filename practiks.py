import cv2 as cv 

harcascade = "C:/Users/Xakimov Allamurod/Documents/Computer vision/computer-vision-1m/model/haarcascade_frontalface_default.xml"
cap = cv.VideoCapture(0)
cap.set(3, 640) # width
cap.set(4, 480) # height

while True:
    success, img = cap.read()
    facecascade = cv.CascadeClassifier(harcascade)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face = facecascade.detectMultiScale(img_gray, 1.1, 4)

    cv.imshow('Face', img_gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    
