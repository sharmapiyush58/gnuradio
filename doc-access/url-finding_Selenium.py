from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
url = 'http://gnuradio.org/doc/doxygen/'
browser.get(url)

try:
    check1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "MSearchField")))
finally:
    Search = browser.find_element_by_id("MSearchField")
    Search.clear()
    Search.send_keys('block')# we'll send the appropriate block_keys here


try:
    browser.switch_to_frame("MSearchResults")
    check2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "SR_block"))) #SR_key
finally:
    result = browser.find_element_by_id("SR_block")
    final = result.find_element_by_css_selector("a")
    final.click()
