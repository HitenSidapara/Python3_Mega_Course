"""
exercise : reduce image size into 100 * 100 pixel
"""

import cv2
import glob

images = glob.glob("*.jpg")
print(images)


for image in images:
    img = cv2.imread(image,1)
    resize = cv2.resize(img,(100,100))
    cv2.imshow("Image",resize)
    cv2.imwrite("resize_"+image,resize)
    cv2.waitKey(500)
    cv2.destroyAllWindows()