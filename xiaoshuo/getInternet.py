import requests as  re
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
ass="story">Once upon a time there were three little sisters; and their names were
<a hr
<p clef="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
response = re.get('https://blog.csdn.net/idiot_xue/article/details/72626332')
# print(response.text)
# soup = BeautifulSoup(response.text)
soup = BeautifulSoup(html_doc)


print(soup.get_text)
