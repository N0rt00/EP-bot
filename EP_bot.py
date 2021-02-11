inputList = """
danser to dance
elle joue she plays; she is playing
faire de l'exercice to do exercise
faire du sport to play sports
il joue he plays; he is playing
ils jouent they play (masculine plural); they are playing
ils jouent au tennis they are playing tennis (masc)
ils jouent; elles jouent they play (feminine plural); they are playing
je joue I play
je joue au basket; je joue au basketball I play basketball
je monte I climb; I go up; I am climbing; I am going up
jouer to play
marcher to walk
monter to climb
muscler to work out
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
# Answers Questions
while 1 == 1:
    print('running')
    if 'game?' in driver.current_url:
            time.sleep(0.01)
            inputElement = driver.find_elements_by_xpath("//span[@id='question-text']")
            text = ''
            for i in inputElement:
                text = i.text
            textinput = text
            current = 0
            new = ''
            letter = ''
            if "(starts with" in textinput:
                letter = textinput.split("starts with \"")[1][0]
                textinput = textinput.replace(" (starts with \""+letter+"\")", "")
            if ',' in textinput:
                textinput = textinput.replace(',', ';')
            for i in inputList:
                if textinput in i:
                    v = inputList[current].replace(textinput, '')
                    if v[0] == letter or letter == '':
                        new = v
                    elif v[0] == '' and v[1] == letter:
                        new = v
                    break
                current += 1
            if ';' in new:
                new = new.split(';')[0]
            if new != '':
                userinput = driver.find_element_by_xpath("//input[@id='answer-text']")
                userinput.send_keys(new)
                userinput = driver.find_element_by_xpath("//button[@id='submit-button']")
                userinput.click()
        

