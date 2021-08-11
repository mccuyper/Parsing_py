from bs4 import BeautifulSoup
import requests

url = 'https://news.ycombinator.com/newest'
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

titles = soup.find_all("td", class_='title')
for title in titles:
    title = title.find("a", {"class":'storylink'})
    if title is not None:
        sublink = title.get('href')
        print(str(title.text) + "\n" + str(sublink))
        print("=============================")
