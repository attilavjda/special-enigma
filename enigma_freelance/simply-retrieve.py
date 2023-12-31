import requests
from bs4 import BeautifulSoup

def fetch_freelancer_projects():
    url = "https://www.freelancer.com/jobs/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        project_elements = soup.select('.JobSearchCard-item')
        
        # Extracting relevant information from the project elements
        projects = []
        for project in project_elements[:10]:
            title = project.select_one('.JobSearchCard-primary-heading-link').text.strip()
            description = project.select_one('.JobSearchCard-primary-description').text.strip()
            skills = [skill.text.strip() for skill in project.select('.JobSearchCard-primary-tagsItem')]
            budget = project.select_one('.JobSearchCard-primary-price').text.strip()

            # Check if the 'posted_by' element exists
            posted_by_element = project.select_one('.JobSearchCard-employer')
            posted_by = posted_by_element.text.strip() if posted_by_element else "N/A"

            projects.append({
                'title': title,
                'description': description,
                'skills': skills,
                'budget': budget,
                'posted_by': posted_by
            })

        return projects
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Example usage:
if __name__ == "__main__":
    projects = fetch_freelancer_projects()

    if projects:
        for i, project in enumerate(projects, start=1):
            print(f"Project {i}:\nTitle: {project['title']}\nDescription: {project['description']}\nSkills: {project['skills']}\nBudget: {project['budget']}\nPosted By: {project['posted_by']}\n")
    else:
        print("No projects retrieved.")
