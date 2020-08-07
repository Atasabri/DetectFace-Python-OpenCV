
import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"MP4V")
out = cv2.VideoWriter("out.mp4", fourcc, 20.0, (640, 480))

face_cascade = cv2.CascadeClassifier("facedetectdataset.xml")


def getframe():
    ret, frame = cap.read()
    # Add To Out Video File
    # out.write(frame)
    # Detect Face
    face_rects = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        break
    # Show Image
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()


@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')


def gen():
    while True:
        # get camera frame
        frame = getframe()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run()
