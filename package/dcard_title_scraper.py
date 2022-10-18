from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ChromeService(
    executable_path=ChromeDriverManager().install()),options=options)

driver.get("https://www.dcard.tw/f/relationship")

titles = set()
anchors = []
def get_dcard_titles():
    for i in range(50):
        try:
            a = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div[{i}]/article/h2/a')
            
            if a in anchors:
                pass
            else:
                anchors.append(a)    
                
            titles.add(a.text)
        except:
            pass


def scroll_page():
    for i in range(1, 5000, 1080):
        try:
            driver.execute_script("window.scrollTo(0, {});".format(i))
            get_dcard_titles()
        except:
            driver.execute_script("window.scrollTo(0, {});".format(i))
            get_dcard_titles()


def remove_bottom_login_or_register():
    driver.execute_script("""
    let element = document.getElementsByClassName("sc-91460981-0 eLFHzF");
    if (element)
        element[0].remove();
    """)

# Retrieve all titles in given scroll range
for i in range(1):
    get_dcard_titles()
    driver.execute_script(f"window.scrollTo(0, {int(i*1080)});")

anchors[2].click()
btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div/svg')
btn.click()

# for title in titles:
#     with open('dcardTitles.txt','a', encoding='UTF-8') as f:
#         f.write(f'{title}\n')

time.sleep(2)

driver.quit()
