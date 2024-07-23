import cv2 as cv

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors, minSize=(40, 40))
    coords = []
    for (x, y, w, h) in features:
        cv.rectangle(img, (x, y), (x+w, y+h), color, 2)
        cv.putText(img, text, (x, y-4), cv.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv.LINE_AA)
        coords = [x, y, w, h]
    return coords
    
def detect(img, faceCascade, eyesCascade):
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0)}
    coords = draw_boundary(img, faceCascade, 1.1, 5, color['green'], "Face")
    if len(coords) == 4:
        roi_img = img[coords[1]: coords[1]+coords[3], coords[0]: coords[0]+coords[2]]
        coords = draw_boundary(roi_img, eyesCascade, 1.1, 14, color['red'], "Eyes")
    return img
 
faceCascade = cv.CascadeClassifier("model/haarcascade_frontalface_default.xml")
eyesCascade = cv.CascadeClassifier('model/haarcascade_eye.xml')

video_capture = cv.VideoCapture(0)

while True:
    _, img = video_capture.read()
    img = detect(img, faceCascade, eyesCascade)
    cv.imshow('Face detection', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv.destroyAllWindows()

