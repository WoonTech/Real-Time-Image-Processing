import cv2
import numpy as np

template = cv2.imread('climbing.jpeg',0)
w, h = template.shape[::-1]
video_capture = cv2.VideoCapture(0)

while True:
    ret , frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if gray.shape[0]>template.shape[0] and gray.shape[1]>template.shape[1]:
        res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            cv2.putText(frame, "climbing", (250,150),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),2)
                
            
        cv2.imshow('orginal', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    
