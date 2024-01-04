import requests
from bs4 import BeautifulSoup

def fetch_latest_project_url():
    """
    Fetches the URL of the latest project posted on Freelancer.com.

    Returns:
        str: The URL of the latest project.
    """
    url = "https://www.freelancer.com/jobs/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        latest_project_link = soup.select_one('.JobSearchCard-primary-heading-link')

        if latest_project_link:
            return latest_project_link['href']
        else:
            return "No project link found on the page."
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"

def fetch_project_description(project_url):
    """
    Fetches the full project description from the specific project page on Freelancer.com.

    Args:
        project_url (str): The URL of the specific project.

    Returns:
        str: The full project description.
    """
    response = requests.get(project_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        description_element = soup.select_one('.project-description')

        if description_element:
            full_description = description_element.get_text(strip=True)
            return full_description
        else:
            return "No project description found on the page."
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"

if __name__ == "__main__":
    latest_project_url = fetch_latest_project_url()

    if latest_project_url:
        project_description = fetch_project_description(latest_project_url)
        print(f"Full Project Description:\n{project_description}")
    else:
        print("Could not retrieve the latest project URL.")
