import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
import re
import random
options = uc.ChromeOptions()
#options.user_data_dir = "/Users/austin/Library/Application Support/Google/Chromes/Default"

unvisited = []


def somethong(number: int):
    try:
        driver.get(
            f'view-source:https://www.dcard.tw/f/relationship/p/{number}')
        body_text = driver.find_element(By.TAG_NAME, 'body').text

        body_text = body_text.replace(' ', '')
        body_text = body_text.replace('\n', '')
        with open('body.txt', 'w', encoding='UTF-8') as f:
            f.write(body_text)

        # <h1 class="sc-ae7e8d73-0 jQMxOW">Re: 以前發生過的詐騙手法又復燃了</h1>
        title_text = re.findall('<h1.*>(.*)</h1>', body_text)[0]
        print(title_text)

        article = re.findall('<article.*</article>', body_text)[0]
        paragraph = re.findall('<span>(.*?)</span>', article)[0]
        with open('dcardText.txt', 'a', encoding='UTF-8') as f:
            f.write(
                f"---{title_text}---\n{paragraph}\n\n\n----------------------------------------------------------------------\n")
    except:
        unvisited.append(number)
        pass

    time.sleep(random.uniform(3.0, 4.0))


if __name__ == '__main__':
    driver = uc.Chrome(options=options)
    for i in range(240284377, 240284000, -1):
        somethong(i)
    driver.quit()
