import cv2


#path to image
img_location = 'tower.jpg'
#save as
saveas = "pencil6.jpg"


img = cv2.imread(img_location)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
pencil_sketch_img = cv2.divide(gray_img, blurred_gray_img, scale=260)
#300
#200
cv2.imwrite(saveas, pencil_sketch_img)
cv2.imshow("org", img)
cv2.imshow("gray", pencil_sketch_img)
cv2.waitKey(0)
