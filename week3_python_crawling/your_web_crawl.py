from bs4 import BeautifulSoup
import requests

url = "https://about-me-introduce.netlify.app/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.h1.string)


# file = open("new.html",'w')
# file.write(response.text)
# file.close()