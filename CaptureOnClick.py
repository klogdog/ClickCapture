import PIL.ImageGrab
import os
import time
from pynput import mouse

def captureImage():    
    capturedImage = PIL.ImageGrab.grab()
    fileName = 'capturedimage' + str(int(time.time())) + '.jpg'
    path = os.getcwd()
    path = os.path.join(path, fileName)
    capturedImage.save(path)

def mouseButtonClicked(x, y, button, pressed):
    if pressed:
        if button == button.x1:
            return False
        if button == button.left or button == button.right:
            captureImage()
    
mouseListener = mouse.Listener(on_click=mouseButtonClicked)
mouseListener.start()
mouseListener.join()
