from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#insert path to the chromedriver
driver = webdriver.Chrome('/usr/bin/chromedriver') 

#open up wordpress.com
driver.get("https://wordpress.com/")

#allow some time for the page to load before moving on
sleep(2)

#click on sign in button
driver.find_element_by_xpath('//*[@id="lpc-header-nav"]/div/div/div[1]/div/nav/ul[2]/li[1]/a').click()

#allow some time for the page to load before moving on
sleep(5)

#look for the username field
username = driver.find_element_by_xpath('//*[@id="usernameOrEmail"]')
#type in your email
username.send_keys("your username")

#click on next button
driver.find_element_by_xpath('//*[@id="primary"]/div/main/div/div/form/div[1]/div[2]/button').click()

#allow some time for the page to load before moving on
sleep(2)

#look for the password field
password = driver.find_element_by_xpath('//*[@id="password"]')
#type in your password
password.send_keys("your password")

#click on next button
driver.find_element_by_xpath('//*[@id="primary"]/div/main/div/div/form/div[1]/div[2]/button').click()


#-------------------------------------------------------------------------------------------------------------------------------------

#allow some time for the page to load before moving on
sleep(4)

#click on write a new blog post button
driver.find_element_by_xpath('//*[@id="primary"]/main/div[3]/div[2]/div[1]/div[2]/div/div[3]').click()


#allow some time for the page to load before moving on
sleep(8)

driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="primary"]/div[2]/iframe'))

#click on options button
driver.find_element_by_xpath('//*[@id="editor"]/div[1]/div[1]/div[1]/div/div[3]/div[3]/button').click()

sleep(1)

#click on code editor button
driver.find_element_by_xpath('//*[@id="editor"]/div[2]/div/div/div/div/div[2]/div[2]/button[2]').click()

sleep(1)

#Add a Title
title = driver.find_element_by_xpath('//*[@id="post-title-1"]')
title.send_keys("Testing")

#Add content
content = driver.find_element_by_xpath('//*[@id="post-content-0"]')
content.send_keys("Testing Blog Post")

#click on publish button
driver.find_element_by_xpath('//*[@id="editor"]/div[1]/div[1]/div[1]/div/div[3]/button[2]').click()

sleep(3)

#click on publish button
driver.find_element_by_xpath('//*[@id="editor"]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div[1]/div[1]/button').click()



