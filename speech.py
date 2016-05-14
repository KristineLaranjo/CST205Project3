import speech_recognition
import Scraper

recognizer = speech_recognition.Recognizer()

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

print 'Say an emotion'
command = listen()
print command
i = True

while i == True:
    if command == "smile":
        print Scraper.getimage("smiling-face-with-open-mouth-and-smiling-eyes")
        print "\n:)"
    elif command == "sad":
        i = False
        print Scraper.getimage("crying-face")
        print "\n:("
    elif command == "excited":
        i = False
        print Scraper.getimage("jack-o-lantern")
        print "\n:O"
    elif command == "upset":
        i = False
        print Scraper.getimage("angry-face")
        print "\n>:("
    else:
        print command
        print "Could not recognize: Please Try Again"
        command = listen()