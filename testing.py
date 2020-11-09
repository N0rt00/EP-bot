import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from googletrans import Translator, constants
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
import os
import time
import pyscreenshot as ImageGrab
translator = Translator()
left = 300
top =  700
right = 2500
bottom = 1500
def listToString(s):  
    str1 = " " 
    return (str1.join(s)) 
driver = webdriver.Chrome('/Users/samthornton/chromedriver')
driver.get("https://www.educationperfect.com/app/#/dashboard/french/")
inputElement = driver.find_element_by_id("login-username")
inputElement.send_keys('WHSTHO0065')
inputElement = driver.find_element_by_id("login-password")
inputElement.send_keys('Bl0cks#French')
inputElement.send_keys(Keys.ENTER)
time.sleep(10)
driver.find_element_by_id('start-button-main-label').click()
print('done')
time.sleep(2)
for i in range(1):
    im = ImageGrab.grab()
    im.save('fullscreen.png')
    im = Image.open ('fullscreen.png')
    im1 = im.crop((left, top, right, bottom))
    im1.save('fullscreen2.png')
    text = pytesseract.image_to_string(Image.open('fullscreen2.png'))   
    li = text.splitlines()
    li2 = ' '.join(li).split()
    print (li2)
    lang_to = li2[4]
    lang_to = li2[4]
    del li2[0]
    del li2[0]
    del li2[1]
    del li2[0]
    del li2[0]
    li2 = listToString(li2)
    word = li2
    print (lang_to)
    print (word)
    if lang_to == 'English':
        lang_to = 'en'
    if lang_to == 'French':
        lang_to = 'fr'
    print (lang_to)
    #translation is not working
    translation = translator.translate(word)
    print (translation.text)
