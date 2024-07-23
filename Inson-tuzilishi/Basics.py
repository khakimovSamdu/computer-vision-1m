import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

# Face masks
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=10)
landmark_draw_spec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=2)
connection_draw_spec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=2)

cap = cv2.VideoCapture(0)
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    face_results = faceMesh.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(h, w, c)
            print(lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
    # Face loadmasks
    if face_results.multi_face_landmarks:
        for faceLms in face_results.multi_face_landmarks:
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
                # print(id, x, y)
    else:
        x_img, y_img, c = img.shape
        cv2.putText(img, 'Kameraga yaqinroq keling', (y_img-500, 120), cv2.FONT_HERSHEY_PLAIN, 2,
                (0, 0, 255), 2)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
