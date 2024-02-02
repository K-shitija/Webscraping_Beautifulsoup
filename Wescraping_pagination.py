# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:17:23 2024

@author: KSHITIJA
"""


from bs4 import BeautifulSoup
import requests
import lxml
import time

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

pagination =  soup.find('ul',class_ ='pagination')
pages=pagination.find_all('li', class_ = 'page-item')
last_page = pages[-2].text


links=[]
for page in range(1, int(last_page)+1):
    #https://subslikescript.com/movies_letter-A?page=1
    result = requests.get(f'{website}?page={page}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    

    box = soup.find('article', class_="main-article")
    
    #find_all returns list
    
    
    for link in box.find_all('a', href= True ):
        links.append(link['href'])
        
    
    for link in links:
        try:
            print(link)
            time.sleep(5)
            
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            
            box = soup.find('article', class_="main-article")
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip =True, separator=' ')
            #strip : deletes trailing and leading spaces (beginningand ending of sentence)
            #separator : replaces blank space with new line
            
            with open(f'{title}.txt','w', encoding='utf-8') as file:
                file.write(transcript)
            
        except:
            
            print('-----------Link not working-------------')
            print(link)
            pass
        
    
