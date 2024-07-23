import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("../Vedios/1.mp4")
pTime = 0
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)

landmark_draw_spec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=2)
connection_draw_spec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=2)
out = cv2.VideoWriter('../Vedios/new_2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))
while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(
                img, 
                faceLms, 
                mpFaceMesh.FACEMESH_CONTOURS, 
                landmark_draw_spec, 
                connection_draw_spec
            )
            for id, lm in enumerate(faceLms.landmark):
                ih, iw, _ = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                print(lm)
                print(id, x, y)
            
    

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    out.write(img)
    
cap.release()
cv2.destroyAllWindows()
