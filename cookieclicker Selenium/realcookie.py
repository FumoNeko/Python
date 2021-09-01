from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get(URL)
store = driver.find_elements_by_xpath('//*[@id="store"]')
print(len(store))
