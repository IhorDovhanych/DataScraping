from requests import get
from bs4 import BeautifulSoup

URL = "https://irshavaotg.gov.ua/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

page = get(URL, headers=HEADERS)
soup = BeautifulSoup(page.text)

with open('links.txt', 'w') as file:
    for link in soup.find_all('a'):
        file.write(f"{link.get('href')}\n")