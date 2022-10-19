from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-data-dir=/Users/austin/Library/Application Support/Google/Chromes/Default")
driver = webdriver.Chrome(service=ChromeService(
    executable_path=ChromeDriverManager().install()), options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get('view-source:https://www.dcard.tw/f/relationship/p/240282218')
time.sleep(3)
body = driver.find_element(By.TAG_NAME, 'body').text

body = body.replace(' ', '')
body = body.replace('\n', '')

article = re.findall('<article.*</article>', body)[0]
print(article)

# paragraph = re.findall('<span>.*?</sapn>', article)[0]
# print(paragraph)
driver.quit()
