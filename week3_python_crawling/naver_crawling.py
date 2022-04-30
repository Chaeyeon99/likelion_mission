from bs4 import BeautifulSoup
import requests
from datetime import datetime

now = datetime.now()
print(datetime.today().strftime("\n========== %Y년 %m월 %d일의 차트 순위! ==========\n"))

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%8C%EC%9B%90%EC%B0%A8%ED%8A%B8&oquery=%EB%A9%9C%EB%A1%A0%EC%B0%A8%ED%8A%B8&tqi=UrZ0HsprvN8ssK5ZP%2BsssssstVh-314088"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
results = soup.findAll('div','album_info')

music_rank_file = open("musicrank.txt","a")

rank=0

for result in results:
    rank += 1
    music_rank_file.write(str(rank)+"위: "+result.get_text()+"\n")
    print(rank, "위:", result.get_text())
