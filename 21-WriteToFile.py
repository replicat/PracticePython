import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

with open('21-TheFile.txt', 'w') as open_file:    
    for content in soup.find_all("p"):
        try:
            open_file.write(content.text.strip() + "\n")
        except:
            pass