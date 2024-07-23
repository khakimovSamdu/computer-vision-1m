import cv2
import mediapipe as mp
import time

pTime = 0
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=10)

landmark_draw_spec = mpDraw.DrawingSpec(color=(2, 247, 27), thickness=1, circle_radius=2)
connection_draw_spec = mpDraw.DrawingSpec(color=(2, 247, 27), thickness=1, circle_radius=2)
img = cv2.imread('C:/Users/Xakimov Allamurod/Documents/Computer vision/computer-vision-1m/images/image9.jpg')

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = faceMesh.process(imgRGB)
if results.multi_face_landmarks:
    for faceLms in results.multi_face_landmarks:
        mpDraw.draw_landmarks(
                img, 
                faceLms, 
                mpFaceMesh.FACEMESH_TESSELATION , 
                landmark_draw_spec, 
                connection_draw_spec
        )
        for id, lm in enumerate(faceLms.landmark):
            ih, iw, _ = img.shape
            x, y = int(lm.x * iw), int(lm.y * ih)
            print(id, x, y)

cTime = time.time()
fps = 1 / (cTime - pTime)
pTime = cTime
cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
cv2.imshow("Image", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
