from bs4 import BeautifulSoup
import requests
from datetime import datetime

#서버로 GET요청을 보냄
url = "http://www.daum.net/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('a','link_favorsch')

search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위: "+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1