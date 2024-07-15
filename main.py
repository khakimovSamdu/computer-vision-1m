import cv2 as cv
harcascade = "model/haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(harcascade)
image = cv.imread('images/image2.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
print(image.shape)
# prak_2_img = image[0: 80, 117: 207, :]

faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
print("Found {0} faces!".format(len(faces)))
kor = []
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    img_one = image[y: y+h, x: x+w]
    cv.imshow("Face", img_one)
    cv.waitKey(0)
for i in faces:
    kor.append(i)
print(kor)
cv.imshow("New face image", image)
# # cv.imwrite('new_face_image.jpg', image)
cv.waitKey(0)