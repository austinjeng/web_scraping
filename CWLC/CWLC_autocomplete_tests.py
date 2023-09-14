import time
import json 

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def login():
    driver.get("https://www.leadercampus.com.tw/login")
    time.sleep(1.0)
    
    #fill in login information
    company_account = driver.find_element(By.NAME, "company_account")
    company_account.send_keys("sculib")
    account = driver.find_element(By.NAME, "account")
    account.send_keys("09156213")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("scu74779")
    
    #comfirm login 
    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn--block.btn--sendForm")
    button.click()

def start_learning():
    #start_learning_btn = driver.find_element(By.XPATH, '//*[@id=\'sticky-wrapper\']/ul/li[2]/a')
    #start_learning_btn.click()
    time.sleep(1.0)
    
    # test_btn = driver.find_element(By.XPATH, "//*[@id="sticky-wrapper"]/ul/li[4]/a")
    # test_btn.click()
    time.sleep(1.0)
    
def testing():
    pass

def start():
    login()
    time.sleep(2)
    
    driver.quit()

if __name__ == "__main__":
    start()

