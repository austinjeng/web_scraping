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

        title_text = re.findall('<h1.*>(.*)</h1>', body_text)[0]
        category = re.findall('</h1>.*?<a.*?>(.*?)</a>', body_text)[0]
        print(title_text)

        article = re.findall('<article.*</article>', body_text)
        
        #if article is deleted or no text is found in content, don't write to file
        if not article or title_text == '文章已被刪除':
            pass
        else:    
            #if some text exist in article list, extract the parargraph from the list
            paragraph = re.findall('<span>(.*?)</span>', article[0])[0]
            with open('dcardText.txt', 'a', encoding='UTF-8') as f:
                f.write(
                    f"---{title_text}---   {category}版   文章編號:{number}\n{paragraph}\n\n\n----------------------------------------------------------------------\n")
    except:
        unvisited.append(number)
        pass

    time.sleep(random.uniform(3.0, 4.0))


if __name__ == '__main__':
    driver = uc.Chrome(options=options)
    for i in range(240298341, 240298300, -1):
        somethong(i)
        
    print(f'Unvisited articles are\n{str(unvisited)}')
    driver.quit()
