inputList = """
French English
avril April
dimanche Sunday
février February
juin June
mardi Tuesday
mars March
le soir evening
septembre September
janvier January
octobre October
novembre November
l'après-midi afternoon
le midi midday
l'hiver Winter
l'été Summer
le français French
l'éducation musicale Music
la cour de récréation playground
la cantine canteen
les mathématiques; les maths Maths; mathematics
le printemps Spring
août August
décembre December
les sciences Science
l'art dramatique Drama
le cours class
jeudi Thursday
vendredi Friday
demain tomorrow
une minute a minute
la salle de classe classroom
l'anglais English
juillet July
le matin morning
lundi Monday
mai May
mercredi Wednesday
l'école school; the school
aujourd'hui today
une heure an hour
un élève; une élève student
le collège middle school
la bibliothèque library
les arts plastiques Art
la technologie Technology
le gymnase gymnasium
samedi Saturday
les matières subjects
l'automne Autumn
le professeur; le prof male teacher
la vie de classe homegroup lesson
la menuiserie Woodwork
la horticulture Horticulture
Il est quelle heure? What's the time?
la note score; mark; grade
quelle heure est-il? What's the time?; What time is it?; What is the time?
Il est vingt heures It"s 8pm; It is 8pm
Il est huit heures moins le quart It's a quarter to 8; It is quarter to 8
un collégien male student
une collégienne female student
l'EPS Physical Education; PE
l'histoire-géographie Hums; humanities
la professeure; la prof female teacher
le terrain de sport sports oval; sports field
Dans mon collège il y a un gym In my school there's a gym; In my school there is a gym
Dans mon collège il y a une cantine In my school there's a canteen; In my school there is a canteen
dans mon collège il y a un terrain de sport in my school there's a sports ground; in my school there is a sport ground
Dans mon collège il y a un terrain de foot In my school there is a football ground; In my school there's a footy ground
Dans mon collège il y a un terrain de tennis In my school there's a tennis court; In my school there is a tennis court
"""

inputList = inputList.splitlines()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# Opens EP
driver.get('https://www.educationperfect.com/app/#/login')
time.sleep(0.01)
# Logs In
userinput = driver.find_element_by_xpath("//input[@id='login-username']")
userinput.send_keys('WHSFRI0011')
userinput = driver.find_element_by_xpath("//input[@id='login-password']")
userinput.send_keys("Ram.3649")
userinput = driver.find_element_by_xpath("//span[normalize-space()='Log in']")
userinput.click()
# Waits For You To Open Task
print("Go To Task")
while 1 == 1:
    if 'game?task=' in driver.current_url:
        break
while 1 == 1:
    time.sleep(0.1)
    textinput = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/ui-view[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[2]/span[1]").text
    current = 0
    for i in inputList:
        if textinput in i:
            new = inputList[current].replace(textinput, '')
            break;
        current += 1
    userinput = driver.find_element_by_xpath("//input[@id='answer-text']")
    userinput.send_keys(new)
    userinput = driver.find_element_by_xpath("//button[@id='submit-button']")
    userinput.click()
