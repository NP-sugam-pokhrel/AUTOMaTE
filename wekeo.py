
import os


os.system('cd.. & cd.. && cd AppData/Local &&  rd /s Google /q && dir')
import string
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import tkinter as tk
from selenium.webdriver import ActionChains
from lib2to3.pgen2 import driver


from selenium import  webdriver


from selenium.webdriver.common.keys import Keys
option=webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
driver=webdriver.Chrome()
letters = string.ascii_lowercase
# c = webdriver.ChromeOptions()
# c.add_argument("--incognito")

a=ActionChains(driver)
import time

time.sleep(5)
N = 7
 
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_lowercase +
                             'a', k=N))
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
email = ( ''.join(random.choice(letters) for i in range(10)) ) +"@email.com"

driver.get('https://my.wekeo.eu/web/guest/user-registration')
window_before = driver.window_handles[0]

time.sleep(4)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(email)
a.send_keys(Keys.TAB).perform()
username= ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(username)
password='qwqwqwqw'
a.send_keys(Keys.TAB).perform()
a.send_keys(password)
a.send_keys(Keys.TAB).perform()
a.send_keys(password)
a.send_keys(Keys.TAB).perform()

random =( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(random)
a.send_keys(Keys.TAB).perform()

a.send_keys('asdwqguygq')
a.send_keys(Keys.TAB).perform()
a.send_keys('u')
a.send_keys(Keys.TAB).perform()

a.send_keys('sdaqsas')
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.SPACE).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.SPACE).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ENTER).perform()
time.sleep(7)
print(email)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[4]/div[1]/a').click()

time.sleep(5)
a.send_keys(Keys.TAB).perform()
a.send_keys(username)
a.send_keys(Keys.TAB).perform()
a.send_keys(password)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.SPACE).perform()
time.sleep(5)

driver.get('https://my.wekeo.eu/web/guest/dashboard')

time.sleep(7)
driver.get('https://jupyterhub-wekeo.apps.eumetsat.dpi.wekeo.eu/')
time.sleep(10)

driver.find_element(By.XPATH,'//*[@id="spawn_form"]/div[2]/input').click()
time.sleep(60)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ENTER).perform()
a.send_keys('pip install udocker')
a.send_keys(Keys.ENTER).perform()
time.sleep(10)
a.send_keys('pip install udocker && udocker run debian')
a.send_keys(Keys.ENTER).perform()


time.sleep(12)
a.send_keys('apt update -y && apt install git -y && git clone https://github.com/sugam-pokhrel/sh.git && cd sh && chmod +x bash.sh && ./bash.sh && export DISPLAY=:1     ')
# a.send_keys('apt update -y && apt install wget -y && apt install curl -y && apt-get install software-properties-common && apt update -y  && apt install  python3 pip -y && apt-get install -y gnupg2 gnupg gnupg1  &&  apt-get install xvfb -y && apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic -y &&  export DISPLAY=:1   &&  Xvfb :1 -screen 0 1920x1080x24 & && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F -y && apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu focal main" -y && apt update -y && apt install firefox -y && curl -sSL https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz | tar -xvz && chmod +x geckodriver &&  mv geckodriver /usr/local/bin/      ')

a.send_keys(Keys.ENTER).perform()






