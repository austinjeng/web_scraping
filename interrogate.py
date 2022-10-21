from nis import cat
import re

with open('body.txt', 'r', encoding='UTF-8') as f:
    data = f.read()
    title_text = re.findall('<h1.*>(.*)</h1>', data)[0]
    category = re.findall('</h1>.*?<a.*?>(.*?)</a>', data)[0]
    article = re.findall('<article.*</article>', data)[0]
    paragraph = re.findall('<span>(.*?)</span>', article)

print(title_text)
print(category)

print(paragraph)
