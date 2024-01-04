import requests
from bs4 import BeautifulSoup

url = "https://www.freelancer.com/jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
