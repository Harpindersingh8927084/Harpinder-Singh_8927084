# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(5)

# Navigating to the books section
Books = driver.find_element(By.XPATH, "//a[text()='Books']")
Books.click()
time.sleep(2)

# Selecting Canadian books
Canadian_Books = driver.find_element(By.XPATH, "//a[text()='Canadian Books']")
Canadian_Books.click()
time.sleep(2)

# Selecting Best Sellers books
BestSellers_Books = driver.find_element(By.XPATH, "//span[normalize-space()='Best Sellers & More']")
BestSellers_Books.click()
time.sleep(2)

# Selecting Most Read
MostRead_Books = driver.find_element(By.XPATH, "//img[@alt='Amazon Charts Most Read']")
MostRead_Books.click()

# Closing the webdriver
driver.close()