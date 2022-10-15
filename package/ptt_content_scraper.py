from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    executable_path=ChromeDriverManager().install()))


def get_body_text():

    driver.get("https://www.ptt.cc/bbs/Stock/M.1665819567.A.800.html")
    main_content = driver.find_element(By.CSS_SELECTOR, 'div#main-content')

    # with open('pttbody.txt', 'w') as f:
    #     f.write(main_content.text)
    index = main_content.text.index('發信站')
    with open('pttbody.txt', 'a') as f:
        f.write(main_content.text[:index - 2])
    driver.quit()


get_body_text()
