# import dlib
# import cv2 as cv
# import numpy as np

# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# def read_image(filename):
#     image = cv.imread(filename)
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     return image, gray

# def get_face_descriptor(image):
#     faces = detector(image)
#     for face in faces:
#         shape = predictor(image, face)
#         return np.array([p.x for p in shape.parts()] + [p.y for p in shape.parts()])
#     return None

# image1, gray1 = read_image('images/image1.jpg')
# image2, gray2 = read_image('images/image2.jpg')
# tasvir1 = gray1[251: 251+250, 79: 79+250]
# tasvir2 = gray2[321: 321+110, 1000: 1000+110]
# desc1 = get_face_descriptor(tasvir1)
# desc2 = get_face_descriptor(tasvir2)

# if desc1 is not None and desc2 is not None:
#     distance = np.linalg.norm(desc1 - desc2)
#     print("Euclidean masofasi:", distance)
#     if distance < 1000:  # Masofa kichik bo'lsa, tasvirlar o'xshash deb hisoblanadi
#         print("Tasvirlar o'xshash.")
#     else:
#         print("Tasvirlar o'xshash emas.")
# else:
#     print("Yuz tasvirlarini aniqlashda xato.")

import cv2 as cv
import numpy as np

def read_image(filename):
    image = cv.imread(filename)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return image, gray

image1, gray1 = read_image('images/image1.jpg')
image2, gray2 = read_image('images/image2.jpg')

# Tasvirlarni bir xil o'lchamga keltirish
resize_dim = (gray1.shape)

tasvir1 = gray1[251: 251+250, 79: 79+250]
tasvir2 = gray2[297: 297+80, 79: 79+80]
# tasvir2 = cv.copyMakeBorder(tasvir2, 85, 85, 85, 85, cv.BORDER_CONSTANT)
print(tasvir2.shape)
gray1_resized = cv.resize(tasvir1, resize_dim)
gray2_resized = cv.resize(tasvir2, resize_dim)
# HOG descriptorlarini chiqarish
hog = cv.HOGDescriptor()

h1 = hog.compute(gray1_resized)
h2 = hog.compute(gray2_resized)

# Descriptorlarni solishtirish uchun Euclidean masofasini hisoblash
distance = np.linalg.norm(h1 - h2)

print("Euclidean masofasi:", distance)

# O'xshashlik darajasini aniqlash
if distance < 1000:  # Masofa kichik bo'lsa, tasvirlar o'xshash deb hisoblanadi
    print("Tasvirlar o'xshash.")
else:
    print("Tasvirlar o'xshash emas.")

print(tasvir1.shape)


cv.imshow('Face', tasvir1)
cv.imwrite('face1.jpg', tasvir1)
cv.waitKey(0)
cv.imshow('Face2', tasvir2)
cv.waitKey(0)