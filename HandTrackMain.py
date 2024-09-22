#modules
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

#hand detection module
#tracking confidence
#max # of hands

mpHands = mp.solutions.hands
hands = mpHands.Hands()
#drawing mdl
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    #color conversion
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                #pixels
                h, w, c= img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #id which is wc=================
                print(id, cx, cy)
                #drawing points
                # if id ==4:
                cv2.circle(img, (cx, cy), 15,(255, 0, 255), cv2.FILLED )
            #connections drw
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
#pos size---------------------------------
    cv2.putText(img, str(int(fps)),(10, 70), cv2.FONT_HERSHEY_COMPLEX, 3,(0, 255, 0),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
