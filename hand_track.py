import cv2 as cv
import mediapipe as mp

class handDetector():
    def __init__(self,
               static_image_mode=False,
               max_num_hands=2,
               model_complexity=1,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5):
        self.static_image_mode  = static_image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity = model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.mpHands = mp.solutions.hands
        self.Hands = self.mpHands.Hands(self.static_image_mode,self.max_num_hands,self.model_complexity,self.min_detection_confidence,self.min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,frame,draw=True):
            imageRGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            self.results = self.Hands.process(imageRGB)
            if self.results.multi_hand_landmarks:
                h , w ,c = frame.shape
                for landmarks in self.results.multi_hand_landmarks:
                    if draw:
                        self.mpDraw.draw_landmarks(frame , landmarks , self.mpHands.HAND_CONNECTIONS)
            return frame            

    def findPosition(self , frame , handNo = 0, draw = True):

        lmlist = []
        if self.results.multi_hand_landmarks:
                h , w ,c = frame.shape
                if self.results.multi_hand_landmarks:
                    myHand=self.results.multi_hand_landmarks[0]
                    if draw:
                       for id,lm in enumerate(myHand.landmark):
                            h ,w,c =frame.shape
                            cx,cy = int(lm.x*w),int(lm.y*h)
                            lmlist.append([id,cx,cy])
                            cv.circle(frame,(int(cx),int(cy)),10,(255,0,0),thickness=3)
                            
        return lmlist


 








def main():
    cap = cv.VideoCapture(0)
    detector  = handDetector()
    while True:
        isTrue,frame = cap.read()
       
        detector.findHands(frame)
        lmlist = detector.findPosition(frame)
        if(lmlist!=0):
             print(lmlist)
        cv.imshow("Image",frame)
        cv.waitKey(1)



if __name__ == "__main__":
    main()
