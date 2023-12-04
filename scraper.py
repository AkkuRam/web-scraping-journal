import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.webofscience.com/wos/woscc/full-record/WOS:001056613800001')

# Currently this is logging into the website to web scrape, since I don't have access to a VPN
username = ""
password = ""

driver.find_element(By.ID, "mat-input-0").send_keys(username)
driver.find_element(By.ID, "mat-input-1").send_keys(password)
driver.find_element("name", "login-btn").click()  

source = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//a[@data-ta='jcr-link']"))
)

# clicking is a bit inconsistent sometimes, I switch between these statements (needs fixing)
source.click()
# ActionChains(driver).move_to_element(source).click().perform()
time.sleep(5)

categories = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//td[@class='ng-star-inserted']"))
)
print(categories.text)  

while(True):
    pass

