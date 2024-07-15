import cv2 as cv
import time
harcascade = "C:/Users/Xakimov Allamurod/Documents/Computer vision/computer-vision-1m/model/haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(harcascade)
video_capture = cv.VideoCapture(0)
while True:
    ret, image = video_capture.read()
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    print("Found {0} faces!".format(len(faces)))
    
    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv.imshow("Faces found", image)
    cv.imwrite('new_face_image.jpg', image)
    if cv.waitKey(1) and 0xFF == ord('q'):
        break
    
video_capture.release()
cv.destroyAllWindows()