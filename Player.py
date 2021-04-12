import cv2
import os
import time
import pickle
import tkinter 

path = "C:/Users/Dell/Desktop/Bad-apple-in-python-master/"                        
with open(path + '0.dat', 'rb') as fp:
    strings = pickle.load(fp)                                                                          

window = tkinter.Tk()                                                                                   
window.title('Bad Apple') 
window.geometry('1500x720') 
player = tkinter.Label(window, font=('Courier', 8))                           
player.place(x = 0,y = 0)                                    
for each in strings:
    player['text'] = each
    time.sleep(1/30)
    window.update()
window.mainloop()