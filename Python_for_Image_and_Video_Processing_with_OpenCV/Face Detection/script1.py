import cv2

face_casecade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img = cv2.imread("photo.jpg")
img = cv2.imread("news.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# here faces detect the 4 cordinate of the image x,y,width and height

faces = face_casecade.detectMultiScale(gray_img,
                                       scaleFactor=1.1,
                                       minNeighbors=5)

print(faces)

# draw the co-ordinates on image

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h),(0,255,9),5)
    #(x axis , y axis),(width , height),(color of line),(line thickness)


# resize image

resize_image = cv2.resize(img,(720,480))

cv2.imshow("Image", resize_image)
cv2.imwrite("image_detect.jpg", resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()