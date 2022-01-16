import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://docs.oracle.com/javase/jp/8/docs/api/allclasses-noframe.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのliタグを検索して、その文字列を表示する
file = open('/Users/user/git/python/javadic.txt', 'w')

for element in soup.find_all("li"):    # すべてのliタグを検索して表示
    file.write(element.text)
    file.write('\n')
    

