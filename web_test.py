from selenium import webdriver
from selenium.webdriver.common.keys import Keys

search_for=input("what do you want to search for?")



edgeBrowser = webdriver.Edge("msedgedriver.exe")
edgeBrowser.implicitly_wait(15)
edgeBrowser.get('https://www.youtube.com/')



edgeBrowser.find_element_by_xpath("//input[@id='search']").send_keys(search_for)
edgeBrowser.find_element_by_xpath("//input[@id='search']").send_keys(Keys.RETURN)
edgeBrowser.find_element_by_xpath("//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']").click()
