from PIL import Image
import pyscreenshot as ImageGrab
import time
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
li1 = 1
li12 = 1
li2 = 1
li22 = 1
left = 400
top =  1000
right = 2500
bottom = 1500
list1 = pytesseract.image_to_string(Image.open("list1.png"))
try:
    list12 = pytesseract.image_to_string(Image.open("list12.png"))
except:
    print("")
list2 = pytesseract.image_to_string(Image.open("list2.png"))
try:
    list22 = pytesseract.image_to_string(Image.open("list22.png"))
except:
    print("")

def table(listName, listPic):
    listName = []
    listName = listPic.split("\n")
    listName = [x for x in listName if x]
    listName = listName[:-1]
    return listName

li1 = table(li1, list1)

try:
    li12 = table(li12, list12)
except:
    print("")

li2 = table(li2, list2)

try:
    li22 = table(li22, list22)
except:
    print("")

#print(li1)
#print(li2)

try:
    list1 = li1 + li12
except:
    list1 = li1
try:
    list2 = li2 + li22
except:
    list2 = li2

print (list1)
print(list2)

print("Enter Your Language:")
language = input()

driver = webdriver.Chrome('/Users/samthornton/chromedriver')
driver.get("https://www.educationperfect.com/app/#/login")

time.sleep(3)

email = driver.find_element(By.ID, 'login-username')
password = driver.find_element(By.ID, 'login-password')
logInButton = driver.find_element(By.ID, 'login-submit-button')
email.send_keys("username")
password.send_keys("password")
logInButton.click()
time.sleep(4)
print(language)
driver.get("https://www.educationperfect.com/app/#/dashboard/" + language + "/");
url = driver.current_url
print("https://www.educationperfect.com/app/#/dashboard/" + language + "/")
while url == "https://www.educationperfect.com/app/#/dashboard/" + language + "/":
    url = driver.current_url
print("Open Your Task Within The Next 10 Seconds")
time.sleep(10)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Starting Script")
time.sleep(2)
url = driver.current_url
urlstorage = url
while url == urlstorage:

    im = ImageGrab.grab()
    im.save('fullscreen.png')
    print('saved fullscreen')
    im = Image.open ('fullscreen.png')
    im1 = im.crop((left, top, right, bottom))
    im1.save('fullscreen2.png')
    print('saved crop')
    text = pytesseract.image_to_string(Image.open('fullscreen2.png'))
    print (text)
    text = text.rstrip('\n\x0c')
    print (text)
    if language == 'french':
        index = list2.index(text)
        ans = list1[index]
    else:
        index = list1.index(text)
        ans = list2 [index]
    answer_box = driver.find_element_by_css_selector('#answer-text-container > #answer-text')
    answer_box.send_keys(ans)
    driver.find_element_by_id('submit-button').click()

