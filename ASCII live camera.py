import tkinter
import time
import cv2.cv2 as cv2
import numpy as np

# Resize function
def resize(img, new_width = 50):
    width,height = img.shape
    ratio = width/height
    new_height = int(new_width * ratio)
    dim = (new_width,new_height)
    resized_image = cv2.resize(img, dim)
    return(resized_image)

# ASCII interpreter
ASCII_CHARS=["@","$","#","%","?","!","*",";",":","."," "]
def pixelsToASCII(img):
    characters = []
    for i in img:
        temp = []
        for j in i:
            temp.append(ASCII_CHARS[j//25])
        characters.append(temp)
    return(characters)
    
# Array -> string
def arrayToString(arr):
    ascii = ''
    for i in arr:
        ascii+= ' '.join(i)
        ascii+='\n'
    return ascii

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    # Initializing ASCII live window
    window = tkinter.Tk()                                                                                   
    window.title('ASCII_live_cam') 
    window.geometry('1500x720') 
    player = tkinter.Label(window, font=('Courier', 8))                           
    player.place(x = 0,y = 0)  
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        # ASCII code in here
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ASCII_converted = arrayToString(pixelsToASCII(resize(gray))) + "\n" 
        player['text'] = ASCII_converted
        window.update()
        cv2.imshow('my webcam', img)
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()