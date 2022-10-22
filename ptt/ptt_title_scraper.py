from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    executable_path=ChromeDriverManager().install()))


def get_current_page_titles():
    titles = driver.find_elements(By.CLASS_NAME, "title")
    return titles


def test_eight_components():

    driver.get("https://www.ptt.cc/bbs/Stock/index.html")

    for i in range(20):

        titles = get_current_page_titles(driver)
        for data in titles:
            print(data.text, end=" ")

        try:
            prev_btn = driver.find_element(By.LINK_TEXT, "‹ 上頁")
            prev_btn.click()
        except:

            prev_btn.click()


test_eight_components()
