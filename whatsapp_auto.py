
"""

------------How to spam on whatsapp-----------------------------------------------------------------------------------------------

1. We need to install a driver for our browser.
    a. first need to check the version of our browser.
    If its edge. we can get the existing version of edge by using edge://version/
    b. https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads
    from this link get the driver that matches your version.
2. Copy and Paste the following in your terminal.
    a. pip install selenium
    b. pip install msedge-selenium-tools selenium==3.141
3. How to get css_selector, xpath, tag_name?
    a. https://youtu.be/hIZikYCHs4Q    --- //startingtag[@uniquetag="value of the unique tag"]
    b. 
"""





from selenium import webdriver
# we are importing selenium packages with webdriver.

#we want to be able to use selenium keys, like sometimes we have to press enter. 
from selenium.webdriver.common.keys import Keys


#we can take the input form our users too. 
#search_for = input()
#inputstring = input('how are you? This is a spam, dont worry, wont hurt')

#let's import the driver
Browser = webdriver.Edge(r"msedgedriver.exe") 


#we will wait 35 seconds before visiting the site
Browser.implicitly_wait(35)

Browser.get('https://web.whatsapp.com/')

#locate the input textbox and click into it,
#Then type in the name,
#After that, we will press enter
Browser.find_element_by_css_selector("div[title='Search input textbox']").click()
Browser.find_element_by_css_selector("div[title='Search input textbox']").send_keys('Kasita')
Browser.find_element_by_css_selector("div[title='Search input textbox']").send_keys(Keys.ENTER)


#we want to run while loop to execute the spam
#in the while loop, we can define the condition
#we want to send spam as long as our while loop condition is true. 

n=0
while n < 2:
    Browser.find_element_by_xpath("//p[@class='selectable-text copyable-text']").send_keys('This is automatic') #into the textbox
    Browser.find_element_by_xpath("//span[@data-testid='send']").click() #clicking on the send button
    n = n+1
    
"""
Selenium python documentation is here: https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys

"""
