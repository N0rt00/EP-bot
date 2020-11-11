# EP-bot
pip install selenium
pip install googletrans
python3 -m pip install Pillow pyscreenshot







# VoidsGod's Code:
from PIL import Image
import pyscreenshot as ImageGrab
import time
import pytesseract
from translate import Translator
from pprint import pprint


pytesseract.pytesseract.tesseract_cmd = r'C:\My Folder\Pytesseract\tesseract.exe'

tolang = ""
left = 400
top =  400
right = 1600
bottom = 800
word = "temp"
dest = "temp"
translated = "temp"

im = ImageGrab.grab()
im.save("screenshot.png")
im = Image.open ("screenshot.png")
imc = im.crop((left, top, right, bottom))
imc.save("croppedscreenshot.png")
imc = Image.open("croppedscreenshot.png")
imt = pytesseract.image_to_string(Image.open("croppedscreenshot.png"))
print (imt)
imtlist = imt.split()
print(imtlist)
transto = imtlist[4]
del imtlist[0:5]
print(transto)
print(imtlist)
word = " ".join(imtlist)
print (word)
if transto == "English":
   tolang = "English"
elif transto == "French":
   tolang = "French"
print (tolang)
translator= Translator(to_lang=tolang)
translation = translator.translate(word)
print(translation)
# End
