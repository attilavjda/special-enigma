import requests
from bs4 import BeautifulSoup

url = "https://www.freelancer.com" + "/projects/research-writing/condense-rewrite-the-current-evident"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find the div with class='PageProjectViewLogout-detail'
project_detail_div = soup.find('div', class_='PageProjectViewLogout-detail')

# Check if the div is found before proceeding
if project_detail_div:
    # Find all <p> elements within the project_detail_div
    paragraphs = project_detail_div.find_all('p')

    # Extract and print the formatted text content
    for paragraph in paragraphs:
        formatted_text = ' '.join(paragraph.stripped_strings)
        print(formatted_text)
else:
    print("Project detail div not found on the page.")
