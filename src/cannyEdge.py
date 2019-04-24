import cv2

srcImage = cv2.imread('t1.jpg')

srcImageResize = cv2.resize(srcImage, (600, 700))
image_gray = cv2.cvtColor(srcImageResize, cv2.COLOR_RGB2GRAY)
blurImage = cv2.GaussianBlur(image_gray, (5, 5), cv2.BORDER_DEFAULT)
cannyImage = cv2.Canny(blurImage, 200, 300)

#cv2.imshow('Original_Image', srcImage)
cv2.imshow('Resize_Image', image_gray)
cv2.imshow('Blurred_Image', blurImage)
cv2.imshow('Canny_Image', cannyImage)
cv2.imwrite('cannyImage.png', cannyImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
