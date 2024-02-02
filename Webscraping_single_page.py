# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:09:48 2024

@author: KSHITIJA
"""

from bs4 import BeautifulSoup
import requests
import lxml


website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')

#print(soup.prettify())

box = soup.find('article', class_="main-article")
title = soup.find('h1').get_text()
#print('box' , box)
print('Title :' , title)

transcript = box.find('div', class_='full-script').get_text(strip =True, separator=' ')
#strip : deletes trailing and leading spaces (beginningand ending of sentence)
#separator : replaces blank space with new line

with open(f'{title}.txt','w', encoding='utf-8') as file:
    file.write(transcript)

