import cv2


image = cv2.imread("flower.jpg")
re_image = cv2.resize(image,(500,500))
cv2.imshow("Flower", re_image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = cv2.resize(gray_image,(500,500))
cv2.waitKey(0)

inverted_image = 255 - gray_image
inverted_image = cv2.resize(inverted_image,(500,500))
cv2.waitKey()

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
pencil_sketch = cv2.resize(pencil_sketch,(500,500))
cv2.waitKey(0)

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)