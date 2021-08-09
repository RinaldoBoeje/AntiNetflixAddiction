#Information sources: 
#https://www.geeksforgeeks.org/python-using-pil-imagegrab-and-pytesseract/

#steps: 
#1: using PIL (imageGrab) take a shot of the screen
#2: using pyTesseract look on screen for x
#   x = inputted Text
#3: if x is found, start a 15 second countdown to "application" shutdown. Or "pc" shutdown
#   make compatible with Windows and Linux machines, Fuck Mac OSX

import os
import platform
import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab


input == "Next Episode"

#Take image of screen
def screenGrab():
    #take image of screen
    #TODO: Remove
    print("screenGrab test")
    foundString = "placeholder"

    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd ='**Path to tesseract executable**'
    while(True):
  
        # ImageGrab-To capture the screen image in a loop. 
        # Bbox used to capture a specific area.
        cap = ImageGrab.grab(bbox =(700, 300, 1400, 900))
  
        # Converted the image to monochrome for it to be easily 
        # read by the OCR and obtained the output String.
        foundString = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
                lang ='eng')
        print(foundString)

    return foundString


#look on screen for x
def screenSearch(inputString, foundString):
    #search on screen
    #TODO: Remove
    if inputString == foundString:
        systemShutdown


#shutdown system
def systemShutdown():
    system = platform.system()

    if system == 'Windows':
        #Windows based
        os.system("shutdown /s /t 1")        
    elif system == 'Linus' or system == 'Darwin':
        #unix based
        os.system("poweroff")
    else:
        #fucking try unix based shit again
        os.system("shutdown now -h")

#main
def main():
    screenSearch(input, screenGrab())
