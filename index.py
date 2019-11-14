from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import random

counter = 0
random_word = list(string.ascii_lowercase)

driver = webdriver.Firefox() # Opens firefox
driver.maximize_window() # Maximizes window
driver.implicitly_wait(10) # Gives the page time to load before initiating
driver.get("https://www.Bing.com") # searches

while counter <= 100: # The word and keys are in the loop so the browser only opens once
    random.shuffle(random_word)
    word = "".join(random_word)

    element = driver.find_element_by_id("sb_form_q")
    element.clear()
    element.send_keys(random_word)
    element.send_keys(Keys.RETURN)
    