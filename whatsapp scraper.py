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

global first_call # this should be at first and out every loop and function or shouldn't repeat
first_call = True

driver_path = "/usr/lib/chromium-browser/chromedriver"

birthdays_today= []
birthday_csv = pd.read_csv('birthdays.csv')
column= birthday_csv.birthdate
name = birthday_csv.names

for i, bsdate in enumerate(column):
    bdate = datetime.strptime(bsdate, '%Y-%m-%d')
    if bdate.month == datetime.now().month and bdate.day == datetime.now().day:
        birthdays_today.append(str(name[i]))
        print(name[i])


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("user-data-dir=C:\\Users\\NAVEED\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get('https://web.whatsapp.com')

wait = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"side\"]/div[1]/div/div/div[2]/div/div[1]/p")))

for contact in birthdays_today:
    
    wait = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"side\"]/div[1]/div/div/div[2]/div/div[1]/p")))


    ix = "//*[@id=\"side\"]/div[1]/div/div/div[2]/div/div[1]/p"
    ix_box = driver.find_element("xpath" ,ix)

    ix_box.send_keys(contact)
    
    time.sleep(5)

    contact_find = driver.find_element("xpath" , "//span[@title= '"+contact+"']")
    contact_find.click()
    inp_xpath = "//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"

    input_box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    time.sleep(1)

    input_box.send_keys("Happy Birthday " + contact + " ! "+ Keys.ENTER) 
    print("Successfully Send Message to : "+ contact + '\n')
    wait = WebDriverWait(driver,60).until(EC.staleness_of(ix_box))


