import cv2

img = cv2.imread("Images/2.jpg", 0)
print(img)
print(img.shape)

cv2.imshow("Legend",img)
cv2.waitKey(0)
cv2.destroyAllWindows()