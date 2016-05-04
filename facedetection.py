import cv2
import numpy as np

# Loads the picture
emoji = cv2.imread("./Emojis/lmfao.png", -1)

# Created the cascades for the face and eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Create the mask for emoji
orig_mask = emoji[:,:,3]

# Create the inverted mask for the emoji
orig_mask_inv = cv2.bitwise_not(orig_mask)

# Convert emoji to BGR
# and save the original emoji size
emoji = emoji[:,:,0:3]
origEmojiHeight, origEmojiWidth = emoji.shape[:2]

# Opens the webcam
cap = cv2.VideoCapture(0)

while True:
    # Creates the frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detects faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Checks for user speech, CODE GOES HERE
    
    # I will make this for loop a function after we combine everything
    # This will take in the emotion, and convert the emotion to its
    # corresponding emoji, which will then be displayed on the user's face
    for(x,y,w,h) in faces:
        # Sets the region of interest in the frame, which is the face
        #roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # Resizes the emoji, mask, and mask_inv according to the face
        emoji = cv2.resize(emoji, (w,h), interpolation = cv2.INTER_AREA)
        mask = cv2.resize(orig_mask, (w,h), interpolation = cv2.INTER_AREA)
        mask_inv = cv2.resize(orig_mask_inv, (w,h), interpolation = cv2.INTER_AREA)

        # Sets the region of interest of the face
        roi = roi_color[0:w, 0:h]
        
        # Creates the background (face) and foreground (emoji)
        roi_bg = cv2.bitwise_and(roi,roi, mask = mask_inv)
        roi_fg = cv2.bitwise_and(emoji,emoji, mask = mask)
        
        # Overlays emoji to face
        dst = cv2.add(roi_bg,roi_fg)
        
        # Sets the layer back to the region of interest
        roi_color[0:h, 0:w] = dst
        
        #for(ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color, (ex, ey), (ex+ew,ey+eh), (0,255,0), 2)
      
    # Displays the the resulting frame      
    cv2.imshow('Video',frame)

    # Quit
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
 
#Exits the webcam and terminates window      
cap.release()
cv2.destroyAllWindows()