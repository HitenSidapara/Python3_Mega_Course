import cv2

"""
    0 indicates the back and white image => 2 dimension numpy array
    1 indicate rgb color image => 3 dimarsion numpy array
    -1 indicate rgba color image
"""

img = cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)

# resize image

img_resized = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

cv2.imwrite("Galaxy_resized.jpg", img_resized)
cv2.imshow("Galaxy", img_resized)
cv2.waitKey(2000)
cv2.destroyAllWindows()