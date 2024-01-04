import requests
from bs4 import BeautifulSoup

url = "https://www.freelancer.com/jobs/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

anchors = soup.find_all('a')

for anchor in anchors:
    href_value = anchor.get('href')
    if href_value and "/projects/" in href_value:
        print(href_value)
