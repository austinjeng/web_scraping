from os import remove
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(
    executable_path=ChromeDriverManager().install()))


driver.get("https://www.dcard.tw/f/relationship")
time.sleep(2)

titles = set()


def get_dcard_titles():
    h2_tags = driver.find_elements(By.TAG_NAME, "h2")

    a_tags = []

    for h2 in h2_tags:
        data = h2.find_elements(By.TAG_NAME, "a")
        a_tags.append(data)

    for a in a_tags:
        for i in a:
            data = i.find_element(By.TAG_NAME, 'span')
            titles.add(data.text)


def scroll_page():
    for i in range(1, 100000, 1080):
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


remove_bottom_login_or_register()
scroll_page()

with open('dcardTitles.txt', 'a') as f:
    for i in titles:
        f.write(i+"\n")

driver.quit()
