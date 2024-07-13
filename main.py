import cv2 as cv
harcascade = "C:/Users/Xakimov Allamurod/Documents/Computer vision/computer-vision-1m/model/haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(harcascade)
image = cv.imread('images/image2.jpg')
# print(image.shape)
prak_1 = [365, 232, 184, 184]
prak_2 = [712, 351, 118, 118]
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

prak_2_img = (gray[78: 297, 78+81: 297+81])

faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
print("Found {0} faces!".format(len(faces)))
c = 0
for (x, y, w, h) in faces:
    
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print(faces[c])
    cv.imshow(f'Face {c}', image)
    c+=1
    cv.waitKey(0)
    print(image[x: x+w-1][y: y+h-1][:3])
    break

    
# print(faces[0])
# print(faces[1])
# cv.imshow('Face 1', image)
# cv.imshow("Face", prak_2_img)
# cv.imwrite('new_face_image.jpg', image)
cv.waitKey(0)