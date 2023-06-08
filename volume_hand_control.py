import cv2 as cv
import mediapipe as mp
import numpy as np
from hand_track import handDetector
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
cap = cv.VideoCapture(0)

detector =handDetector(min_detection_confidence=0.7)




devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
vol_range = (volume.GetVolumeRange())

min_Vol = vol_range[0]
max_Vol = vol_range[1]

while(True):
    success,frame = cap.read()
    detector.findHands(frame)
    lmlist = detector.findPosition(frame)
    if(len(lmlist)!=0):
        
        x1 , y1 = lmlist[4][1],lmlist[4][2]
        x2 , y2 = lmlist[8][1],lmlist[8][2]
        cv.circle(frame,(x1,y1),15,(255,0,255),cv.FILLED)
        cv.circle(frame,(x2,y2),15,(255,0,255),cv.FILLED)
        cv.line(frame,(x1,y1),(x2,y2),(255,0,255),3)
        cv.circle(frame,((x1+x2)//2,(y1+y2)//2),15,(255,0,255),cv.FILLED)
        length = math.hypot(x2-x1,y2-y1)
        vol = np.interp(length,[10,250],[min_Vol,max_Vol])
        volume.SetMasterVolumeLevel(vol, None)
    cv.imshow('Main_window',frame)
    cv.waitKey(1)