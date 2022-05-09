import requests
from bs4 import BeautifulSoup

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
try:
    response = requests.get(
        'https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt',
        headers = headers, timeout = 5)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find('span',{'class': 'lx-stream-post__header-text'})

        if title:
            result = title.getText()
            print(result)
        else:
            print('元素不存在')

    else:
        print('狀態碼非200')

except Exception as e:
    print(str(e))