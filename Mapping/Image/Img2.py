import cv2

img=cv2.imread("Lighthouse.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

cv2.imshow("Lighthouse",img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
