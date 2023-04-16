from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import os
import platform
# this should be at first and out every loop and function or shouldn't repeat
global first_call
first_call = True

# Check if chromedriver is in systempath or in the same directory | This will work on all platforms. If not then fail.
# /usr/local/bin/chromedriver and /usr/bin/chromedriver are almost always in system path in Linux and Mac.
# For Windows, you can add chromedriver to system path or put it in the same directory as this script.
# This also removes the need for the user to specify the path to chromedriver.
try:
    subprocess.run(['chromedriver', '--version'], check=True)
except:
    exit("chromedriver not found in systempath or in the same directory")


# Needs admin prilivges to run on windows. This is not needed on Linux and Mac. Default session is secured.
# This is also cross platform.
# For windows this will be C:\Users\username\AppData\Local\Google\Chrome\User Data and for Linux and Mac it will be /home/username/.config/google-chrome
# You dont need to specify the username. It will automatically use the current user.
# But this needs your existing chrome session to be closed. Only plus point is whatsapp will be already logged in.
if (platform.system() == "Windows"):
    userDataPath = os.path.join(os.path.expanduser("~"), "AppData", "Local",
                                "Google", "Chrome", "User Data",)
elif (platform.system() == "Linux"):  # Linux
    userDataPath = os.path.join(
        os.path.expanduser("~"), ".config", "google-chrome",)
else:  # Mac
    userDataPath = os.path.join(os.path.expanduser("~"), "Library", "Application Support",
                                "Google", "Chrome", "User Data",)

birthdays_today = []
birthday_csv = pd.read_csv('birthdays.csv')
column = birthday_csv.birthdate
name = birthday_csv.names

for i, bsdate in enumerate(column):
    bdate = datetime.strptime(bsdate, '%Y-%m-%d')
    if bdate.month == datetime.now().month and bdate.day == datetime.now().day:
        birthdays_today.append(str(name[i]))
        print(name[i])


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument(
    "user-data-dir={}".format(userDataPath))
options.add_experimental_option("detach", True)

# Executable path is depreciated, should not be used. Hence the checking of chromedriver in path above.
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com')

wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
    (By.XPATH, "//*[@id=\"side\"]/div[1]/div/div/div[2]/div/div[1]/p")))

for contact in birthdays_today:

    wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id=\"side\"]/div[1]/div/div/div[2]/div/div[1]/p")))

    ix = "//*[@id=\"side\"]/div[1]/div/div/div[2]/div/div[1]/p"
    ix_box = driver.find_element("xpath", ix)

    ix_box.send_keys(contact)

    time.sleep(5)

    contact_find = driver.find_element(
        "xpath", "//span[@title= '"+contact+"']")
    contact_find.click()
    inp_xpath = "//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"

    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, inp_xpath)))
    time.sleep(1)

    input_box.send_keys("Happy Birthday " + contact + " ! " + Keys.ENTER)
    print("Successfully Send Message to : " + contact + '\n')
    wait = WebDriverWait(driver, 60).until(EC.staleness_of(ix_box))
