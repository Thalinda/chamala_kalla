from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import time

req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list
ind = []
for proxy in proxies:
    if proxy.country == 'SriLanka':
        ind.append(proxy)
PROXY = proxies[0].get_address()
print(PROXY)
webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    
    "proxyType":"MANUAL",
    
}
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('http://chokolaate.net/choice-award/')
search = driver.find_element_by_class_name('wpp-options')
driver.find_element_by_xpath("//input[@value='1703010260032835']").click() 
driver.find_element_by_class_name("wpp-button-green").click()
time.sleep(10)
driver.quit()