import cv2


cap = cv2.VideoCapture(0)

# fourcc = cv2.VideoWriter_fourcc(*"MP4V")
# out = cv2.VideoWriter("out.mp4", fourcc, 20.0, (640, 480))

face_cascade = cv2.CascadeClassifier("facedetectdataset.xml")


while True:
    ret, frame = cap.read()

    face_rects = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

        # cv2.circle(frame, (x+(w//2), y+(h//2)), w//2, (0, 0, 0), 2)
        # cv2.putText(frame, 'Ata Sabri', (x, y),
        # cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        #cv2.imwrite("ata.png", frame)
        break


cap.release()
# out.release()
# Close All opened Windows
cv2.destroyAllWindows()
