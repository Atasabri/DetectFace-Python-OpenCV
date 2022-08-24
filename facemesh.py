import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_faces = mp.solutions.face_mesh
##
faces = mp_faces.FaceMesh()
##
face_draw = mp.solutions.drawing_utils

drawSpec = face_draw.DrawingSpec(thickness=1, circle_radius= 2 )

while True:
    st, frame = cap.read()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    result = faces.process(rgb_frame)
##
    if result.multi_face_landmarks is not None:
##        
        for face in result.multi_face_landmarks:
##
            face_draw.draw_landmarks(frame,face,mp_faces.FACEMESH_CONTOURS,drawSpec,drawSpec)
            
    cv2.imshow('face detection',frame)

    if cv2.waitKey(30) & 0xff == ord('x'):
        break
    
cap.release()
cv2.destroyAllWindows()
