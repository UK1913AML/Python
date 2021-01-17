import requests
from bs4 import BeautifulSoup
url = "https://www.example.com/"
path = "raw_data.txt"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
elements = soup.find_all("h3")

with open(path, "w", encoding="UTF-8") as f:
    for element in elements:
        f.write(str(element.text) + "\n")
