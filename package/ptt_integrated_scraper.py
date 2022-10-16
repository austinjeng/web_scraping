import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    executable_path=ChromeDriverManager().install()))

driver.implicitly_wait(0.1)


def get_current_page_titles():
    titles = driver.find_elements(By.CLASS_NAME, "title")

    return titles


def last_page():
    try:
        prev_btn = driver.find_element(By.LINK_TEXT, "‹ 上頁")
        prev_btn.click()
    except:
        prev_btn.click()


def get_body_text():
    main_content = driver.find_element(By.CSS_SELECTOR, 'div#main-content')

    # with open('pttbody.txt', 'w') as f:
    #     f.write(main_content.text)
    index = main_content.text.index('發信站')
    with open('pttbody.txt', 'a', encoding='UTF-8') as f:
        f.write(main_content.text[:index - 2])


def start():
    driver.get('https://www.ptt.cc/bbs/Stock/index.html')

    for i in range(50):
        title_list = get_current_page_titles()

        for title in title_list[:]:
            if '閒聊' in title.text or '公告' in title.text or '刪除' in title.text or title.text.strip() == '':
                title_list.remove(title)

        for title in title_list:
            try:
                title.find_element(By.TAG_NAME, 'a').click()
                get_body_text()
                driver.back()
            except:
                title.find_element(By.TAG_NAME, 'a').click()
                get_body_text()
                driver.back()

        last_page()

    driver.quit()


start()
