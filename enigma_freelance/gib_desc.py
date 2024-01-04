import requests
from bs4 import BeautifulSoup

def fetch_wacky_project_narrative() -> str:
    """
    Snags the zany saga of the most recent shenanigans on Freelancer.com.

    Returns:
        str: The quirky narrative of the latest escapade.
    """
    url_of_wonder = "https://www.freelancer.com/jobs/"
    magical_response = requests.get(url_of_wonder)

    if magical_response.status_code == 200:
        soup_of_delight = BeautifulSoup(magical_response.text, 'html.parser')
        latest_spectacle_element = soup_of_delight.select_one('.JobSearchCard-item')

        if latest_spectacle_element:
            tale_of_the_unusual = latest_spectacle_element.select_one('.JobSearchCard-primary-description').text.strip()
            return tale_of_the_unusual
        else:
            return "Alas! No project discovered on this enchanted page."
    else:
        return f"Alack! Failed to procure data. Status code: {magical_response.status_code}"

if __name__ == "__main__":
    whimsical_project_narrative = fetch_wacky_project_narrative()
    print(f"Wacky Project Narrative:\n{whimsical_project_narrative}")
