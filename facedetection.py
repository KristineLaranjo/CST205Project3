import cv2
import numpy as np
import Tkinter as tk
from PIL import Image, ImageTk

# Loads the picture
fileName = askopenfilename(parent=root)
emoji = cv2.imread(fileName, -1)#"./Emojis/lmfao.png"

# Created the cascades for the face and eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
glasses_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

# Opens the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 400)

while True:
    # Creates the frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detects faces, eyes, glasses in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    glasses = glasses_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Checks for user speech, CODE GOES HERE
        
    # I will make this for loop a function after we combine everything
    # This will take in the emotion, and convert the emotion to its
    # corresponding emoji, which will then be displayed on the user's face
        
    for(x,y,w,h) in faces:
        # Sets the region of interest in the frame, which is the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        #top-left start position of mouth
        my = y + ((h*3)/4) - 8
        mx = x + ((w*1)/3)
        mw = w/3
        mh = h/6
        
        #mouth = frame[my:mh,mx:mw]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        #cv2.rectangle(frame, (mx,my), (mx+mw,my+mh), (0,255,0), 2)
        mouth = mouth_cascade.detectMultiScale(roi_gray)
        
        for(mx,my,mw,mh) in mouth:
            cv2.rectangle(roi_gray, (mx,my), (mx+mw,my+mh), (0,255,0), 2)
            # Displays the the resulting frame
    cv2.imshow('Video',frame)

    # Quit
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
 
#Exits the webcam and terminates window      
cap.release()
cv2.destroyAllWindows()