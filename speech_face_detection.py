import cv2
import numpy as np
import speech_recognition
import Scraper
import addEmoji

# Created the cascades for the face and eyes
face_cascade = cv2.CascadeClassifier('./HaarCascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./HaarCascades/haarcascade_eye.xml')
glasses_cascade = cv2.CascadeClassifier('./HaarCascades/haarcascade_eye_tree_eyeglasses.xml')

recognizer = speech_recognition.Recognizer()
recognizer.energy_threshold = 3000

def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
	try:
		return recognizer.recognize_sphinx(audio)
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""

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
        
    for(x,y,w,h) in faces:
        print 'Say an emotion'
        command = listen()
    
        # Sets the region of interest in the frame, which is the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        if command == "smile" or command == "happy":
            emoji = cv2.imread("./Emojis/smile.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        elif command == "sad" or command == "crying":
            emoji = cv2.imread("./Emojis/crying.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        elif command == "shocked":
            emoji = cv2.imread("./Emojis/shocked.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        elif command == "upset" or command = "mad":
            emoji = cv2.imread("./Emojis/mad.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        elif command == "cool":
            emoji = cv2.imread("./Emojis/cool.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        elif command == "nervous":
            emoji = cv2.imread("./Emojis/nervous.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        elif command == "nerdy":
            emoji = cv2.imread("./Emojis/nerdy.png", -1)
            addEmoji.add(emoji, w, h, roi_color)
        else:
            print command
            print "Could not recognize: Please Try Again"
        
    # Displays the the resulting frame      
    cv2.imshow('Video',frame)

    # Quit
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
 
#Exits the webcam and terminates window      
cap.release()
cv2.destroyAllWindows()