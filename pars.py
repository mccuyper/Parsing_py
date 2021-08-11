from bs4 import BeautifulSoup
import requests


x = 0
while True:
    if x == 0:
        url = 'https://news.ycombinator.com/newest'
    else:
        url = 'https://news.ycombinator.com/newest'+nxt
        
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    titles = soup.find_all("td", class_='title')
    for title in titles:
        title = title.find("a", {"class":'storylink'})
        if title is not None and 'github.com' in str(title):
            sublink = title.get('href')
            print(str(title.text) + "\n" + str(sublink))
            print("=============================")


    next = soup.find(class_="morelink")
    nextlink = next.get("href")

    nxt = nextlink[6:]
    x += 1