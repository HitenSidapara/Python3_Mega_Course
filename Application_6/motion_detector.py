import cv2, time
import pandas as pd
from datetime import datetime

first_frame = None
status_list = [None, None]
date_list = []
df = pd.DataFrame(columns=["Start Time", "End Time"])
video = cv2.VideoCapture(0)

while True:
    # boolean, numpyarray
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cuts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cuts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+h,y+w), (0,255,0),5)

    status_list.append(status)
    
    status_list = status_list[-2:]

    if status_list[-1]==1 and status_list[-2]==0:
        date_list.append(datetime.now())

    if status_list[-1] == 0 and status_list[-2] == 1:
        date_list.append(datetime.now())

    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Thresh Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        if status==1:
            date_list.append(datetime.now())
        break

print(date_list)

for i in range(0,len(date_list),2):
    df = df.append({"Start Time": date_list[i], "End Time": date_list[i+1]}, ignore_index=True)


df.to_csv("times.csv")
video.release()
cv2.destroyAllWindows()