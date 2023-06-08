import cv2 as cv
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands=mp.solutions.hands


cap = cv.VideoCapture(0)
hands = mphands.Hands()
while True:
    isTrue,frame = cap.read()
    image = cv.cvtColor(cv.flip(frame,1),cv.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv.cvtColor(image,cv.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hl in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hl,mphands.HAND_CONNECTIONS
            )
    cv.imshow('Handtracker',image)
    cv.waitKey(1)