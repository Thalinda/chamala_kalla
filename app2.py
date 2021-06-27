from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
driver.get("https://sslproxies.org/")
driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//th[contains(., 'IP Address')]"))))
ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 1]")))]
ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 2]")))]
driver.quit()
proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])
print(proxies)
for i in range(0, len(proxies)):
    try:
        print("Proxy selected: {}".format(proxies[i]))
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}'.format(proxies[i]))
        driver = webdriver.Chrome(options=options, executable_path=PATH)
        driver.get('http://chokolaate.net/choice-award/')
        search = driver.find_element_by_class_name('wpp-options')
        driver.find_element_by_xpath("//input[@value='1703010260032835']").click() 
        driver.find_element_by_class_name("wpp-button-green").click()
        time.sleep(20)
        if "Proxy Type" in WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text"))):
            break
    except Exception:
        driver.quit()
print("Proxy Invoked")