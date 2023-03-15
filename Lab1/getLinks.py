from requests import get
from bs4 import BeautifulSoup
#* vv-variables-vv
# URL = "https://irshavaotg.gov.ua/"
URL = "https://www.pythontutorial.net/python-basics/python-write-text-file/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
page = get(URL, headers=HEADERS)
soup = BeautifulSoup(page.text, 'lxml')
links_arr = []
#* ^^-variables-^^

with open('./links.txt', 'w') as file:
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and href not in links_arr:
            if 'www' in href: 
                file.write(f"{href}\n")
                links_arr.append(href)
    for link in links_arr:
        URL = link
        page = get(URL, headers=HEADERS)
        soup = BeautifulSoup(page.text, 'lxml')
        for additional_link in soup.find_all('a'):
            href = additional_link.get('href')
            if href is not None and href not in links_arr:
                if 'www' in href: 
                    file.write(f"{href}\n")
                    links_arr.append(href)