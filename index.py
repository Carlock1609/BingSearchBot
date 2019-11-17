from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import random
import time

counter = 0
random_word = list(string.ascii_lowercase)

driver = webdriver.Firefox() # Opens firefox
driver.set_window_size(600,400) # Small window -> fasting loading
driver.implicitly_wait(10) # Gives the page time to load before initiating
driver.get("https://www.Bing.com") # grabs the url

while counter <= 100: # The word and keys are in the loop so the browser only opens once
    random.shuffle(random_word) # random word
    word = "".join(random_word)

    searchbar = driver.find_element_by_id("sb_form_q") #looking for the id for the searchbar

    searchbar.send_keys(Keys.CONTROL,'a') # clears searchbar
    searchbar.send_keys(Keys.DELETE) 
    time.sleep(1) 
    searchbar.send_keys(random_word) # inputs word
    searchbar.send_keys(Keys.RETURN) # submits
    time.sleep(1) # Giving the script time to load for some reason makes it work
    