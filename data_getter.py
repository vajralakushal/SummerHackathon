from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver_') #make sure that you have the chrome webdriver installed and placed in path
driver.get("https://simple.wikipedia.org")
