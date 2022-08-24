from itertools import count
import cv2


image = cv2.imread("C:/Users/Ata Sabri/OneDrive/Desktop/Folder/test.jpg")
face_cascade = cv2.CascadeClassifier("facedetectdataset.xml")


face_rects = face_cascade.detectMultiScale(image, 1.3, 5)

count = 0

for (x, y, w, h) in face_rects:
    count += 1
    cv2.rectangle(image, (x, y), (x+w, y+h), (100, 100, 55), 2)
    cv2.putText(image, f'face {count}', (x, y),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)


cv2.imshow("Test Window", image)
cv2.waitKey(10000)
