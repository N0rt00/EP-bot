from PIL import Image
import os
import time
import pyscreenshot as ImageGrab
for i in range(1):
    im = ImageGrab.grab()
    im.save('fullscreen.png')
im = Image.open ('fullscreen.png')
left = -1000
top =  -1000
right = 600
bottom = 300
im1 = im.crop((left, top, right, bottom))
im1.save('fullscreen2.png')













    #if os.path.exists("fullscreen.png"):
        #os.remove("fullscreen.png")
