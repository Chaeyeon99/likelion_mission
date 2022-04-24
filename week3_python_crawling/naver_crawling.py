from bs4 import BeautifulSoup
import requests
from datetime import datetime

now = datetime.now()
print("\n","="*8,now.year, "년 ", now.month, "월 ", now.day, "차트 순위!", "="*8, "\n")

# url = "http://ncov.mohw.go.kr/"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')
# results = soup.findAll('div', 'occurrenceStatus')

# for result in results:
#     print(result.get_text())


url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%8C%EC%9B%90%EC%B0%A8%ED%8A%B8&oquery=%EB%A9%9C%EB%A1%A0%EC%B0%A8%ED%8A%B8&tqi=UrZ0HsprvN8ssK5ZP%2BsssssstVh-314088"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
results = soup.findAll('div','album_info')

for result in results:
    print(result.get_text())

# while(True):
#     answer = input("오늘의 날씨 정보도 얻고 싶으신가요?(Y/N): ")
#     if answer == "Y":
#         url = "http://www.naver.com/"
#         response = requests.get(url)

#         soup = BeautifulSoup(response.text, 'html.parser')
#         print(soup.title.string, "에 나타난 오늘의 정보를 알아봅시다.")

#         result = soup.findAll('span', 'news')
#         print(result.get_text())
#         break
#     elif answer == "N":
#         print("오늘도 좋은 하루 되세요~")
#         break
#     else:
#         print("Y/N으로 입력해주세요!")

