import time
import re
import random

from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
options = uc.ChromeOptions()


# Save articles that have some exceptions that the script can't handle. Should be empty.
unvisited = []


def somethong(number: int):
    try:
        driver.get(
            f'view-source:https://www.dcard.tw/f/relationship/p/{number}')
        body_text = driver.find_element(By.TAG_NAME, 'body').text

        body_text = body_text.replace(' ', '')
        body_text = body_text.replace('\n', '')

        title_text = re.findall('<h1.*>(.*)</h1>', body_text)[0]
        category = re.findall('</h1>.*?<a.*?>(.*?)</a>', body_text)[0]

        article = re.findall('<article.*</article>', body_text)

        # if article is deleted or no element in article, don't write to file
        if not article or title_text == '文章已被刪除':
            pass
        else:
            # if some text exist in article list, extract the parargraph from the list
            try:
                paragraph = re.findall('<span>(.*?)</span>', article[0])[0]
                with open('dcardText.txt', 'a', encoding='UTF-8') as f:
                    f.write(
                        f"---{title_text}---   {category}版   文章編號:{number}\n{paragraph}\n\n\n----------------------------------------------------------------------\n")
            except:
                pass

    except Exception as e:
        unvisited.append(
            f'{number}. The exception is {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}')
        pass

    time.sleep(random.uniform(3.0, 4.0))


if __name__ == '__main__':
    driver = uc.Chrome(options=options)
    # for i in range(240298341, 240298300, -1):
    #     somethong(i)
    somethong(240294859)
    print(f'Unvisited articles are\n{str(unvisited)}')
    driver.quit()
