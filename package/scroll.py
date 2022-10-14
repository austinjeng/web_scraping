from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
driver.get("https://www.dcard.tw/f/relationship")

def scroll_page(page_num):
    SCROLL_PAUSE_TIME = 0.5
    
    count = int(0)
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while count < page_num:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
        count+=1

