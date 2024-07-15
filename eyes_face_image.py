import cv2 as cv

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors, minSize=(40, 40))
    coords = []
    for (x, y, w, h) in features:
        cv.rectangle(img, (x, y), (x+w, y+h), color, 2)
        cv.putText(img, text, (x, y-4), cv.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv.LINE_AA)
        coords.append([x, y, w, h])
    return coords
    
def detect(img, faceCascade, eyesCascade):
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0)}
    coords = draw_boundary(img, faceCascade, 1.1, 5, color['green'], "Face")
    print('Coords', (coords))
    for item in coords:
        roi_img = img[item[1]: item[1]+item[3], item[0]: item[0]+item[2]]
        coords = draw_boundary(roi_img, eyesCascade, 1.1, 10, color['red'], "Eyes")
    return img

faceCascade = cv.CascadeClassifier("model/haarcascade_frontalface_default.xml")
eyesCascade = cv.CascadeClassifier('model/haarcascade_eye.xml')

img = cv.imread('images/image2.jpg')
img = detect(img, faceCascade, eyesCascade)
cv.imshow('Face detection', img)
cv.waitKey(0)
