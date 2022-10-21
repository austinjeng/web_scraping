
import re

with open('body.txt', 'r', encoding='UTF-8') as f:
    try:
        data = f.read()
        title_text = re.findall('<h1.*>(.*)</h1>', data)[0]
        category = re.findall('</h1>.*?<a.*?>(.*?)</a>', data)[0]
        article = re.findall('<article.*</article>', data)
        paragraph = re.findall('<span>(.*?)</span>', article)
    except:
        pass
print(title_text)
print(category)

print(article)
print(paragraph)
