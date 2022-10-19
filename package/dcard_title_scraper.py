from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=ChromeService(
    executable_path=ChromeDriverManager().install()), options=options)

article_number = 240284355

for i in range(200):
    target = f'https://www.dcard.tw/f/relationship/p/{article_number}'
    driver.get(target)

    try:
        title = driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/div/div/article/div[1]/div/h1')
        genre = driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/div/div/article/div[2]/div[1]/a')

        if genre.text != '感情':
            pass
        else:
            # This div contains some number of span that contain the text
            div = driver.find_element(
                By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/div/div/article/div[3]/div/div')
            spans = div.find_elements(By.TAG_NAME, 'span')

            with open('dcardText.txt', 'a', encoding='UTF-8') as f:
                f.write(f'---{title.text}---         {genre.text}版\n\n')
                for span in spans:
                    f.write(span.text + "\n")
    except:
        pass

    print(article_number)
    article_number -= 1


driver.quit()
