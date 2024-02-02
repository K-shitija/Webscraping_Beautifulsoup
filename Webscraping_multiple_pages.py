# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:49:23 2024

@author: KSHITIJA
"""

from bs4 import BeautifulSoup
import requests
import lxml
import time

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
box = soup.find('article', class_="main-article")

#find_all returns list

links=[]
for link in box.find_all('a', href= True ):
    links.append(link['href'])
    
print(links)

for link in links:
    time.sleep(5)
    
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    
    box = soup.find('article', class_="main-article")
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip =True, separator=' ')
    #strip : deletes trailing and leading spaces (beginningand ending of sentence)
    #separator : replaces blank space with new line

    with open(f'{title}.txt','w', encoding='utf-8') as file:
        file.write(transcript)
