# this program using selenium to make translate from the detect language to English.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# user inputting what He wants to translate.
user_input = input("what do you want to translate:")

my_driver = webdriver.Chrome(executable_path="C:/Users/tzuf_bar_or/Desktop/chromedriver.exe")
my_driver.get("https://translate.google.com")
time.sleep(1)
my_driver.find_element(By.ID, "yDmH0d").click()
my_driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys(user_input)