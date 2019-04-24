import cv2
import numpy as np
import glob
import math

#empty list to store template images
template_data=[]
#make a list of all template images from a directory
files1 = glob.glob('C:\\Users\\laksh\\PycharmProjects\\evaluating-bolt-loosening\\src\\template*.png')

for myfile in files1:
    image = cv2.imread(myfile, 0)
    template_data.append(image)

test_image = cv2.imread('cannyImage.png')
test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

my_list = list()

#loop for matching
for tmp in template_data:
    (tH, tW) = tmp.shape[:2]
    print('Height n Width of the the template image:', 'Height:', tH, 'Width:', tW)
    cv2.imshow("Template", tmp)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    result = cv2.matchTemplate(test_image, tmp, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + tW, top_left[1] + tH)
    cv2.rectangle(test_image, top_left, bottom_right, 255, 1)

    print('rec', top_left, bottom_right)

    my_list.insert(0, top_left)

cv2.line(test_image, (my_list[1][0], my_list[1][1]), (my_list[0][0], my_list[0][1]), 255, 2)
#cv2.line(test_image, (338, 320), (389, 403), 255, 2)
#print(my_list[1][0])

x = my_list[1][0] - my_list[0][0]
y = my_list[1][1] - my_list[0][1]

gap = (x*x) + (y*y)
gap = math.sqrt(gap)
print('Gap in Pixels', gap)
print('Gap in Centimeters', (gap*2.54/96))
cv2.imwrite('final.png', test_image)
if gap > 84.0:
    print('Bolt-loosening Detected')
else:
    print('Bolt Fixed')
cv2.imshow('Result', test_image)
cv2.waitKey(0)
