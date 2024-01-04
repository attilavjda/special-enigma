import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import Optional

def fetch_latest_project_description() -> Optional[str]:
    url = "https://www.freelancer.com/jobs/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    latest_project_link = soup.select_one('.ProjectTable-title a')

    if not latest_project_link:
        return "No link to the latest project found on the parent page."

    print(f"Latest Project Link: {latest_project_link['href']}")
    latest_project_url_relative = latest_project_link['href']
    latest_project_url = urljoin(url, latest_project_url_relative)

    response_project = requests.get(latest_project_url)

    if response_project.status_code != 200:
        return f"Failed to fetch individual project page. Status code: {response_project.status_code}"

    soup_project = BeautifulSoup(response_project.text, 'html.parser')
    description_element = soup_project.select_one('.JobDescription-section .JobDescription-section-content')

    if not description_element:
        return "No project description found on the individual project page."

    return description_element.get_text(strip=True)

if __name__ == "__main__":
    latest_project_description = fetch_latest_project_description()

    if latest_project_description:
        print(f"Full Project Description:\n{latest_project_description}")
    else:
        print("Could not retrieve the latest project description.")
