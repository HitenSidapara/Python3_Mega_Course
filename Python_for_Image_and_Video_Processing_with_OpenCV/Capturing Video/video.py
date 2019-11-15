import cv2, time

video = cv2.VideoCapture(0)

a=0

while True:
    a+=1
    # boolean, numpyarray
    check, frame = video.read()

    print(check)
    print(frame)

    cv2.imshow("Capturing", frame)
    cv2.imwrite(f"image_{a}.jpg",frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(f"Value of a is : {a}")
video.release()
cv2.destroyAllWindows()