import os
import time
import pyscreenshot as ImageGrab
for i in range(20)
  im = ImageGrab.grab()
  im.save('fullscreen.png')
  time.sleep(5)
  if os.path.exists("fullscreen.png"):
    os.remove("fullscreen.png")
