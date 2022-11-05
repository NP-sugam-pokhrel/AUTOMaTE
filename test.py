
import os


# os.system('cd.. & cd.. && cd AppData/Local &&  rd /s Google /q && dir')
import string
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random 
import time
import tkinter as tk
from selenium.webdriver import ActionChains
from lib2to3.pgen2 import driver


letters = string.ascii_lowercase
# c = webdriver.ChromeOptions()
# c.add_argument("--incognito")

N=7
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_lowercase +
                             'a', k=N))
 




# driver=webdriver.Chrome()



time.sleep(5)

    
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
email = ( ''.join(random.choice(letters) for i in range(10)) ) +"@email.com"
print(email)