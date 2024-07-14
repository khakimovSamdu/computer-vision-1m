import cv2 as cv

harcascade = "model/haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(harcascade)
lst = []
def read_image(filname):
    image = cv.imread(filename=filname)
    gray =  cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return image, gray

image, gray = read_image('images/image1.jpg')
image2, gray2 = read_image('images/image2.jpg')
tasvir1 = gray[251: 251+250, 79: 79+250]
tasvir2 = gray2[321: 321+110, 1000: 1000+110]
# tasvir2 = gray2[357: 357+110, 717: 717+110]
x, y = tasvir1.shape
tasvir2 = cv.resize(tasvir2, (x, y))
# border qo'shish
# tasvir2 = cv.copyMakeBorder(tasvir2, 70, 70, 70, 70, cv.BORDER_CONSTANT)
[717, 357, 110, 110]
print(tasvir1.shape)
print(tasvir2.shape)
mudir = [ 79, 297,  80,  80]
akbar = [308, 337,  77,  77]
asliddin = [1000,  321,  110,  110]
if tasvir1.shape == tasvir2.shape:
    difference = cv.norm(tasvir1, tasvir2, cv.NORM_INF)
    print(difference)
    if difference == 0:
        print(True)
    else:
        print(False)
else:
    print(False)

cv.imshow('Face1', tasvir1)
cv.waitKey(0)
cv.imshow('Face2', tasvir2)
cv.waitKey(0)