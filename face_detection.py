import cv2
import numpy as np
import addEmoji

# Created the cascades for the face and eyes
face_cascade = cv2.CascadeClassifier('./HaarCascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./HaarCascades/haarcascade_eye.xml')
glasses_cascade = cv2.CascadeClassifier('./HaarCascades/haarcascade_eye_tree_eyeglasses.xml')

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
        
    for(x,y,w,h) in faces:
        # Sets the region of interest in the frame, which is the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_color, 1.3, 5)
        glasses = glasses_cascade.detectMultiScale(roi_color, 1.3, 5)
        
        #mouth detection
        my = y + ((h*3)/4) - 8
        mx = x + ((w*1)/3)
        mw = w/3
        mh = h/6
        #mouth = frame[my:mh,mx:mw]        

        #for(mx,my,mw,mh) in mouth:
            #cv2.rectangle(roi_gray, (mx,my), (mx+mw,my+mh), (0,255,0), 2)
        
        if(len(eyes) == 1):
            emoji = cv2.imread("./Emojis/wink.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        elif(len(eyes) == 0 and len(glasses) == 1):
            emoji = cv2.imread("./Emojis/cool.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        elif(len(glasses) == 1):
            emoji = cv2.imread("./Emojis/glasses.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        
    # Displays the the resulting frame      
    cv2.imshow('Video',frame)

    # Quit
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
 
#Exits the webcam and terminates window      
cap.release()
cv2.destroyAllWindows()