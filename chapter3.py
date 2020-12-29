import cv2

img = cv2.imread("Resources\image.png")
print(img.shape)

imgResize = cv2.resize(img, (300,200))
print(imgResize.shape)

imgCrop = img[0:200, :]

cv2.imshow("Image", imgCrop)
cv2.waitKey(0)