#!/usr/bin/python

import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://play.google.com/music/listen?u=1#/artist/Afoktdssbu2nb2n2crnpjs4pu5i/Tomas+Kasey')
time.sleep(5) # Let the user actually see something!

play_button = driver.find_element_by_xpath("""//*[@id="buttonContent"]""")
play_button.click()
time.sleep(100) # Let the user actually see something!
driver.quit()
