import cv2 as cv

image = cv.imread('images/image1.jpg')

image_x, image_y, d =image.shape

resize_img = cv.resize(image, (100, 100))
gray_image = cv.cvtColor(resize_img, cv.COLOR_BGR2GRAY)
print(resize_img.shape)
t = 80
for row in range(image_x):
    for column in range(image_y):
        df = image[row][column]
        x, y, z = int(df[0]), int(df[1]), int(df[2])
        gray_pik = (x+y+z)//3
        # Segmentlashning birinchi usuli
        # print(gray_pik, t)
        if gray_pik<t:
            image[row][column] = 0
        else:
            image[row][column] = 255
        
print(image)
print(image.shape)
cv.imshow("Image", image)
cv.waitKey(0)