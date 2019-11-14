from selenium import webdriver
from selenium.webdriver.common.keys import Keys
random_word = "Hello"


driver = webdriver.Firefox()
driver.get("https://www.Bing.com")

element = driver.find_element_by_id("sb-form-q")
element.send_keys(random_word)
element.send_keys(Keys.RETURN)
element.close()