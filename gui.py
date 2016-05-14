#import Tkinter as tk
from Tkinter import *
from tkFileDialog import *
import tkMessageBox
from PIL import ImageTk, Image
import cv2
import numpy as np




class mikesButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.runButton = Button(frame, text = "Select an Emoji", command = self.runButton)
        self.runButton.pack()
        
        #self.picButton = Button(frame, text = "take a picture", command = self.picButton)
        #self.picButton.pack(side = LEFT)
        
        self.speechButton = Button(frame, text = "voice command", command = self.speechButton)
        self.speechButton.pack(side = LEFT)
        
        self.emotionButton = Button(frame, text = "prototype", command = self.emotionButton)
        self.emotionButton.pack(side = LEFT)
        
        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side = LEFT)
    
    
    def runButton(self):
        execfile("facedetection.py")
    
    def speechButton(self):
        execfile("speech.py")
    
    def emotionButton(self):
        execfile("face_detection.py")

#def picButton(self):
#execfile("screenshot.py")

root = Tk()

root.wm_title("Emoji Mask")


b = mikesButtons(root)


root.geometry("600x550+200+200")
root.mainloop()