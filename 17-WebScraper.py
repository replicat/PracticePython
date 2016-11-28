import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

for heading in soup.find_all(class_="story-heading"):
    try:
        print(heading.text.strip())
    except:
        pass