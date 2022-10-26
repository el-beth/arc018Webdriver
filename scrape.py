from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as K
from sys import argv
from time import sleep
import re

if len(argv)!=2:
	print("call me with a url")
	exit(1)

driver = webdriver.Chrome()
# url="https://arc018.com/watch-tv/watch-top-gear-free-39446.5750356"
url=argv[1]

def teardown():
	driver.close()
	driver.quit()

try:
	driver.get(url)
	# just sending ESCAPE doesnt quit the initial gretting modal
	# driver.find_element(by=By.TAG_NAME, value="html").send_keys(K.ESCAPE) # this is incase we want to escape any overlay advert
	for i in driver.find_elements(by=By.CLASS_NAME, value="close"):
		if i.is_displayed():
			i.click()
			break
except Exception as e:
	print("error fetching"+url)
	teardown()

# iterating through the embeds

falsePattern=re.compile('^https:\/\/arc018\.com\/watch-tv\/watch.+$')
frames=[]

for vidSource in driver.find_elements(by=By.CLASS_NAME, value="link-item"):
	vidSource.click()
	# sleep(5)
	while falsePattern.search(driver.find_element(by=By.ID, value="iframe-embed").get_attribute('src')):
		sleep(0.1)
	print(driver.find_element(by=By.ID, value="iframe-embed").get_attribute('src'))
	frames.append(driver.find_element(by=By.ID, value="iframe-embed").get_attribute('src'))

teardown()