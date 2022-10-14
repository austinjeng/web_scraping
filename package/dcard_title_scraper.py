from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
driver.get("https://www.dcard.tw/f/relationship")

def test_eight_components():      
    time.sleep(3)
    scroll_page(1)
    time.sleep(3)
    scroll_page(1)
    time.sleep(3)
    scroll_page(1)    
    

def get_dcard_titles():
    h2_tags = driver.find_elements(By.TAG_NAME, "h2")
    
    a_tags = []
    titles = []
    
    for h2 in h2_tags:
        data = h2.find_elements(By.TAG_NAME, "a")
        a_tags.append(data)
    
    for a in a_tags:
        for i in a:
            data = i.find_element(By.TAG_NAME, 'span')
            titles.append(data)
            
    for i in titles:
        print(i.text)
        

def scroll_page(page_num):
    SCROLL_PAUSE_TIME = 0.5
    
    count = int(0)
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while count < page_num:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
        count+=1

test_eight_components()
driver.quit()