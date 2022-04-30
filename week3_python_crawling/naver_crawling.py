from bs4 import BeautifulSoup
import requests
from datetime import datetime

now = datetime.now()
print("\n","="*10,now.year, "년 ", now.month, "월 ", now.day, "일 차트 순위!", "="*10, "\n")

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%8C%EC%9B%90%EC%B0%A8%ED%8A%B8&oquery=%EB%A9%9C%EB%A1%A0%EC%B0%A8%ED%8A%B8&tqi=UrZ0HsprvN8ssK5ZP%2BsssssstVh-314088"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
results = soup.findAll('div','album_info')

i=0

for result in results:
    i = i+1
    print(i, "위:", result.get_text())
