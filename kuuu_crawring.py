import requests
from bs4 import BeautifulSoup
import re

BASE_URL = 'https://gall.dcinside.com/board/lists/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

# 세션을 초기화하여 쿠키를 관리합니다.
session = requests.Session()


params = {
        'id': 'baseball_new11',
        's_type': 'search_subject',
        's_keyword': '원하는 검색어',
       # 'page': str(pages)
}

resp = session.get(BASE_URL, params=params, headers=headers)

# 세션을 사용하여 요청을 보냅니다.
# 상태 코드 출력
# 응답 내용 확인
#print("Status Code:", resp.status_code)  # 200
#print("Requested URL:", resp.url)  # 요청한 URL 출력
soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)
# 모든 tbody 태그 찾기
#contents = soup.find("tbody")
title = soup.select_one("#kakao_seach_list > tbody")
posts = soup.select(".ub-content > .gall_tit > a")  # 게시글 제목 링크 추출
'''
for post in posts:
    # 제목에서 텍스트 추출
    text = post.get_text(strip=True)
    # 정규식을 사용하여 앞의 넘버링과 뒤의 갤러리명, 날짜 제거
    clean_text = re.sub(r"^\d+|\w+/\d+/\d+$", "", text).strip()
    print(clean_text)
'''
#print(title.text)

titles = [a.get_text(strip=True) for a in soup.select('td.gall_tit > a')]

# 추출된 제목 출력
for title in titles:
    print(title)

# 참조 https://conanmoon.medium.com/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%9D%BC%EA%B8%B0-web-crawling-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-a583a852431e
