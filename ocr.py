import cv2
import pytesseract
from PIL import Image 


img = cv2.imread('trial/New folder/plain.jpg',1)   
img = cv2.resize(img, (400,400))
inverted = cv2.bitwise_not(img)
cv2.imwrite('new_img.jpg', inverted)
cv2.imshow('Image', inverted)
cv2.waitKey(0)   
 

ocr = pytesseract.image_to_string( inverted)
print("output: 1")
print(ocr)


img_file2 =  "trial/New folder/poster.jpg"
img2 = Image.open(img_file2)
ocr2 = pytesseract.image_to_string(img2)
print("output: 2")
print(ocr2)


img_file3 =  "trial/New folder/quest.jpg"
img3 = Image.open(img_file3)
ocr3 = pytesseract.image_to_string(img3)
print("output: 3")
print(ocr3)