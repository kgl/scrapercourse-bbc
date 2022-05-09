import requests
from bs4 import BeautifulSoup 
for page in range(1,4):
    response = requests.get(f'https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt/page/{page}')

    #print(request.text.find('中國多家車企四月交付幾乎腰斬 經濟下行壓力接近武漢疫情時期'))

    soup = BeautifulSoup(response.text, 'lxml')
    #title = soup.find('span',{'class': 'lx-stream-post__header-text'})
    titles = soup.find_all('span',{'class': 'lx-stream-post__header-text'})

    #print(title.getText())
    #print(titles)
    title_list = []
    for title in titles:  
        title_list.append(title.getText())
    #print(title_list)
    urls = soup.find_all('a',{'class':'qa-heading-link'})
    tag_list = []
    for url in urls:
        sub_response = requests.get('https://www.bbc.com' + url.get('href'))
        sub_soup = BeautifulSoup(sub_response.text, 'lxml')
        tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e1hq59l0'})
        for tag in tags:
            tag_list.append(tag.getText())
    print(f"第{page}頁")
    print(title_list)
    print(tag_list)