# moduel import
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://gall.dcinside.com/board/lists/'

para = {'id' : 'iamsolo',}

header = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

resp = requests.get(BASE_URL, params=para, headers=header)

# 상태 코드 출력
#print("Status Code:", resp.status_code) # 200

# 요청 URL 확인
print("Requested URL:", resp.url)

# 응답 내용 확인
#print("Response Content:", resp.content)
soup = BeautifulSoup(resp.content, 'html.parser')
#print(soup)

contents = soup.find('article').find_all('a')
#print(contents)

'''
Status Code: 200
Requested URL: https://gall.dcinside.com/board/lists/?id=iamsolo

'''


for i in contents:
    #print('-'*15)
    if i.get('href'):
        title_tag =  i.get_text(strip=True)
        if title_tag:
            print(title_tag)
   # print(i)
