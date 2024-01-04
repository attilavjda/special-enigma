import requests
from bs4 import BeautifulSoup

base_url = "https://www.freelancer.com/jobs/"
current_page = 1

while True:
    url = f"{base_url}{current_page}/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Add your data extraction logic here
        anchors = soup.find_all('a')

        for anchor in anchors:
            href_value = anchor.get('href')
            if href_value and "/projects/" in href_value:
                print(href_value)
                
        current_page += 1
    else:
        print(f"Failed to fetch page {current_page}. Status code: {response.status_code}")
        break
