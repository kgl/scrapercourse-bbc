import requests
from bs4 import BeautifulSoup 

response = requests.get('https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt')

#print(request.text.find('中國多家車企四月交付幾乎腰斬 經濟下行壓力接近武漢疫情時期'))

soup = BeautifulSoup(response.text, 'lxml')
#title = soup.find('span',{'class': 'lx-stream-post__header-text'})
titles = soup.find_all('span',{'class': 'lx-stream-post__header-text'})

#print(title.getText())
#print(titles)
title_list = []
for title in titles:  
    title_list.append(title.getText())
print(title_list)