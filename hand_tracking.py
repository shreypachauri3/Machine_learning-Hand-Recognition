import cv2 as cv
import mediapipe as mp


cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    isTrue,frame = cap.read()
    imageRGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results = Hands.process(imageRGB)
    if results.multi_hand_landmarks:
        h , w ,c = frame.shape
        for landmarks in results.multi_hand_landmarks:
            data = list(landmarks.landmark)[0]
            cv.circle(frame,(int(w*data.x),int(h*data.y)),10,(255,0,0),thickness=3)
            mpDraw.draw_landmarks(frame , landmarks , mpHands.HAND_CONNECTIONS)
    cv.imshow("Image",frame)
    cv.waitKey(1)
